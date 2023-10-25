import re
import pandas as pd
import numpy as np
import datetime

from arcticdb import Arctic, QueryBuilder
from pandas import DataFrame

class ArcticOptions():
    def __init__(self, url:str) -> None:
        s3_url = f's3://{url}:20080:research?access=lany&secret=ly@123456&region=cn-north-1'
        self._arc = Arctic(s3_url)

    def __load_data(self, lib_name, symbol, start_time=None, end_time=None, columns=[]) -> DataFrame:
        date_range = (pd.to_datetime(start_time), pd.to_datetime(end_time))        
        if self._arc[lib_name].has_symbol(symbol):
            if len(columns) > 0:
                data = self._arc[lib_name].read(symbol, columns=columns,date_range=date_range).data
            else:
                data = self._arc[lib_name].read(symbol,date_range=date_range).data
        else:
            data = DataFrame()
        return data
    
    def load_options_daily_data(self, symbol, start_date='2000-01-01', end_date='2100-01-01', columns=[]) -> DataFrame:
        return self.__load_data(lib_name='option_daily', symbol=symbol, start_time=start_date, end_time=end_date, columns=columns)


    def load_options_minute_data(self, symbol, start_date='2000-01-01 09:00:00', end_date='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        return self.__load_data(lib_name='option_minute', symbol=symbol, start_time=start_date, end_time=end_date, columns=columns)

    def load_options_tick_data(self, symbol, start_date='2000-01-01 09:00:00', end_date='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        q = QueryBuilder()
        q.optimise_for_memory()
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date))
        q = q.date_range(date_range)
        if self._arc['option_tick'].has_symbol(symbol):
            if len(columns) > 0:
                data = self._arc['option_tick'].read(symbol=symbol, columns=columns, query_builder=q)
            else:
                data = self._arc['option_tick'].read(symbol=symbol, query_builder=q)
        else:
            data = DataFrame()
        
        return data


    def list_tick_symbols(self):
        return self._arc['option_tick'].list_symbols()
    
    def list_minute_symbols(self):
        return self._arc['option_minute'].list_symbols()
    
    def list_daily_symbols(self):
        return self._arc['option_daily'].list_symbols()
    

arc_options = ArcticOptions
