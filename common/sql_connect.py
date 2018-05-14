import psycopg2

def sql_redshift(sql):

    connection = psycopg2.connect(database="cmdata_new", user="cmpm", password="#CO58131@Isx0#", host="52.80.53.182",
                                  port="5439")
    cursor = connection.cursor()
    cursor.execute(sql)
    data_info = cursor.fetchall()
    return data_info[0][0]


def sql_chain_store(cmid, showcode):
    connection = psycopg2.connect(database="cmb_chainstore", user="cmb_chainstore", password="yuSpUh_2aX!",
                                  host="cmb-chainstore.cdl8ar96w1hm.rds.cn-north-1.amazonaws.com.cn",
                                  port="5432")
    cursor = connection.cursor()
    sql = "select foreign_store_id from public.chain_store where cmid=%s and show_code='%s'" % (cmid, showcode)
    cursor.execute(sql)
    foreign_store_id = cursor.fetchall()
    return foreign_store_id[0][0]
