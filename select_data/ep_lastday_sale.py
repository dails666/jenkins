# -*- coding:utf-8 -*-
from cmdata.common.sql_connect import sql_redshift

def lastday_sale(cmid, source_id, item_cat1_ignores, days_delay):

    sql = "select sum(total_sale) from public.cost_%s where date=getdate()::date-%s and cmid=%s and foreign_category_lv1" \
          " not in %s" % (source_id, days_delay, cmid, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info