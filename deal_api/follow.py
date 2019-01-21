# coding:utf-8
from common.request_API import Access
from common.get_EXCEL_test_data import *
import json


class Follow:
    def __init__(self, api_name='FollowList'):
        """
        :param api_name: like --> 'FollowList'
        """
        self.response_list = []
        if api_name == 'FollowList':
            self.data_list = post_excel_test_data(api_name)
            print(self.data_list)
            for i in self.data_list:
                check_point = json.loads(i.pop('check_point'))
                response = Access(api_name, **i).post()
                self.response_list.append([response, check_point])
        elif api_name in ('SetFollow', 'DisableFollow'):
            self.data_list = get_excel_test_data(api_name)
            for i in self.data_list:
                check_point = json.loads(i.pop('check_point'))
                response = Access(api_name, **i).get()
                self.response_list.append([response, check_point])

    def set_follow(self):
        """添加关注"""
        return self.response_list

    def get_follow_list(self):
        """获取关注列表"""
        return self.response_list

    def disable_follow(self):
        return self.response_list
