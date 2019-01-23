# coding:utf-8
from common.request_API import Access
from common.get_EXCEL_test_data import GetExcelData
import json


class SMS:
    def __init__(self, api_name='SendSMSMessage'):
        """
        :param api_name: like --> 'SendSMSMessage'
        """
        self.response_list = []
        data_list = GetExcelData(api_name).get_excel_test_data()
        for i in data_list:
            check_point = json.loads(i.pop('check_point'))
            response = Access(api_name, **i).get()
            self.response_list.append([response, check_point])

    def send_message(self):
        return self.response_list

