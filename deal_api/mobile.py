# coding:utf-8
from common.request_API import Access
from common.content_mysql import DB
from common.get_EXCEL_test_data import *
from common.encrypt import *
import json


class Mobile:
    def __init__(self, api_name='GetPassSafeMobile'):
        """
        :param api_name: like --> 'GetPassSafeMobile'
        """
        self.response_list = []
        data_list = get_excel_test_data(api_name)
        for i in data_list:
            check_point = json.loads(i.pop('check_point'))
            response = Access(api_name, **i).get()
            self.response_list.append([response, check_point])

    def get_mobile_number(self):
        return self.response_list

    def send_verification_code(self):
        return self.response_list


class CheckVerificationCode:
    def __init__(self):
        pass

    @staticmethod
    def check_verification_code():
        """
        :tips: uin = 40805092 --> 17688834313的手机号码
        :return:
        """
        # 先调用发验证码接口
        params = {'serverId': 3711, 'uin': 40805092, 'account_id': 22650705, 'user_id': 15001242, 'ip': 123456}
        params = encrypt(**params)
        Access('SendVerificationCode', **params).get()
        # 获取数据库最新的验证码
        verify_code = int(DB().get_verification_code())
        # 调用校验验证码接口
        payload = {'serverId': 3711, 'uin': 40805092, 'account_id': 22650705, 'user_id': 15001242, 'ip': 123456,
                   'verify_code': verify_code}
        payload = encrypt(**payload)
        response = Access('CheckVerificationCode', **payload).get()
        return response
