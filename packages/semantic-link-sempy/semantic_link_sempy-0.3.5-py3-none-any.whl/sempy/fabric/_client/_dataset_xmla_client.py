import os
import tempfile
import pandas as pd
from uuid import UUID, uuid4

from sempy.fabric._client._utils import _init_analysis_services, create_tom_server, _build_adomd_connection_string
from sempy.fabric._client._base_dataset_client import BaseDatasetClient
from sempy.fabric._environment import _get_workspace_url
from sempy.fabric._token_provider import create_on_access_token_expired_callback, TokenProvider

from sempy._utils._log import log_xmla

from typing import Optional, Union, TYPE_CHECKING, List, Tuple, Dict

if TYPE_CHECKING:
    from sempy.fabric._client import WorkspaceClient


class DatasetXmlaClient(BaseDatasetClient):
    """
    Client for access to Power BI data in a specific dataset (database) using an XMLA client.

    Generally, a single instance of the class is needed per dataset (database),
    where it can execute multiple DAX queries.

    In contrast to :class:`PowerBIWorkspace` it wraps a different XMLA client:
    `AdomdDataAdapter <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.adomdclient.adomddataadapter?view=analysisservices-dotnet>`__
    which deals with data access rather than the PowerBI Model (metadata).
    Each client will usually map to a Dataset (Database) i.e. one or more clients can be instantiated
    within each accessed workspace.

    Parameters
    ----------
    workspace : str or WorkspaceClient
        PowerBI workspace name or workspace client that the dataset originates from.
    dataset : str or UUID
        Dataset name or UUID object containing the dataset ID.
    token_provider : TokenProvider, default=None
        Implementation of TokenProvider that can provide auth token
        for access to the PowerBI workspace. Will attempt to acquire token
        from its execution environment if not provided.
    """
    def __init__(
            self,
            workspace: Union[str, "WorkspaceClient"],
            dataset: Union[str, UUID],
            token_provider: Optional[TokenProvider] = None
    ):
        _init_analysis_services()

        BaseDatasetClient.__init__(self, workspace, dataset, token_provider)

    def _get_connected_dataset_server(self, readonly: bool = True):
        connection_string = self._get_dax_connection_string(readonly)
        tom_server = create_tom_server(connection_string, self.token_provider)

        return tom_server

    def _get_dax_connection_string(self, readonly: bool = True) -> str:
        workspace_url = _get_workspace_url(self._workspace_client.get_workspace_name())
        return _build_adomd_connection_string(workspace_url, self._dataset_name, readonly)

    def _evaluate_dax(self, query: str, verbose: int = 0, batch_size: int = 100000) -> pd.DataFrame:
        return self._get_DAX(connection_string=self._get_dax_connection_string(), dax_string=query, batch_size=batch_size, verbose=verbose)

    def _evaluate_measure(
        self,
        measure: Union[str, List[str]],
        groupby_columns: List[Tuple[str, str]],
        filters: Dict[Tuple[str, str], List[str]],
        num_rows: Optional[int] = None,
        batch_size: int = 100000,
        verbose: int = 0,
    ) -> pd.DataFrame:

        # we should always quote table names (e.g. Date/Calendar as table name will fail without quotes)
        groupby_string = ", ".join(f"'{col[0]}'[{col[1]}]" for col in groupby_columns)

        measure_lst = measure if isinstance(measure, list) else [measure]
        measure_string = ", ".join(f'"{m}", CALCULATE([{m}])' for m in measure_lst)

        filter_clauses = []
        for table_col, filter_list in filters.items():
            table_name = table_col[0]
            col_name = table_col[1]
            # DAX requires the "IN" items to use double quotes within braces:
            filter_vals = "{" + ", ".join([f'"{val}"' for val in filter_list]) + "}"
            # Create individual FILTER functions for every filter specified by user (table names always quoted with single quotes)
            # See https://learn.microsoft.com/en-us/dax/filter-function-dax)
            filter_clauses.append(f"FILTER('{table_name}', '{table_name}'[{col_name}] IN {filter_vals})")
        # Final String: FILTER('Table1', 'Table1'[Col1] IN {"X", "Y"}), FILTER('Table2', 'Table2'[Col2] IN {"A"})
        filter_string = ", ".join(filter_clauses)

        summarize_columns = 'SUMMARIZECOLUMNS('
        if len(groupby_string) > 0:
            summarize_columns += f'{groupby_string}, '
        if len(filter_string) > 0:
            summarize_columns += f"{filter_string}, "
        summarize_columns += f"{measure_string})"

        if num_rows:
            dax_string = f"EVALUATE TOPN({num_rows}, {summarize_columns})"
        else:
            dax_string = f"EVALUATE {summarize_columns}"

        if verbose > 0:
            print(f"Executing DAX query: {dax_string}")

        df = self._get_DAX(connection_string=self._get_dax_connection_string(), dax_string=dax_string, verbose=verbose)

        # DAX returns all measures in the form [MeasureName]. To maintain consistency with REST we remove this formatting.
        renamed_measure_cols = {f"[{m}]": m for m in measure_lst}
        df.rename(columns=renamed_measure_cols, inplace=True)

        return df

    @log_xmla
    def _get_DAX(self, connection_string: str, dax_string: str, batch_size: int = 100000, verbose: int = 0) -> pd.DataFrame:
        # = Chapter 1 =
        # At the beginning there was a simple implementation that used the AdomdDataAdapter filling DataTable and
        # directly accessing the DataTable via PythonNet. This was very slow and the team was sad.
        # = Chapter 2 =
        # Then a new age came and a might warrior created a .NET implementation which access the DataTable
        # without PythonNet and wrote a parquet file. The team was happy and the performance was good.
        # Tales are told about 15x to 110x performance improvements.
        # = Chapter 3 =
        # Then the code was rolled out and customers discovered more issues. The team was sad again.
        # On large datasets (>45mio rows) the code failed with a parquet exception.
        # We gather reports about "ArgumentOutOfRangeException: Specified argument was out of the range of valid values. (Parameter 'minimumLength')"
        # To fix the issue, the parquet row groups were split up into smaller chunks.
        # Along the way we also ditched the AdomdDataAdapter & DataTable and directly interfaced with DataReader.
        # This allows us to reduce the memory footprint (previously the whole dataset was loaded into memory - namely the DataTable), then copied again
        # into various Arrays to satisfy the parquet writer and lastly the pandas dataframe.
        # Using the data reader we can bound the memory consumption using the batch size.
        # Additionally reading the data from Adomd and post-processing & writing the parquet file is now interleaved.
        # The test set was ~650MB of snappy compressed parquet, which is 45mio rows and 14 columns.
        # Running on the dev box, the entire code took 70mins to execute. On Fabric it takes 16mins.

        from Microsoft.Fabric.SemanticLink import ParquetWriter
        from Microsoft.AnalysisServices import AccessToken
        from System import Func

        get_access_token = create_on_access_token_expired_callback(self.token_provider)

        # Manually build file temp_file_name. Using a simpler tempfile.NamedTemporaryFile breaks on Windows,
        # where file held by python cannot be overriden by C#
        temp_file_name = os.path.join(tempfile.gettempdir(), f"sempy-{uuid4()}.parquet")

        try:
            ParquetWriter.DAXToParquet(connection_string,
                                       dax_string,
                                       temp_file_name,
                                       batch_size,
                                       verbose,
                                       onAccessTokenExpired=Func[AccessToken, AccessToken](get_access_token))
            df = pd.read_parquet(temp_file_name)
        finally:
            try:
                os.remove(temp_file_name)
            except FileNotFoundError:
                # File will not be written if exception thrown in DAXToParquet (e.g. error in DAX)
                pass

        return df

    def __repr__(self):
        return f"DatasetXmlaClient('{self._workspace_client.get_workspace_name()}[{self._dataset_name}]')"
