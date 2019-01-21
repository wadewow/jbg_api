# coding:utf-8
import unittest
from deal_api.query import QueryOrder


class TestQueryOrder(unittest.TestCase):
    def setUp(self):
        pass

    def test_query_order_ok(self):
        """查询订单列表"""
        response_list = QueryOrder(api_name = 'QueryOrder').query_order()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "获取订单失败！")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
