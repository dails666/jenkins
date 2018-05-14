# -*- coding: utf-8 -*-
from cmdata.select_data import ep_lastday_margin
from cmdata.common import unit
from cmdata.api import get_enterprise_detail
from cmdata.common.ep_showcode import *
import re

class TestLastdayMargin(unit.Unit):

    # 查询企业上日毛利额
    def test_ep_lastday_margin(self):
        cmids = {'3201': cmid_3201(), '34': cmid_34(), '43': cmid_43(), '48': cmid_48(), '49': cmid_49()}
        try:
            for cmid, ep_info in cmids.items():
                source_id = ep_info[1]
                item_cat1_ignores = ep_info[2]
                days_delay = ep_info[3]
                token = 'token__cm_%s_user_all' % cmid
                data = '%.2f' % (ep_lastday_margin.lastday_margin(cmid, source_id, item_cat1_ignores, days_delay))
                data_sql = re.sub(r"(\d)(?=(\d\d\d)+(?!\d))", r"\1,", data) + u'元'
                data_api = get_enterprise_detail.get_enterprise_detail(token)['margin']['last_date']
                if data_sql == data_api:
                    print(u'%s上日毛利额数据正常！' % (cmid))
                else:
                    print(u'%s上日毛利额数据异常：' % (cmid)),
                    print(u'%s≠%s' % (data_sql, data_api))
        except UnicodeDecodeError:
            print(u'编码错误')
        finally:
            print(u'上日毛利额测试结束！~~~~~~~~~~~~~')