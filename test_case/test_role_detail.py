# coding:utf-8
import unittest
from deal_api.role import RoleDetail


class TestRoleDetail(unittest.TestCase):
    def setUp(self):
        pass

    def test_role_detail_ok(self):
        """查询我的交易列表"""
        response_list = RoleDetail(api_name = 'RoleDetail').get_role_detail()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "获取角色详细信息失败！")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
