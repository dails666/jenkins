# -*- coding:utf-8 -*-
# 门店详情接口,GET请求方式
from cmdata.common import request_method


def get_store_detail(showcode=None, token=None):

    data = {'token': token}
    store_detail = request_method.get_request("https://qa-api.chaomengdata.com/metrics/get-store-detail/%s" % showcode,
                                              data)
    return store_detail.json()
