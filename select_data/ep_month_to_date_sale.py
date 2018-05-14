# -*- coding:utf-8 -*-
from cmdata.common.sql_connect import sql_redshift

# 企业月至今销售额
def ep_month_to_date_sale(cmid, source_id, item_cat1_ignores, days_delay):

    cmid = cmid
    source_id = source_id
    item_cat1_ignores = item_cat1_ignores
    days_delay = days_delay
    sql = "select sum(total_sale) from public.cost_%s where date BETWEEN '2018-05-01' and getdate()::date-%s and cmid=%s and foreign_category_lv1" \
          " not in %s" % (source_id, days_delay, cmid, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info