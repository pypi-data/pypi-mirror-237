# -*- coding: utf-8 -*-

import arcticdb
import pandas as pd
import numpy as np

from arcticdb import Arctic, QueryBuilder
from pandas import DataFrame, Series

cmd_minDate_dict={
    'A'	: '2003-12-11',
    'AG': '2012-05-10',
    'AL': '2005-01-07',
    'AU': '2008-01-09',
    'BU': '2016-01-01',#'2013-10-09',
    'C'	: '2004-09-22',
    'CF': '2005-12-02',
    'CS': '2014-12-19',
    'CU': '2007-01-07',
    'FG': '2012-12-03',
    'HC': '2014-03-21',
    'I'	: '2013-10-18',
    'IC': '2015-04-16',
    'IF': '2010-04-16',
    'IH': '2015-04-16',
    'J'	: '2011-04-15',
    'JD': '2013-11-08',
    'JM': '2013-03-22',
    'L'	: '2007-07-31',
    'M'	: '2003-12-11',
    'MA': '2014-06-17',
    'NI': '2015-03-27',
    'OI': '2013-01-04',
    'P': '2008-10-29',
    'PB': '2011-03-24',
    'PP': '2014-02-28',
    'RB': '2009-03-27',
    'RM': '2012-12-28',
    'RU': '2003-01-07',
    'SN': '2015-03-27',
    'SR': '2006-01-06',
    'T'	: '2015-03-20',
    'TA': '2006-12-18',
    'TF': '2013-09-06',
    'V'	: '2009-05-25',
    'WH': '2012-11-01',
    'Y'	: '2006-01-09',
    'ZN': '2007-03-26',
    'ZC': '2015-09-28',
    'SF': '2017-02-21',
    'SM': '2016-05-04',
    'AP': '2017-12-22',
    'SC': '2018-03-26',
    'FU': '2018-07-16',
    'CY': '2018-10-09',
    'B': '2017-06-01',
    'EG': '2018-12-15',
    'SP': '2018-12-15',
    'SS': '2019-09-25',
    'PG': '2020-03-30',
    'NR': '2019-08-12',
    'EB': '2019-09-26',
    'UR': '2019-08-09',
    'SA': '2019-12-06',
    'CJ': '2019-04-30',
    'LU': '2020-06-22',
    'PF': '2020-10-12',
    'LH': '2021-01-08'
}


def _tz_convert(date, timezone):
    date = pd.to_datetime(date)
    if date.tzinfo is None:
        date = date.tz_localize(timezone)
    else:
        date = date.tz_convert(timezone)
    return date


def _set_trade_date(data, dailyData):
    tradeDates = pd.Series(pd.to_datetime(dailyData.index.date), index=pd.to_datetime(dailyData.index.date)+pd.to_timedelta('18:00:00')) # Trade date cutoff time as 18:00
    data['trade_date'] = tradeDates.reindex(data.index, method='bfill')
    return data


class ArcticFutures(object):


    def __init__(self, url:str):
        s3_url = f's3://{url}:20080:research?access=lany&secret=ly@123456&region=cn-north-1'
        self._arc = Arctic(s3_url)


    def get_list_symbols(self, lib_name):
        return sorted(self._arc[lib_name].list_symbols())
    

    def load_futures_daily_data(self, symbol, start_date='2000-01-01', end_date='2100-01-01', columns=[]) -> DataFrame:
        columns_map = {'SETTLE_PX': 'settle', 'OPEN_INTEREST': 'open_int', 'TICKER': 'contract_id', 'HIGH_PX': 'high',
                     'MATURITY_DATE': 'maturity_date', 'LOW_PX': 'low', 'VOLUME': 'volume', 'MARKET': 'market',
                     'OPEN_PX':'open', 'TURNOVER': 'turnover', 'CLOSE_PX': 'close', 'INSTRUMENT_ID': 'instrument_id'}
        columns_reverse_map = {'settle': 'SETTLE_PX', 'open_int': 'OPEN_INTEREST', 'contract_id': 'TICKER',
                               'high': 'HIGH_PX', 'maturity_date': 'MATURITY_DATE', 'low': 'LOW_PX', 'volume': 'VOLUME',
                               'market': 'MARKET', 'open': 'OPEN_PX', 'turnover': 'TURNOVER', 'close': 'CLOSE_PX',
                               'instrument_id': 'INSTRUMENT_ID'}

        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date)) 
        if self._arc['future_daily'].has_symbol(symbol):
            if len(columns) > 0:
                columns = [columns_reverse_map[col] for col in columns]
                data = self._arc['future_daily'].read(symbol=symbol, date_range=date_range, columns=columns).data
            else:
                data = self._arc['future_daily'].read(symbol=symbol, date_range=date_range).data
            columns_to_convert = [col for col in data.columns if col in columns_map.keys()]
            new_columns = [columns_map[col] for col in data.columns if col in columns_map.keys()]
            data.rename(columns=dict(zip(columns_to_convert, new_columns)), inplace=True)
        else:
            data = DataFrame()
        return data


    def load_futures_daily_data_batch(self, symbols:list, start_date='2000-01-01', end_date='2100-01-01', columns=[]) -> DataFrame:
        columns_map = {'SETTLE_PX': 'settle', 'OPEN_INTEREST': 'open_int', 'TICKER': 'contract_id', 'HIGH_PX': 'high',
                     'MATURITY_DATE': 'maturity_date', 'LOW_PX': 'low', 'VOLUME': 'volume', 'MARKET': 'market',
                     'OPEN_PX':'open', 'TURNOVER': 'turnover', 'CLOSE_PX': 'close', 'INSTRUMENT_ID': 'instrument_id'}
        columns_reverse_map = {'settle': 'SETTLE_PX', 'open_int': 'OPEN_INTEREST', 'contract_id': 'TICKER',
                               'high': 'HIGH_PX', 'maturity_date': 'MATURITY_DATE', 'low': 'LOW_PX', 'volume': 'VOLUME',
                               'market': 'MARKET', 'open': 'OPEN_PX', 'turnover': 'TURNOVER', 'close': 'CLOSE_PX',
                               'instrument_id': 'INSTRUMENT_ID'}
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date)) 

        q = QueryBuilder()
        q = q.date_range(date_range)

        data = DataFrame()
        vi_list = self._arc['future_daily'].read_batch(symbols=symbols, query_builder=q)
        data = pd.concat([vi.data for vi in vi_list], axis=0)
        if data.empty:
            return DataFrame()
        if len(columns > 0):
            columns = [columns_reverse_map[col] for col in columns]
            data = data[columns]
        columns_to_convert = [col for col in data.columns if col in columns_map.keys()]
        new_columns = [columns_map[col] for col in data.columns if col in columns_map.keys()]
        data.rename(columns=dict(zip(columns_to_convert, new_columns)), inplace=True)

        return data


    def load_futures_daily_all_contracts_data(self, symbol, start_date='2000-01-01', end_date='2100-01-01', columns=[]) -> DataFrame:
        symbol_list = sorted([sy for sy in self._arc['future_daily'].list_symbols() if sy.find(symbol) != -1])
        data = self.load_futures_daily_data_batch(symbol_list, start_date, end_date, columns)
        return data
    

    def load_futures_daily_active_data(self, market, start_date='2000-01-01', end_date='2100-01-01', columns=[]) -> DataFrame:
        columns_map = {'SETTLE_PX': 'settle', 'OPEN_INTEREST': 'open_int', 'TICKER': 'contract_id', 'HIGH_PX': 'high',
                       'MATURITY_DATE': 'maturity_date', 'LOW_PX': 'low', 'VOLUME': 'volume', 'MARKET': 'market',
                       'OPEN_PX': 'open', 'TURNOVER': 'turnover', 'CLOSE_PX': 'close', 'INSTRUMENT_ID': 'instrument_id',
                       'PRICE_DELTA': 'px_delta', 'PRICE_RETURN': 'return', 'ROLLOVER_DELTA': 'rollover_delta',
                       'FPV': 'fpv'}
        columns_reverse_map = {'settle': 'SETTLE_PX', 'open_int': 'OPEN_INTEREST', 'contract_id': 'TICKER',
                               'high': 'HIGH_PX', 'maturity_date': 'MATURITY_DATE', 'low': 'LOW_PX', 'volume': 'VOLUME',
                               'market': 'MARKET', 'open': 'OPEN_PX', 'turnover': 'TURNOVER', 'close': 'CLOSE_PX',
                               'instrument_id': 'INSTRUMENT_ID', 'px_delta': 'PRICE_DELTA', 'return': 'PRICE_RETURN', 
                               'rollover_delta': 'ROLLOVER_DELTA', 'fpv': 'FPV'}
        
        if market in cmd_minDate_dict.keys():
            start_date = max(start_date, cmd_minDate_dict[market])
        if pd.to_datetime(start_date) > pd.to_datetime(end_date):
            return pd.DataFrame()
        
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date)) 

        if self._arc['future_daily_active'].has_symbol(market):
            if len(columns) > 0:
                columns = [columns_reverse_map[col] for col in columns]
                data = self._arc['future_daily_active'].read(symbol=market, date_range=date_range, columns=columns).data
            else:
                data = self._arc['future_daily_active'].read(symbol=market, date_range=date_range).data
            columns_to_convert = [col for col in data.columns if col in columns_map.keys()]
            new_columns = [columns_map[col] for col in data.columns if col in columns_map.keys()]
            data.rename(columns=dict(zip(columns_to_convert, new_columns)), inplace=True)
        else:
            data = pd.DataFrame()
        return data

    
    def load_futures_minute_data(self, symbol, start_date='2000-01-01 09:00:00', end_date='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        columns_reverse_map = {'volume': 'volumn'}
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date))
        if self._arc['future_minute'].has_symbol(symbol):
            if len(columns) > 0:
                columns = [col if col not in columns_reverse_map.keys() else columns_reverse_map[col] for col in columns]
                if 'end_time' not in columns:
                    columns = columns + ['end_time']
                data = self._arc['future_minute'].read(symbol=symbol, date_range=date_range, columns=columns).data
            else:
                data = self._arc['future_minute'].read(symbol=symbol, date_range=date_range).data
        else:
            data = pd.DataFrame()

        #fix a name issue in columns
        if 'volumn' in data.columns:
            data.rename(columns={'volumn': 'volume'}, inplace=True)

        if not data.empty:
            data.loc[:, 'end_time'] = pd.to_datetime(data.end_time)
            data.loc[:, 'start_time'] = pd.to_datetime(data.index)
            data.rename(columns={'end_time': 'date_time'}, inplace=True)
            data.set_index('date_time', inplace=True)

            if trade_date:
                dailyData = self.load_futures_daily_data(symbol, start_date, end_date)
                if not dailyData.empty:
                    _set_trade_date(data, dailyData)
        else:
            data = pd.DataFrame()
        return data
    

    def load_futures_minute_data_batch(self, symbols, start_date='2000-01-01 09:00:00', end_date='2100-01-01 09:00:00', columns=[]) -> DataFrame:
        columns_reverse_map = {'volume': 'volumn'}
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date)) 

        q = QueryBuilder()
        q = q.date_range(date_range)
        data = DataFrame()
        vi_list = self._arc['future_minute'].read_batch(symbols=symbols, query_builder=q)
        data = pd.concat([vi.data for vi in vi_list], axis=0)

        if data.empty:
            return DataFrame()
        if len(columns > 0):
            if 'end_time' not in columns:
                columns = columns + ['end_time']
            columns = [columns_reverse_map[col] for col in columns]
            data = data[columns]
        
        if 'volumn' in data.columns:
            data.rename(columns={'volumn': 'volume'}, inplace=True)


        data.loc[:, 'end_time'] = pd.to_datetime(data.end_time)
        data.loc[:, 'start_time'] = pd.to_datetime(data.index)
        data.rename(columns={'end_time': 'date_time'}, inplace=True)
        data.set_index('date_time', inplace=True)

        return data



    def load_futures_minute_active_data(self, market, start_date='2000-01-01 09:00:00', end_date='2100-01-01 09:00:00', columns=[], trade_date=False) -> DataFrame:
        if market in cmd_minDate_dict.keys():
            start_date = max(start_date, cmd_minDate_dict[market])

        active_range = self.get_active_range(market, start_date, end_date)
        data = pd.concat([self.load_futures_minute_data(row[0], row[1].start_time, row[1].end_time, columns=columns, trade_date=trade_date)
                          for row in active_range.iterrows()])
        return data


    def load_futures_tick_data(self, symbol, start_date='2000-01-01 09:00:00', end_date='2100-01-01 09:00:00', columns=[]):
        date_range = (pd.to_datetime(start_date), pd.to_datetime(end_date))
        if symbol in self._arc['future_tick_chunk'].list_symbols():
            if len(columns) > 0:
                data = self._arc['future_tick_chunk'].read(symbol=symbol, date_range=date_range, columns=columns).data
            else:
                data = self._arc['future_tick_chunk'].read(symbol=symbol, date_range=date_range).data
        else:
            data = pd.DataFrame()

        if not data.empty:
            data['end_time'] = data.index
            data.loc[:, 'end_time'] = pd.to_datetime(data.end_time)
            data.rename(columns={'end_time': 'date_time'}, inplace=True)
            data.set_index('date_time', inplace=True)
        return data


    def load_futures_tick_active_data(self, market, start_date='2000-01-01 09:00:00', end_date='2100-01-01 09:00:00', columns=[]):
        if market in cmd_minDate_dict.keys():
            start_date = max(start_date, cmd_minDate_dict[market])

        active_range = self.get_active_range(market, start_date, end_date)
        data = pd.concat([self.load_futures_tick_data(row[0], row[1].start_time, row[1].end_time, columns=columns)
                          for row in active_range.iterrows()])
        return data


    def get_active_range(self, market, start_date, end_date):
        if market in cmd_minDate_dict.keys():
            start_date = max(start_date, cmd_minDate_dict[market])

        start_adj = (pd.to_datetime(start_date) + pd.to_timedelta(-10, 'D')).strftime('%Y-%m-%d')
        date_range = (pd.to_datetime(start_adj), pd.to_datetime(end_date))
        daily_range = self._arc['future_daily_active'].read(market, date_range, columns=['TICKER', 'ROLLOVER_TICKER'])
        daily_range.index.name = 'date'
        daily_range = daily_range.reset_index()
        daily_range['prev_date'] = daily_range['date'].shift(1)
        if pd.isnull(daily_range.loc[0, 'prev_date']):
            daily_range.loc[0, 'prev_date'] = pd.to_datetime(start_date) + pd.to_timedelta(-1, 'D')
        daily_range['start_time'] = daily_range.prev_date + pd.to_timedelta(16, 'h')
        daily_range['end_time'] = daily_range.date + pd.to_timedelta(16, 'h')
        daily_range = daily_range[daily_range.date >= start_date]

        if daily_range.end_time.iloc[-1] < pd.to_datetime(end_date):
            if not pd.isnull(daily_range.ROLLOVER_TICKER.iloc[-1]):
                daily_range.loc[daily_range.index[-1], 'end_time'] = daily_range.loc[daily_range.index[-1], 'end_time'] + pd.to_timedelta(12, 'H')
            else:
                new_row = pd.Series({'date': daily_range.date.iloc[-1] + pd.to_timedelta(1, 'D'),
                                     'TICKER': daily_range.ROLLOVER_TICKER.iloc[-1],
                                     'ROLLOVER_TICKER': None,
                                     'prev_date': daily_range.date.iloc[-1],
                                     'start_time': daily_range.end_time.iloc[-1],
                                     'end_time': daily_range.end_time.iloc[-1] + pd.to_timedelta(12, 'H'),
                                     })
                daily_range = daily_range.append(new_row, ignore_index=True)

        daily_range['start_time'] = daily_range.start_time.clip(pd.to_datetime(start_date), pd.to_datetime(end_date))
        daily_range['end_time'] = daily_range.end_time.clip(pd.to_datetime(start_date), pd.to_datetime(end_date))
        active_range = daily_range.groupby('TICKER').agg({'start_time': min, 'end_time': max})
        return active_range
    
arc_futures = ArcticFutures