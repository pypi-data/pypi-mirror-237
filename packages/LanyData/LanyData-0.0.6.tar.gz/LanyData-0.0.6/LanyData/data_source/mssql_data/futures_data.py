# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:01:45 2020

@author: zhi
"""
# coding=utf-8
import warnings

import importlib,sys
import pyodbc as ss
import pandas as pd
import logging
import pickle
import datetime as dt

import data_engine.setting as setting

importlib.reload(sys)

warnings.filterwarnings("ignore")


class MSSQLFutures(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._sql_daily = setting.DB_CONFIG_DAILY
        self._sql_minute = setting.DB_CONFIG_MINUTE

    def _read_data_db(self, query=None, db_config=None):
        try:
            conn = ss.connect(db_config)
        except:
            print("DB connection error:" + db_config)
            self._logger.warning("DB connection error: read, " + db_config)
            return None

        try:
            df = pd.read_sql(query, conn)
            return df
        except:
            print("read failed:", query)
            self._logger.warning("read failed:", query)
            return None

    def load_futures_trade_dates(self):
        """
        load the trading days
        Returns:
        data frame
        """
        query = """
            select distinct(TRADE_DATE) from dbo.DAILY_PRICES order by 1 
            """

        data = self._read_data_db(query, self._sql_daily)
        return data

    def load_futures_market_info(self):
        """
        This function loads the futures market information such as contract size, tick size, exchange fee, broker fee, margin. Use table FUTURES_CONTRACTS only.

        Returns:
        dataframe
        """
        query = """
            SELECT RTRIM(I.TICKER) AS TICKER, C.CONTRACT_SIZE, C.TICK_SIZE, C. EXCHANGE_FEE, C.EXCHANGE_FEE_RATE,C.BROKER_FEE, C.BROKER_FEE_RATE, C.MARGIN_RATE, M.* FROM [MARKET].[dbo].[FUTURES_CONTRACTS] C,[MARKET].[dbo].INSTRUMENTS I,[MARKET].[dbo].MARKETS M 
            WHERE C.UNDERLYING_ID=I.ID AND I.MARKET_ID=M.ID
            ORDER BY TICKER
            """
        try:
            costs_df = self._read_data_db(query, self._sql_daily)
        except:
            print('cannot query costs df from DB, load from local')
            with open('.\costs_df.pkl', 'rb') as f:
                costs_df = pickle.load(f)
                costs_df.reset_index(inplace=True)
            f.close()

        costs_df.set_index('TICKER', inplace=True)
        code_map = {'IF': '000300', 'IH': '000016', 'IC': '000905'}
        for mkt in code_map.keys():
            costs_df.loc[mkt, :] = costs_df.loc[code_map[mkt], :]
            #costs_df.loc[mkt, 'BROKER_FEE_RATE'] = 0.00005

        with open('costs_df.pkl', 'wb') as f:
            pickle.dump(costs_df, f)

        return costs_df

    def load_futures_daily_all_contracts_data(self, st=None, ed=None, cmd=None):
        """
        This function will get all prices of all contracts in given commodity name
        with given parameters
        st: start_date
        ed: end_date
        cmd: the market, for example CU
        exch_code: the code of exchange

        exch_code:
        - Stock futures: CFFEX
        - Shanghai: SHFE
        - Dalian: DCE
        - Zhengzhou: ZCE
        """

        code_map = {'IF': '000300', 'IH': '000016', 'IC': '000905'}
        cmd_temp = cmd
        if cmd in code_map.keys():
            cmd_temp = code_map[cmd]

        query = """ SELECT I.TICKER,P.TRADE_DATE,P.OPEN_PX,P.HIGH_PX,P.LOW_PX,P.CLOSE_PX,P.SETTLE_PX,P.VOLUME,P.OPEN_INTEREST,P.TURNOVER,F.MATURITY_DATE 
        FROM MARKET.dbo.MARKETS M,MARKET.dbo.INSTRUMENTS I,MARKET.dbo.FUTURES F,MARKET.dbo.INSTRUMENTS U,MARKET.dbo.DAILY_PRICES P 
        WHERE M.ID=I.MARKET_ID 
        ---AND M.CODE='exch_code' 
        AND I.ID=F.INSTRUMENT_ID 
        AND I.ID=P.INSTRUMENT_ID 
        AND F.UNDERLYING_ID=U.ID 
        AND U.TICKER='""" + cmd_temp + """' 
        AND P.TRADE_DATE between '""" + st + """' and '""" + ed + """'
        AND P.CLOSE_PX>0.0
        ORDER BY P.TRADE_DATE,I.TICKER  
        """

        dataAll_df = self._read_data_db(query, self._sql_daily)
        dataAll_df['TRADE_DATE'] = pd.to_datetime(dataAll_df['TRADE_DATE'])
        dataAll_df = dataAll_df.rename(columns={'TRADE_DATE': 'date_time'})
        dataAll_df.set_index('date_time', inplace=True)

        # reverse_map = {'000300': 'IF', '000016': 'IH', '000905': 'IC'}
        # mkt = cmd
        # if cmd in reverse_map.keys():
        #     mkt = reverse_map[cmd]

        return dataAll_df
