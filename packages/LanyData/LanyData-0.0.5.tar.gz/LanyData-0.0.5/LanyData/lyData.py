import pandas
from pandas import DataFrame
from data_source.arctic_data.future_data import arc_futures
from data_source.arctic_data.option_data import arc_options


class LanyData:
    def __init__(self,
                 url:str) -> None:
        s3_url = f's3://{url}:20080:research?access=lany&secret=ly@123456&region=cn-north-1'
        self._arc_future = arc_futures(s3_url)
        self._arc_option = arc_options(s3_url)


    def load_options_daily_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns:list=[]) -> DataFrame:
        return self._arc_option.load_options_daily_data(market, start, end, columns)


    def load_options_minute_data(self, market:str, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        return self._arc_option.load_options_minute_data(market, start, end, columns)


    def load_options_tick_data(self, market:str, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        return self._arc_option.load_options_daily_data(market, start, end, columns)


    def load_futures_daily_data(self, contract:str|list, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        if type(contract) == list:
            data = self._arc_future.load_futures_daily_data_batch(contract, start, end, columns)
        else:
            data = self._arc_future.load_futures_daily_data(contract, start, end, columns)
        return data


    def load_futures_daily_all_contracts_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        return self._arc_future.load_futures_daily_all_contracts_data(market, start, end, columns)
    

    def load_futures_daily_active_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        return self._arc_future.load_futures_daily_active_data(market, start, end, columns)

    
    def load_futures_minute_data(self, contract:str|list, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        if type(contract) == list:
            data = self._arc_future.load_futures_minute_data_batch(contract, start, end, columns)
        else:
            data = self._arc_future.load_futures_minute_data(contract, start, end, columns, trade_date)
        return data


    def load_futures_minute_active_data(self, market, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        return self._arc_future.load_futures_minute_active_data(market, start, end, columns, trade_date)


    def load_futures_tick_data(self, contract, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[]):
        return self._arc_future.load_futures_tick_data(contract, start, end, columns)


    def load_futures_tick_active_data(self, market, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[]):
        return self._arc_future.load_futures_tick_active_data(market, start, end, columns)

# lyData = LanyData