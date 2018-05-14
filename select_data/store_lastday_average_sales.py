# _*_coding:utf-8_*_
from cmdata.common import unit
from cmdata.common.ep_showcode import *
from cmdata.common.sql_connect import sql_redshift


class TestLastdayAverageSales(unit.Unit):

    # 查询单家门店上日客单价
    def test_store_lastday_average_sales(self):
        pass