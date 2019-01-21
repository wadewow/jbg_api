# coding:utf-8
import unittest
from deal_api.tradelist import TradeList


class TestTradeList(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_my_trade_list_ok(self):
        """查询我的交易列表"""
        response_list = TradeList(api_name = 'MyTradeList').get_my_trade_list()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "获取我的交易列表失败！")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
