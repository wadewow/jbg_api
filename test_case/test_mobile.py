# coding:utf-8
import unittest
from deal_api.mobile import Mobile
from common.encrypt import *
from common.content_mysql import DB
from common.request_API import Access
'''
Created on 2018-10-23
@author: wade
Project: 聚宝阁API测试'''


class TestMobileCertificate(unittest.TestCase):
    def setUp(self):
        pass

    def test_GetMobileNumber_ok(self):
        """获取密保手机"""
        response_list = Mobile('GetPassSafeMobile').get_mobile_number()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "获取密保手机失败！")

    def test_SendVerificationCode_ok(self):
        """发送验证码"""
        response_list = Mobile('SendVerificationCode').send_verification_code()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "发送验证码失败！")

    def tearDown(self):
        print('********测试结束*********')


class TestCheckCertificate(unittest.TestCase):
    def setUp(self):
        # 先调用发验证码接口
        params = {'serverId': 3711, 'uin': 40805092, 'account_id': 22650705, 'user_id': 15001242, 'ip': 123456}
        params = encrypt(**params)
        Access('SendVerificationCode', **params).get()
        # 获取数据库最新的验证码
        self.verify_code = int(DB().get_verification_code())

    def test_check_verification_code_ok(self):
        """校验验证码成功"""
        # 调用校验验证码接口
        payload = {'serverId': 3711, 'uin': 40805092, 'account_id': 22650705, 'user_id': 15001242, 'ip': 123456,
                   'verify_code': self.verify_code}
        payload = encrypt(**payload)
        response = Access('CheckVerificationCode', **payload).get()
        message = response['Message']
        self.assertEqual('Verification Code is correct!', message)

    def test_check_verification_code_fail(self):
        """校验验证码失败"""
        payload = {'serverId': 3711, 'uin': 40805092, 'account_id': 22650705, 'user_id': 15001242, 'ip': 123456,
                   'verify_code': 12345}
        payload = encrypt(**payload)
        response = Access('CheckVerificationCode', **payload).get()
        message = response['Message']
        self.assertEqual('Verification Code is not correct!', message)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()




