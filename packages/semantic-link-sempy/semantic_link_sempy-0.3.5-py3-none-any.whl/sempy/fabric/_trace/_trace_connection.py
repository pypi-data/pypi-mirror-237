import pandas as pd

from sempy.fabric._trace._trace import Trace
from typing import Dict, List, Optional


class TraceConnection:
    """
    Connection object for starting, viewing, and removing Traces.

    Python wrapper around `Microsoft Analysis Services Tabular Server
    <https://learn.microsoft.com/en-us/dotnet/api/microsoft.analysisservices.tabular.server?view=analysisservices-dotnet>`_.

    Parameters
    ----------
    server : Tabular Server
        Server to wrap.
    """
    def __init__(self, server):
        self.tom_server = server

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.disconnect_and_dispose()

    def create_trace(self, event_schema: Dict[str, List[str]], name: Optional[str] = None) -> Trace:
        """
        Create a blank Trace object on this connection.

        Parameters
        ----------
        event_schema : dict
            Dictionary containing event types as keys and list of column names for that event as values.
            Both event and column names must be specified as strings, without spaces and in PascalCase.
        name : str, default=None
            Name identifying trace. If None, the trace name will be "SemanticLinkTrace_<GUID>".

        Returns
        -------
        Trace
            Trace object to be customized and started.
        """
        return Trace(self.tom_server, event_schema, name)

    def list_traces(self) -> pd.DataFrame:
        """
        List all stored (active or inactive) traces on a this connection.

        Returns
        -------
        DataFrame
            DataFrame containing the ID, name, timestamp, and state of each trace.
        """
        trace_info = []
        for trace in self.tom_server.Traces:
            info = {
                "ID": trace.ID,
                "Name": trace.Name,
                "Created Timestamp": trace.CreatedTimestamp,
                "Is Started": trace.IsStarted,
            }
            trace_info.append(info)

        return pd.DataFrame(trace_info, columns=["ID", "Name", "Created Timestamp", "Is Started"])

    def drop_traces(self) -> None:
        """
        Remove all traces on a server.
        """
        trace_collection = [trace for trace in self.tom_server.Traces]
        for trace in trace_collection:
            self._stop_and_drop_trace(trace)

    def drop_trace(self, trace_name: str) -> None:
        """
        Drop the trace with the specified name from the server.

        Parameters
        ----------
        trace_name : str
            Name of trace to drop.
        """
        trace_collection = [trace for trace in self.tom_server.Traces]
        for trace in trace_collection:
            if trace.Name == trace_name:
                self._stop_and_drop_trace(trace)

    def _stop_and_drop_trace(self, trace):
        from Microsoft.AnalysisServices import DropOptions

        if trace.IsStarted:
            trace.Stop()
        trace.Drop(DropOptions.IgnoreFailures)

    def disconnect_and_dispose(self) -> None:
        """
        Clear all traces on a server.
        """
        self.tom_server.Disconnect()
        self.tom_server.Dispose()
