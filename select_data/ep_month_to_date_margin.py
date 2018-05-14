# _*_coding:utf-8_*_
from cmdata.common.sql_connect import sql_redshift

# 查询企业月至今毛利额
def month_to_date_margin(cmid, source_id, item_cat1_ignores, days_delay):
    sql = "select sum(total_sale-total_cost) from public.cost_%s where date between '2018-05-01' and getdate()::date-%s and cmid=%s and foreign_category_lv1" \
          " not in %s" % (source_id, days_delay, cmid, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info