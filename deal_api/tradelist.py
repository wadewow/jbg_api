# coding:utf-8
from common.request_API import Access
from common.get_EXCEL_test_data import *
import json


class TradeList:
    def __init__(self, api_name='MyTradeList'):
        """
        :param api_name: like --> 'MyTradeList'
        """
        self.response_list = []
        data_list = post_excel_test_data(api_name)
        for i in data_list:
            check_point = json.loads(i.pop('check_point'))
            response = Access(api_name, **i).post()
            self.response_list.append([response, check_point])

    def get_my_trade_list(self):
        return self.response_list
