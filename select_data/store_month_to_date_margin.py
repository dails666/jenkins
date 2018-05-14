# -*- coding:utf-8 -*-
from cmdata.common.sql_connect import sql_redshift


# 查询单家门店月至今毛利额：
def lastday_margin(cmid, store_id, source_id, item_cat1_ignores, days_delay):

    sql = "select sum(total_sale-total_cost) from public.cost_%s where date between '2018-05-01' and getdate()::date-%s " \
          "and cmid=%s and foreign_store_id=%s and foreign_category_lv1 not in %s" % (source_id, days_delay, cmid,
                                                                                      store_id, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info