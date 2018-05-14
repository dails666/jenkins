# _*_coding: utf-8 _*_
import requests

# GET请求方法
def get_request(url, data=None, **kwargs):

    return requests.get(url, params=data)

# POST请求方法
def post_request(url, data=None, **kwargs):

    return requests.post(url, json=data)