# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/30 9:20
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day47_测试用的函数.py
# @Software: PyCharm
def get_name(first,last,middle=''):
    "生成整洁的名字"
    if middle:
        fullname=first+' '+last
    else:
        fullname=first+' '+middle+' '+last
    return fullname.title()


