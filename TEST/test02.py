'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2021/11/6 10:28
@Author : Xianyang
@Email : xy_mts@163.com
@File : test02.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''
#向量化和非向量化对比
import numpy as np
from time import time
a=np.random.rand(100000)
b=np.random.rand(100000)
tic=time()

c=np.dot(a,b)
toc=time()
print(1000*(toc-tic))

x=0
tic1=time()
for i in range(100000):
    c+=a[i]*b[i]
toc1=time()
print(1000*(toc1-tic1))


#`sum`的参数`axis=0`表示求和运算按列执行
A=np.array([[56.,0.,4.4,68.],
            [1.2,104.,52.,8.],
            [1.8,135.,99.,0.9]])
print(A)
"axis用来指明将要进行的运算是沿着哪个轴执行，在numpy中，" \
"0轴是垂直的，也就是列，而1轴是水平的，也就是行。"
cal=A.sum(axis=0)#[ 59.  239.  155.4  76.9]

print(cal)
percentage=A/cal*100
print(percentage)

q=np.array([1,2,3,4,5]).reshape(1,5).T
print(q)

print(np.dot(q,q.T))

