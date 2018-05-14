# _*_coding:utf-8_*_
from cmdata.common.sql_connect import sql_redshift

# 查询单家门店库存周转天数
def store_inventory_turn_over_rate(source_id, cmid, store_id, days_delay, item_cat1_ignores):

    sql = '''
            SELECT t1.amount/t2.cost*2 FROM (SELECT SUM(amount) amount FROM inventory_%s WHERE date=getdate()::date
            AND cmid=%s and foreign_store_id='%s') t1,( SELECT SUM(total_cost) cost FROM cost_%s WHERE date between
            '2018-05-01' and getdate()::date-%s AND cmid=%s and foreign_store_id='%s' and foreign_category_lv1
            not in %s) t2
    ''' % (source_id, cmid, store_id, source_id, days_delay, cmid, store_id, item_cat1_ignores)
    data_info = sql_redshift(sql)
    return data_info