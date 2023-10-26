import pandas as pd
import warnings
from pandas.core.dtypes.common import is_dtype_equal
from typing import List, Tuple


def _pandas_merge_cast(left_df, left_on, right_df, right_on, relationship=None, warn=True):

    if not isinstance(left_on, str) or not isinstance(right_on, str):
        raise TypeError(f"Unexpected types {type(left_on)} and {type(right_on)}: not strings")

    string_types = ["string", "unicode", "mixed", "bytes", "empty"]

    # Try to cast some common type issues to make pandas behave more nicely
    if not is_dtype_equal(left_df[left_on], right_df[right_on]):
        left_dtype = pd.api.types.infer_dtype(left_df[left_on])
        right_dtype = pd.api.types.infer_dtype(right_df[right_on])
        msg = f"Mismatching dtypes in merging along relationship {relationship}."
        if (left_dtype in string_types):
            if (right_dtype in string_types):
                # both are string
                pass
            else:
                # left is string but right is not
                if warn:
                    warnings.warn(msg)
                right_df = right_df.astype({right_on: str})

        elif right_dtype in string_types:
            # right is string but left is not
            if warn:
                warnings.warn(msg)
            left_df = left_df.astype({left_on: str})

    return left_df, right_df


def rename_and_validate(df: pd.DataFrame, schema: List[Tuple[str, str, str]]) -> pd.DataFrame:
    """
    Rename columns in a dataframe according to a schema and validate that the schema is satisfied.

    Parameters
    ----------
    df : pd.DataFrame
        The input data.
    schema : List[Tuple[str, str, str]]
        The expected schema. Each element is a tuple of (source column name, destination column name, column type).

    Returns
    -------
    pd.DataFrame
        The renamed dataframe.
    """
    if df is None or len(df) == 0:
        return pd.DataFrame({
            dest: pd.Series(dtype=column_type)
            for _, dest, column_type in schema
        })

    src_columns = [src for src, _, _ in schema]
    missing_columns = [col for col in src_columns if col not in df.columns.values]

    if len(missing_columns) > 0:
        # don't fail, just warn. Assuming the backend returns less data than expected, we should still
        # pass the data
        warnings.warn(UserWarning(f"Missing columns from backend: {missing_columns}"))

    return df.rename({src: dest for src, dest, _ in schema}, axis=1)
