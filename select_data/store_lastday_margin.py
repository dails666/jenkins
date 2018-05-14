# -*- coding:utf-8 -*-
from cmdata.common.sql_connect import sql_redshift, sql_chain_store


# 查询单家门店上日毛利额：
def lastday_margin(cmid, showcode, source_id, item_cat1_ignores, days_delay):

    # 将showcode传递给sql_chain_store方法进行处理，得到foreign_store_id
    store_id = sql_chain_store(cmid, showcode)
    sql = "select sum(total_sale-total_cost) from public.cost_%s where date=getdate()::date-%s and cmid=%s and foreign_store_id=%s" \
          "and foreign_category_lv1 not in %s" % (source_id, days_delay, cmid, store_id, item_cat1_ignores)

    return sql_redshift(sql)