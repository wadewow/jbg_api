# coding:utf-8
from common.request_API import Access
from common.get_EXCEL_test_data import *
import json


class RoleDetail:
    def __init__(self, api_name='RoleDetail'):
        """
        :param api_name: like --> 'RoleDetail'
        """
        self.response_list = []
        data_list = post_excel_test_data(api_name)
        for i in data_list:
            check_point = json.loads(i.pop('check_point'))
            response = Access(api_name, **i).post()
            self.response_list.append([response, check_point])

    def get_role_detail(self):
        return self.response_list



