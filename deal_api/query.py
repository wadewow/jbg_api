# coding:utf-8
from common.request_API import Access
from common.get_EXCEL_test_data import *
import json


class QueryOrder:
    def __init__(self, api_name='QueryOrder'):
        """
        :param api_name: like --> 'QueryOrder'
        """
        self.response_list = []
        self.data_list = post_excel_test_data(api_name)
        for i in self.data_list:
            check_point = json.loads(i.pop('check_point'))
            i['Param'] = json.loads(i['Param'])
            i['Pagination'] = json.loads(i['Pagination'])
            response = Access(api_name, **i).post_json()
            self.response_list.append([response, check_point])

    def query_order(self):
        return self.response_list

#
# r = QueryOrder().query_order()
# print(r)