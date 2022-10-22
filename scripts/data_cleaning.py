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
    def percent_missing(self, df: pd.DataFrame) -> float:
        """
        calculate the percentage of missing values from dataframe
        """
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMising = missingCount.sum()

        return round(totalMising / totalCells * 100, 2)
    def get_numerical_columns(self, df: pd.DataFrame) -> list:
        """
        get numerical columns
        """
        return df.select_dtypes(include=['number']).columns.to_list()
    def get_categorical_columns(self, df: pd.DataFrame) -> list:
        """
        get categorical columns
        """
        return  df.select_dtypes(include=['object','datetime64[ns]']).columns.to_list()
    def percent_missing_column(self, df: pd.DataFrame, col:str) -> float:
        """
        calculate the percentage of missing values for the specified column
        """
        try:
            col_len = len(df[col])
        except KeyError:
            print(f"{col} not found")
        missing_count = df[col].isnull().sum()

        return round(missing_count / col_len * 100, 2)
    
    def fill_missing_values_categorical(self, df: pd.DataFrame, method: str) -> pd.DataFrame:
        """
        fill missing values with specified method
        """

        categorical_columns = df.select_dtypes(include=['object','datetime64[ns]']).columns

        if method == "ffill":

            for col in categorical_columns:
                df[col] = df[col].fillna(method='ffill')

            return df

        elif method == "bfill":

            for col in categorical_columns:
                df[col] = df[col].fillna(method='bfill')

            return df

        elif method == "mode":
            
            for col in categorical_columns:
                df[col] = df[col].fillna(df[col].mode()[0])

            return df
        else:
            print("Method unknown")
            return df


 