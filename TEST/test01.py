'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2021/11/2 10:57
@Author : Xianyang
@Email : xy_mts@163.com
@File : test01.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'# 在导入tensorflow前使用，消除那一些列警告
import tensorflow as tf

random_float=tf.random.uniform(shape=[],minval=2,maxval=20)#定义一个  范围内的标量
zero_vector = tf.zeros(shape=(2),dtype=tf.int32)   # 定义一个有2个元素的零向量,指定元素的类型
print(random_float)
print(zero_vector)
#定义2个矩阵
A = tf.constant([[1, 2], [3, 4]])
B = tf.constant([[5, 6], [7, 8]])
C = tf.matmul(A, B)#*
D=tf.add(A,B)#+

print(C)
print(D.numpy())#张量的值转换为一个 NumPy 数组。[[ 6  8]
'''tf.Tensor([0 0], shape=(2,), dtype=int32) 变量与普通张量一样，变量同样具有形状、类型和值三种属性
使用变量需要有一个初始化过程，可以通过在 tf.Variable() 中指定 initial_value 参数来指定初始值
'''

                                        #    [10 12]]
#自动求导
x1=tf.Variable(initial_value=3.)#定义一个变量x，指定初始值为 3.==3.0
with tf.GradientTape() as tape:
    y1=tf.square(x1)
y_=tape.gradient(y1,x1)
print(y_)
'''tf.GradientTape() 是一个自动求导的记录器。只要进入了 with tf.GradientTape() as tape 的上下文环境，
则在该环境中计算步骤都会被自动记录。比如在上面的示例中，计算步骤 y = tf.square(x) 即被自动记录。
离开上下文环境后，记录将停止，但记录器 tape 依然可用，因此可以通过 
y_grad = tape.gradient(y, x) 求张量 y 对变量 x 的导数。'''

x=tf.constant([[1.,2.],[3.,4.]])
y=tf.constant([[1.],[2.]])
w=tf.Variable(initial_value=[[1.],[2.]])
b=tf.Variable(initial_value=1.)
with tf.GradientTape() as tape:
    L=tf.reduce_sum(tf.square(tf.matmul(x,w)+b-y))
#计算偏导
w_grad, b_grad=tape.gradient(L,[w,b])
print(L,w_grad,b_grad)


import numpy as np

p = np.poly1d([1, 2, 0, 3, 0, 5])   # 构造多项式

print(p)