# _*_ coding:utf-8 _*_
from common.ep_showcode import *
from common.sql_connect import *
import datetime



def lastday_sale():
    cmid = 3201
    showcodes = cmid_3201()
    source_id = showcodes[1]
    item_cat1_ignores = showcodes[2]
    days_delay = showcodes[3]
    sql = "select sum(total_sale) from public.cost_%s where date='2018-05-01' and cmid=%s and foreign_category_lv1" \
          " not in %s" % (source_id, cmid, item_cat1_ignores)
    print(sql)
    data_info = sql_redshift(sql)
    print('企业%s的上日销售额为：%s' % (cmid, data_info))


lastday_sale()