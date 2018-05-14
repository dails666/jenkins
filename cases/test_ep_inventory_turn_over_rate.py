# _*_coding:utf-8_*_
from cmdata.common import unit
from cmdata.common.ep_showcode import *
from cmdata.common.sql_connect import sql_redshift

class TestInventoryTurnOverRate(unit.Unit):
    
    # 查询企业月至今库存周转天数
    def test_ep_inventory_turn_over_rate(self):
        pass