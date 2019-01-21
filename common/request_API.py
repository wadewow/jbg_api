# coding:utf-8
from ConfigurationFolder.ReadConfig import ReadConfig
import requests


class Access:
    """
    1、调用requests库get、post方法访问，并返回dict数据类型。
    """

    def __init__(self, url, **kwargs):
        """
        :param url: config.ini --> "SetFollow"
        :param kwargs: 接口参数
        """
        self.url = ReadConfig().get_url(url)
        self.kwargs = kwargs

    def get(self):
        """
        :return: get响应数据
        :response_data_format: dict
        """
        resp = requests.get(self.url, params = self.kwargs).json()
        return resp

    def post(self):
        """
        :return: post响应数据
        :response_data_format: dict
        """
        resp = requests.post(self.url, data = self.kwargs).json()
        return resp

    def post_json(self):
        """
        :return:
        """
        resp = requests.post(self.url, json =self.kwargs).json()
        return resp
