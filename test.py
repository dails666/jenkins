# _*_ coding:utf-8 _*_
from common.ep_showcode import *
from common import HTMLTestRunner
from common.sql_connect import *
import unittest
import datetime
import time
import os

PRO_DIR = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
CASE_DIR = os.path.join(PRO_DIR, "cases")
FILE_DIR = os.path.join(PRO_DIR, "report")







    # 查询企业月报
def creatsuite():
    testunit=unittest.TestSuite()
    #定义discover 方法的参数
    discover=unittest.defaultTestLoader.discover(CASE_DIR,pattern='test_*.py',
    top_level_dir=None)
    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:

        testunit.addTests(test_case)
        return testunit

# 生成报告
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = FILE_DIR + '//' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'企业上日销售额统计',
    description=u'企业名下所有门店上日销售额汇总')

if __name__ == '__main__':
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()







    '''
    # 应销未销商品查询
    def test_yxwx_item(self, cmid, storeid, item_cat1_ignores):

        should_sell_not_sell()
        self.cursor.execute(self.sql)

    # 滞销商品查询
    def test_zx_item(self, cmid, storeid, item_cat1_ignores):

        should_not_sell()
        self.cursor.execute(self.sql)

    # 畅缺商品查询
    def test_cq_item(self):

        for sheet in range(4):

            self.excel(sheet)
            sql = should_sell_out_of_stock(self.source_id, self.cmid, self.item_cat1_ignores, self.days_delay)
            self.cursor.execute(sql)
            self.cursor.fetchall()


    '''

