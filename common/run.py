# coding:utf-8
import os
import unittest
import time
from common import HTMLTestRunner
test_dir = os.path.dirname(os.getcwd())
discover = unittest.defaultTestLoader.discover(os.path.join(test_dir, 'test_case'), pattern = 'test_*.py')
current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
file_path = os.path.join(test_dir, f'result\\{current_time}.html')
with open(file_path, 'wb') as ftp:
    runner = HTMLTestRunner.HTMLTestRunner(stream = ftp, title = '聚宝阁接口测试结果')
    runner.run(discover)
