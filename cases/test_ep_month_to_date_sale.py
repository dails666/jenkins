# -*- coding:utf-8 -*-
from cmdata.common import unit
from cmdata.common.ep_showcode import *
from cmdata.select_data import ep_month_to_date_sale
from cmdata.api import get_enterprise_detail
import re

class TestMonthToDate(unit.Unit):

    # 企业月至今销售额巡检
    def test_ep_month_to_date_sale(self):
        cmids = {'3201': cmid_3201(), '34': cmid_34(), '43': cmid_43(), '48': cmid_48(), '49': cmid_49()}
        try:
            for cmid, ep_info in cmids.items():
                token = 'token__cm_%s_user_all' % cmid
                source_id = ep_info[1]
                item_cat1_ignores = ep_info[2]
                days_delay = ep_info[3]
                data = '%.2f' % (ep_month_to_date_sale.ep_month_to_date_sale(cmid, source_id, item_cat1_ignores, days_delay))
                data_sql = re.sub(r"(\d)(?=(\d\d\d)+(?!\d))", r"\1,", data) + u'元'
                data_api = get_enterprise_detail.get_enterprise_detail(token)['sales']['month_to_date']
                if data_sql == data_api:
                    print(u'%s月至今销售额数据正常！' % (cmid))
                else:
                    print(u'%s月至今销售额数据异常：' % (cmid)),
                    print(u'%s≠%s' % (data_sql, data_api))
        except UnicodeDecodeError:
            print(u'编码错误')
