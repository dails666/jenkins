# -*- coding:utf-8 -*-
from cmdata.common.sql_connect import sql_redshift


# 查询企业上日毛利额
def lastday_margin(cmid, source_id, item_cat1_ignores, days_delay):
    sql = "select sum(total_sale-total_cost) from public.cost_%s where date=getdate()::date-%s and cmid=%s and foreign_category_lv1" \
          " not in %s" % (source_id, days_delay, cmid, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info