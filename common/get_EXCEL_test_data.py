# coding:utf-8
from common.encrypt import *
import xlrd
import os

file_path = os.path.join((os.path.dirname(os.getcwd())), r'test_data\jbg_test_case.xlsx')


def get_excel_test_data(sheet_name='GetPassSafeMobile'):
    """
    :param sheet_name: 表名
    :return type: list --> [{...},{...},{...}...]
    """
    data = []
    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_name(sheet_name)
    rows = sheet.nrows
    cols = sheet.ncols
    # 获取key
    key = sheet.row_values(1)[1:cols - 1]
    for i in range(2, rows):
        value = sheet.row_values(i)[1:cols - 1]
        # 获取预期结果
        check_point = sheet.row_values(i)[-1]
        for k, v in enumerate(value):
            """将float数据转成int型"""
            if isinstance(v, float):
                value[k] = int(v)
        payload = encrypt(**dict(zip(key, value)))
        # 将预期结果添加到参数中
        payload['check_point'] = check_point
        data.append(payload)
    return data


def post_excel_test_data(sheet_name='FollowList'):
    data = []
    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_name(sheet_name)
    rows = sheet.nrows
    cols = sheet.ncols
    # 获取key
    key = sheet.row_values(1)[1:cols - 1]
    for i in range(2, rows):
        value = sheet.row_values(i)[1:cols - 1]
        # 获取预期结果
        check_point = sheet.row_values(i)[-1]
        for k, v in enumerate(value):
            """将float数据转成int型"""
            if isinstance(v, float):
                value[k] = int(v)
        payload = dict(zip(key, value))
        # 将预期结果添加到参数中
        payload['check_point'] = check_point
        data.append(payload)
    return data

