# coding:utf-8
from common.encrypt import *
import xlrd
import os

file_path = os.path.join((os.path.dirname(os.getcwd())), r'test_data\jbg_test_case.xlsx')


class GetExcelData:
    def __init__(self, sheet_name):
        self.sheet_name = sheet_name
        self.data = []
        self.work_book = xlrd.open_workbook(file_path)
        self.sheet = self.work_book.sheet_by_name(self.sheet_name)
        self.rows = self.sheet.nrows
        self.cols = self.sheet.ncols
        # 获取key
        self.key = self.sheet.row_values(1)[1:self.cols-1]

    def get_excel_test_data(self):
        """
        请求方式等于get时使用
        :return type: list --> [{...},{...},{...}...]
        """
        for i in range(2, self.rows):
            value = self.sheet.row_values(i)[1:self.cols-1]
            # 获取预期结果
            check_point = self.sheet.row_values(i)[-1]
            for k, v in enumerate(value):
                """将float数据转成int型"""
                if isinstance(v, float):
                    value[k] = int(v)
            payload = encrypt(**dict(zip(self.key, value)))
            payload['check_point'] = check_point
            self.data.append(payload)
        return self.data

    def post_excel_test_data(self):
        """
        请求方式等于post时使用
        :return type: list --> [{...},{...},{...}...]
        """
        for i in range(2, self.rows):
            value = self.sheet.row_values(i)[1:self.cols-1]
            # 获取预期结果
            check_point = self.sheet.row_values(i)[-1]
            for k, v in enumerate(value):
                """将float数据转成int型"""
                if isinstance(v, float):
                    value[k] = int(v)
            payload = dict(zip(self.key, value))
            payload['check_point'] = check_point
            self.data.append(payload)
        return self.data


if __name__ == '__main__':
    GetExcelData('SetFollow').get_excel_test_data()
