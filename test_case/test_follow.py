# coding:utf-8
import unittest
from deal_api.follow import Follow
from common.request_API import Access
from common.encrypt import encrypt


class TestFollow(unittest.TestCase):

    def setUp(self):
        self.followed_number = 0

    def test_1_set_20_follow_ok(self):

        """添加20个关注 """

        response_list = Follow(api_name = 'SetFollow').set_follow()
        for i in response_list:
            self.followed_number += 1
            print(f'已关注{self.followed_number}')
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "设置关注失败！")

    def test_2_set_21_follow_fail(self):

        """添加第21个关注失败"""

        params = {'o_serverid': 16, 'o_id': 1, 'serverid': 3711, 'uin': 40805092, 'account_id': 1, 'user_id': 1, 'ip': 1}
        params = encrypt(**params)
        response_code = int(Access('SetFollow', **params).get()['Data'].split()[-1])
        self.assertEqual(0, response_code)

    def test_3_follow_ist(self):

        """获取关注列表成功"""

        response_list = Follow('FollowList').get_follow_list()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "获取关注列表失败！")

    def test_4_disable_follow_ok(self):

        """取消关注成功"""

        response_list = Follow(api_name = 'DisableFollow').disable_follow()
        for i in response_list:
            test_result = i[0]
            expect_result = i[1]
            self.assertEqual(expect_result, test_result, msg = "取消关注失败！")

    def tearDown(self):
        print('********测试结束*********')


if __name__ == '__main__':
    unittest.main()


