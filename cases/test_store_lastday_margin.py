# -*- coding:utf-8 -*-
import re
import time
from cmdata.api import get_store_detail
from cmdata.common import unit
from cmdata.common.ep_showcode import *
from cmdata.select_data import store_lastday_margin


class TestLastdayMargin(unit.Unit):

    # 单家门店上日毛利额巡检
    def test_store_lastday_margin(self):
        cmids = {'3201': cmid_3201(), '34': cmid_34(), '43': cmid_43(), '48': cmid_48(), '49': cmid_49()}
        try:
            for cmid, ep_info in cmids.items():
                source_id = ep_info[1]
                item_cat1_ignores = ep_info[2]
                days_delay = ep_info[3]

                for token, showcodes in ep_info[0].items():

                    for showcode in showcodes:

                        try:

                            response_sql = store_lastday_margin.lastday_margin(cmid, showcode, source_id, item_cat1_ignores,
                                                                           days_delay)
                            if response_sql == None:
                                continue
                            data = '%.2f' % (response_sql)
                            data_sql = re.sub(r"(\d)(?=(\d\d\d)+(?!\d))", r"\1,", data) + u'元'
                            data_api = get_store_detail.get_store_detail(showcode, token)['margin']['last_date']
                            if data_sql == data_api:
                                continue
                            else:
                                print(u'%s：门店%s数据异常：%s≠%s' % (ep_info[4], showcode, data_sql, data_api))

                        except IndexError:
                            print(u'%s：门店%s不存在！' % (ep_info[4], showcode))
                            continue
                        except KeyError:
                            continue
                        time.sleep(2)
                    time.sleep(2)
                time.sleep(3)
        except UnicodeDecodeError:
            print(u'编码错误')

        except ValueError:
            print(u'无法解码JSON对象')