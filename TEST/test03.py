'''
爱生活，爱......
-- coding: UTF-8  --
@Time : 2021/11/6 14:43
@Author : Xianyang
@Email : xy_mts@163.com
@File : test03.py
@Software: PyCharm
♡♡♡---Beauty is about to begin...
'''
import numpy as np
import tensorflow as tf
"用y=ax+b拟合下面的数据"
x_raw=np.array([2017,2018,2019,2020,2021],dtype=np.float32)
y_raw=np.array([12000,14000,15000,16500,17500],dtype=np.float32)
#归一化
x=(x_raw-x_raw.min())/(x_raw.max()-x_raw.min())
y=(y_raw-y_raw.min())/(y_raw.max()-y_raw.min())
print(x,y)

a, b = 0, 0

num_epoch = 10000
learning_rate = 5e-4
for e in range(num_epoch):
    # 手动计算损失函数关于自变量（模型参数）的梯度
    y_pred = a * x + b
    grad_a, grad_b = 2 * (y_pred - y).dot(x), 2 * (y_pred - y).sum()

    # 更新参数
    a, b = a - learning_rate * grad_a, b - learning_rate * grad_b

print(a, b)

X = tf.constant(x)
y = tf.constant(y)

a = tf.Variable(initial_value=0.)
b = tf.Variable(initial_value=0.)
variables = [a, b]

num_epoch = 10000
'''声明了一个梯度下降 优化器 （Optimizer），其学习率为 5e-4。
优化器可以帮助我们根据计算出的求导结果更新模型参数，从而最小化某个特定的损失函数，
具体使用方式是调用其 apply_gradients() 方法。'''
optimizer = tf.keras.optimizers.SGD(learning_rate=5e-4)
for e in range(num_epoch):
    # 使用tf.GradientTape()记录损失函数的梯度信息
    with tf.GradientTape() as tape:
        y_pred = a * X + b
        loss = tf.reduce_sum(tf.square(y_pred - y))
    # TensorFlow自动计算损失函数关于自变量（模型参数）的梯度
    grads = tape.gradient(loss, variables)
    # TensorFlow自动根据梯度更新参数
    optimizer.apply_gradients(grads_and_vars=zip(grads, variables))

print(a,b)





