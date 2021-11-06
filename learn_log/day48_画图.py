# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/9/11 15:17
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day48_画图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
# #输入输出数据
# input1=[1,2,3,4,5]
# squares=[1,4,9,16,25]
# plt.plot(input1,squares,'ro')
# #xy轴标题 、大小
# plt.title('hit me')
# plt.xlabel('value',fontsize=15)
# plt.ylabel('squre',fontsize=15)
# #坐标轴刻度大小
# plt.tick_params(axis='both',labelsize=14)
# plt.show()

#自动计算数据
x=list(range(1,101))
y=[x**2 for x in x]
plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolors=None,s=5)
plt.show()
# plt.savefig('squre.tif',bbox_inches='tight')


