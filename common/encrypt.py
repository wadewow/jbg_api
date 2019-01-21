# coding:utf-8
import hashlib


def encrypt(**params):
    """
       密钥信息md5加密
       密钥信息：e06e9ca89e9d49c3ae427d2e56217ab0
    """
    values = ''
    for v in params.values():
        values += str(v)
    values += 'e06e9ca89e9d49c3ae427d2e56217ab0'
    m = hashlib.md5()
    m.update(values.encode('utf8'))
    sign = m.hexdigest()
    params['sign'] = sign
    return params

