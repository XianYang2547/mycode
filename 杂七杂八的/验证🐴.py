# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/21 10:56
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : 验证🐴.py
# @Software: PyCharm
import random
s = ''
for i in range(6):
    num = random.randint(0,9)#0-9
    alpha1 = chr(random.randint(65,90))#A-Z
    alpha2 = chr(random.randint(97,122))#a-z
    ret = random.choice([num,alpha1,alpha2])#每次循环选取其中一个
    s += str(ret)
print(s)


