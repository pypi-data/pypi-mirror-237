from doublerun.pandas import mismatch_report
import pandas as pd

def test_mismatch_report():

    df1 = pd.DataFrame({
        'Column1' : [1, 2, 3, 4],
        'Column2' : ['A', 'B', 'C', 'D']
    })

    df2 = pd.DataFrame({
        'Column1' : [1, 2, 3, 4],
        'Column2' : ['E', 'B', 'C', 'F']
    })

    expected_left_diff  = df1.iloc[[0, 3]].reset_index(drop=True)
    expected_right_diff = df2.iloc[[0, 3]].reset_index(drop=True)
    expected_common     = df1.iloc[[1, 2]].reset_index(drop=True)

    left_diff, right_diff, common = mismatch_report(df1, df2)

    pd.testing.assert_frame_equal(left_diff, expected_left_diff)
    pd.testing.assert_frame_equal(right_diff, expected_right_diff)
    pd.testing.assert_frame_equal(common, expected_common)



