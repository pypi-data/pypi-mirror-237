# -*- coding: utf-8 -*-

from hbshare.fe.xwq.analysis.orm.hbdb import HBDB
from datetime import datetime
import os
import numpy as np
import pandas as pd

from WindPy import w
w.start()  # 默认命令超时时间为120秒，如需设置超时时间可以加入waitTime参数，例如waitTime=60,即设置命令超时时间为60秒
w.isconnected()  # 判断WindPy是否已经登录成功

class IndustryFinanceData:
    def __init__(self, industry_name, start_date, end_date, report_date, data_path):
        self.industry_name = industry_name
        self.start_date = start_date
        self.end_date = end_date
        self.report_date = report_date
        self.data_path = data_path
        self.industry_universe = pd.read_excel('{0}{1}/{2}_信息.xlsx'.format(self.data_path, self.industry_name, self.industry_name), sheet_name='股票池-v2')
        self.industry_universe.columns = ['TICKER_SYMBOL_EXCHANGE', 'SEC_SHORT_NAME']
        self.industry_universe['TICKER_SYMBOL_EXCHANGE'] = self.industry_universe['TICKER_SYMBOL_EXCHANGE'].astype(str)
        self.industry_universe['SEC_SHORT_NAME'] = self.industry_universe['SEC_SHORT_NAME'].astype(str)
        self.industry_universe['TICKER_SYMBOL'] = self.industry_universe['TICKER_SYMBOL_EXCHANGE'].apply(lambda x: x.split('.')[0])
        self.industry_universe['EXCHANGE'] = self.industry_universe['TICKER_SYMBOL_EXCHANGE'].apply(lambda x: x.split('.')[1])
        self.industry_universe['IDX'] = range(len(self.industry_universe))
        self.industry_universe_A = self.industry_universe[~self.industry_universe['EXCHANGE'].isin(['HK', 'hk'])]
        self.industry_universe_HK = self.industry_universe[self.industry_universe['EXCHANGE'].isin(['HK', 'hk'])]
        self.industry_universe_HK['TICKER_SYMBOL'] = self.industry_universe_HK['TICKER_SYMBOL'].apply(lambda x: x + '.HK')
        self.industry_universe = pd.concat([self.industry_universe_A, self.industry_universe_HK])
        self.industry_universe = self.industry_universe.sort_values('IDX').drop(['IDX', 'EXCHANGE'], axis=1)

    def get_all(self):
        """
        行业集中度（季度）：基于营业收入TTM计算的行业HHI
        资产负债率（季度）：负债TTM / 总资产TTM
        产业链内部杠杆（季度）：（应付增加+ 应收减少） / 营收，TTM
        营收增速（季度）：季度营业收入TTM同比增长率
        盈利增速（季度）：相对全A的归母净利润同比增速
        资本开支增速（季度）：资本开支的同比增长率
        CAPEX / DA（季度）：现金流量表中资本开支 / 折旧摊销，TTM
        研发增速（季度）： 研发费用的同比增速
        研发投入占比（年度）：研发投入 / 营业收入
        净利率（年度，季度）：归母净利润 / 营业收入
        毛利率变动（季度）：毛利率TTM（t)-毛利率TTM（t - 4）
        经营现金流（年度）：行业：用近三年的现金流均值，展示每年滚动数据，个股：用当年的数据
        投资现金流（年度）：行业：用近三年的现金流均值，展示每年滚动数据，个股：用当年的数据
        融资现金流（年度）：行业：用近三年的现金流均值，展示每年滚动数据，个股：用当年的数据
        """
        return


if __name__ == '__main__':
    industry_name = '动力电池'
    start_date = '20190101'
    end_date = '20230908'
    report_date = '20230630'
    data_path = 'D:/Git/hbshare/hbshare/fe/xwq/data/industry_overview/'
    IndustryFinanceData(industry_name, start_date, end_date, report_date, data_path).get_all()