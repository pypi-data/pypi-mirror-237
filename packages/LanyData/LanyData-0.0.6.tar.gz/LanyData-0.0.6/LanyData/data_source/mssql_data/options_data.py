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


class MSSQLOptions(object):
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

    def load_options_market_info(self):
        """
        This function loads the futures market information such as contract size, tick size, exchange fee, broker fee, margin. Use table FUTURES_CONTRACTS only.

        Returns:
        dataframe
        """
        query = """
            SELECT RTRIM(I.TICKER) AS TICKER, C.CONTRACT_SIZE, C.TICK_SIZE, C. EXCHANGE_FEE, C.BROKER_FEE, C.MARGIN_RATE, M.* 
            FROM [MARKET].[dbo].[OPTIONS_CONTRACTS] C,[MARKET].[dbo].INSTRUMENTS I,[MARKET].[dbo].MARKETS M 
            WHERE C.UNDERLYING_ID=I.ID AND I.MARKET_ID=M.ID
            ORDER BY TICKER
            """
        costs_df = self._read_data_db(query, self._sql_daily)
        if costs_df is None:
            print('cannot query costs df from DB, load from local')
            with open('costs_df_options.pkl', 'rb') as f:
                costs_df = pickle.load(f)
                costs_df.reset_index(inplace=True)

        costs_df.set_index('TICKER', inplace=True)
        code_map = {'IF': '000300', 'IH': '000016', 'IC': '000905'}
        for mkt in code_map.keys():
            if mkt in costs_df.index:
                costs_df.loc[mkt, :] = costs_df.loc[code_map[mkt], :]
                #costs_df.loc[mkt, 'BROKER_FEE_RATE'] = 0.00005

        with open('costs_df_options.pkl', 'wb') as f:
            pickle.dump(costs_df, f)

        return costs_df

    def load_options_daily_all_contracts_data(self, st=None, ed=None, cmd=None, volume_threshold=100):
        query = "SELECT TRADE_DATE as date_time, MATURITY_DATE as maturity_date, TICKER as contract, UNDERLYING_TICKER as underlying_contract, " \
                "CONTRACT_UNDERLYING_TICKER as market, PUT_CALL as put_call, CLOSE_PX as 'close', VOLUME as volume, DELTA as delta, IMPLIED_VOL as implied_vol, STRIKE as strike " \
                "FROM GET_OPTIONS_PRICES('{0}', '{1}', '{2}')" \
                "WHERE VOLUME>{3} order by date_time, contract".format(cmd, st, ed, volume_threshold)
        data_df = self._read_data_db(query, db_config=self._sql_daily)

        return data_df
