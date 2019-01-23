# coding:utf-8
import os
import unittest
from common.SendEmail import send_email
from common import HTMLTestRunner

if __name__ == '__main__':
    test_dir = os.path.dirname(os.getcwd())
    discover = unittest.defaultTestLoader.discover(os.path.join(test_dir, 'test_case'), pattern = 'test_*.py')
    file_path = os.path.join(test_dir, r'result\test_report.html')
    with open(file_path, 'wb') as ftp:
        runner = HTMLTestRunner.HTMLTestRunner(stream = ftp, title = '聚宝阁接口测试报告')
        runner.run(discover)
    # 发送测试报告邮件
    send_email()
