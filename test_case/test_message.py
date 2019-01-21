# coding:utf-8
import unittest
from deal_api.message import SMS


class TestSendMessage(unittest.TestCase):
    def setUp(self):
        pass

    def test_send_message_ok(self):

        """发送短信成功"""

        response_list = SMS(api_name = 'SendSMSMessage').send_message()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "发短信失败！")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
