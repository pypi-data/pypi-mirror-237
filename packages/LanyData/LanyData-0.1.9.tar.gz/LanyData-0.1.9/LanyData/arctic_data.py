import pandas
from pandas import DataFrame
from .future_data import ArcticFutures
from .option_data import ArcticOptions

class ArcticData:
    def __init__(self,
                 url:str) -> None:
        self._arc_future = ArcticFutures(url)
        self._arc_option = ArcticOptions(url)

    def get_options_symbols(self, freq='tick')  -> list:
        """获取期权品种列表
        ### Parameters:
        freq: 频率, 可取'tick', 'minute', 'daily'
        ### Returns:
        返回期权品种列表
        """
        if freq == 'tick':
            return self._arc_option.list_tick_symbols()
        elif freq == 'minute':
            return self._arc_option.list_minute_symbols()
        elif freq == 'daily':
            return self._arc_option.list_daily_symbols()


    def load_options_daily_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns:list=[]) -> DataFrame:
        """期权日频数据
        ### Parameters:
        market: 期权品种, 从get_options_symbols获取\n
        start: 起始时间, 如'2000-01-01'\n
        end: 结束时间, 如'2023-12-31'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期权日频数据
        """
        return self._arc_option.load_options_daily_data(market, start, end, columns)


    def load_options_minute_data(self, market:str, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        """期权分钟数据
        ### Parameters:
        market: 期权品种, 从get_options_symbols获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期权分钟数据
        """
        return self._arc_option.load_options_minute_data(market, start, end, columns)


    def load_options_tick_data(self, market:str, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 15:00:00', columns=[]) -> DataFrame:
        """期权tick数据
        ### Parameters:
        market: 期权品种, 从get_options_symbols获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期权tick数据
        """
        return self._arc_option.load_options_tick_data(market, start, end, columns)


    def get_futures_symbols(self, freq='tick')  -> list:
        """获取期货合约列表
        ### Parameters:
        freq: 频率, 可取'tick', 'minute', 'daily'
        ### Returns:
        返回期货合约列表
        """
        if freq == 'tick':
            return self._arc_future.list_tick_symbols()
        elif freq == 'minute':
            return self._arc_option.list_minute_symbols()
        elif freq == 'daily':
            return self._arc_option.list_daily_symbols()
        

    def get_futures_markets(self) -> list:
        """获取期货品种列表
        ### Returns:
        返回期货品种列表
        """
        return self._arc_future.list_markets()


    def load_futures_daily_data(self, contract:str|list, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        """期货日频数据
        ### Parameters:
        contract: 期货合约ID, 从get_futures_symbols获取\n
        start: 起始时间, 如'2000-01-01'\n
        end: 结束时间, 如'2023-12-31'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期货日频数据
        """
        if type(contract) == list:
            data = self._arc_future.load_futures_daily_data_batch(contract, start, end, columns)
        else:
            data = self._arc_future.load_futures_daily_data(contract, start, end, columns)
        return data


    def load_futures_daily_all_contracts_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        """期货日频数据
        ### Parameters:
        market: 期货品种, 从get_futures_markets获取\n
        start: 起始时间, 如'2000-01-01'\n
        end: 结束时间, 如'2023-12-31'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期货日频数据
        """
        return self._arc_future.load_futures_daily_all_contracts_data(market, start, end, columns)
    

    def load_futures_daily_active_data(self, market:str, start:str|pandas.Timestamp='2000-01-01', end:str|pandas.Timestamp='2100-01-01', columns=[]) -> DataFrame:
        """期货主力日频数据
        ### Parameters:
        market: 期货品种, 从get_futures_markets获取\n
        start: 起始时间, 如'2000-01-01'\n
        end: 结束时间, 如'2023-12-31'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期货主力日频数据
        """
        return self._arc_future.load_futures_daily_active_data(market, start, end, columns)

    
    def load_futures_minute_data(self, contract:str|list, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        """期货分钟数据
        ### Parameters:
        contract: 期货合约ID, 从get_futures_symbols获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名\n
        trade_date: 是否根据交易日ReIndex
        ### Returns:
        以DataFrame形式返回期货分钟数据
        """
        if type(contract) == list:
            data = self._arc_future.load_futures_minute_data_batch(contract, start, end, columns)
        else:
            data = self._arc_future.load_futures_minute_data(contract, start, end, columns, trade_date)
        return data


    def load_futures_minute_active_data(self, market, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        """期货主力分钟数据
        ### Parameters:
        market: 期货品种, 从get_futures_markets获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名\n
        trade_date: 是否根据交易日ReIndex
        ### Returns:
        以DataFrame形式返回期货主力分钟数据
        """
        return self._arc_future.load_futures_minute_active_data(market, start, end, columns, trade_date)


    def load_futures_tick_data(self, contract, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[]):
        """期货tick数据
        ### Parameters:
        contract: 期货合约ID, 从get_futures_symbols获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期货tick数据
        """
        return self._arc_future.load_futures_tick_data(contract, start, end, columns)


    def load_futures_tick_active_data(self, market, start:str|pandas.Timestamp='2000-01-01 09:00:00', end:str|pandas.Timestamp='2100-01-01 09:00:00', columns=[]):
        """期货主力tick数据
        ### Parameters:
        market: 期货品种, 从get_futures_markets获取\n
        start: 起始时间, 如'2000-01-01 09:00:00'\n
        end: 结束时间, 如'2023-12-31 18:00:00'\n
        columns: 列名
        ### Returns:
        以DataFrame形式返回期货主力tick数据
        """
        return self._arc_future.load_futures_tick_active_data(market, start, end, columns)