# _*_coding:utf-8_*_
from cmdata.common import unit
from cmdata.common.ep_showcode import *
from cmdata.common.sql_connect import sql_redshift

class TestInventoryTurnOverRate(unit.Unit):

    # 查询单家门店月至今库存周转天数
    def test_store_inventory_turn_over_rate(self):
        pass