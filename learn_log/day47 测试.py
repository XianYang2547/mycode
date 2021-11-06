# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/30 9:19
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day47 测试.py
# @Software: PyCharm
import unittest
from learn_log.day47_测试用的函数 import get_name


class Test1Case(unittest.TestCase):
    '测试day47那个函数'
    def test_first_last(self):
        name=get_name('xian','yang')
        self.assertEqual(name,'Xian Yang')

    def test_first_middle_last(self):
        name=get_name('xian','xiao','yang')
        self.assertEqual(name,'Xian Xiao Yang')
unittest.main()


