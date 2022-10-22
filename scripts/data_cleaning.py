import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer, MinMaxScaler, StandardScaler


class DataCleaner:
    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df
    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """

        df[['start','end']] = df[['start','end']].apply(pd.to_datetime)

        return df 
    def convert_to_string(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert columns to string
        """
        df[['bearer_id', 'imsi', 'msisdn/number', 'imei','handset_type']] = df[['bearer_id', 'imsi', 'msisdn/number', 'imei','handset_type']].astype(str)

        return df
    def remove_whitespace_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        remove whitespace from columns
        """
        df.columns = [column.replace(' ', '_').lower() for column in df.columns]

        return df
 