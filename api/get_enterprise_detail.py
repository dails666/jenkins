# -*- coding:utf-8 -*-
from cmdata.common import request_method

# 业绩追踪接口
def get_enterprise_detail(token):

    store_detail = request_method.get_request("https://api.chaomengdata.com/metrics/get-enterprise-detail?token=%s" %token)
    return store_detail.json()