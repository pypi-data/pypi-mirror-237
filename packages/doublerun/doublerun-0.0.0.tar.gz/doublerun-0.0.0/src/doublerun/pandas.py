from typing import Tuple
import pandas as pd

def mismatch_report(df1: pd.DataFrame, df2: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Function that identifies the rows which are not common between two input DataFrames.

    Args:
        df1, df2 : pd.DataFrame
            Input DataFrames to compare.

    Returns:
        left_diff : pd.DataFrame
            Rows from df1 that are not in df2.
        right_diff : pd.DataFrame
            Rows from df2 that are not in df1.
        common : pd.DataFrame
            Rows from df1 and df2 that are identical.

    Author : Pierre Adeikalam (pierre.adeikalam@axa-direct.com)
    """

    merged_df = df1.merge(df2, indicator=True, how='outer')

    left_diff  = merged_df[merged_df['_merge'] == 'left_only'].drop("_merge", axis=1).reset_index(drop = True)
    right_diff = merged_df[merged_df['_merge'] == 'right_only'].drop("_merge", axis=1).reset_index(drop = True)
    common     = merged_df[merged_df['_merge'] == 'both'].drop("_merge", axis=1).reset_index(drop = True)

    return left_diff, right_diff, common
