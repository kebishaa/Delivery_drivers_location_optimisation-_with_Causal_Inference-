import unittest
import pandas as pd
import sys
import os
from datetime import datetime
cwd = os.getcwd()
sys.path.append(f'{cwd}/scripts')
from data_cleaner import DataCleaner 
cleaner = DataCleaner()
class TestCleaner(unittest.TestCase):
    def test_remove_col_space(self):
        test_df=pd.DataFrame(columns=["col one","col_two"])
        test_df_cols=list(test_df.columns.values)
        new_cols=list(cleaner.remove_space(test_df).columns.values)
        self.assertFalse(test_df_cols == new_cols)
    