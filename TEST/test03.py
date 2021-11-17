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
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import tensorflow as tf
"用y=ax+b拟合下面的数据"
x_raw=np.array([2013,2014,2015,2016,2017],dtype=np.float32)
y_raw=np.array([12000,14000,15000,16500,17500],dtype=np.float32)
#归一化  利于梯度下降
'''/分析上述操作，x_row - x_row.min()所作的是将x_row向量每一项都减去该向量中的最小值，即
x_row.min()，这一步操作产生的结果就是 新的向量x_row都缩小了，并且必定有一项是0（即原来那个
x_row.min()项）。再看分母是 x_row.max()-x_row.min() >= 0 , 在上下相除之后，必定有一项是0，
还有一项是1（即原来那个x_row.max()，该项的分子分母相等），其余的项都是在0~1之间，所以说，这
一顿骚操作，成功的把向量x_row 中每一项的值都限定在了0~1之间，这样梯度下的就快多了
'''
x=(x_raw-x_raw.min())/(x_raw.max()-x_raw.min())
y=(y_raw-y_raw.min())/(y_raw.max()-y_raw.min())
# print(x,y)

a, b = 0, 0

"numpy方法"
num_epoch = 10000
learning_rate = 1e-3

for e in range(num_epoch):
    # 手动计算损失函数关于自变量（模型参数）的梯度
    y_pred = a * x + b
    grad_a, grad_b = 2 * (y_pred - y).dot(x), 2 * (y_pred - y).sum()

    # 更新参数
    a, b = a - learning_rate * grad_a, b - learning_rate * grad_b

print(a, b)
print('*'*50)

"TensorFlow方法"
X = tf.constant(x)
y = tf.constant(y)

a = tf.Variable(initial_value=0.)#初始化参数为0.就行
b = tf.Variable(initial_value=0.)
variables = [a, b]  #变量组
num_epoch = 10000   #下降次数
'''声明了一个梯度下降 优化器 （Optimizer），其学习率为 5e-4。
优化器可以帮助我们根据计算出的求导结果更新模型参数，从而最小化某个特定的损失函数，
具体使用方式是调用其 apply_gradients() 方法。'''
optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)

for e in range(num_epoch):
    # 使用tf.GradientTape()记录损失函数的梯度信息
    with tf.GradientTape() as tape:
        y_pred = a * X + b #预测值
        #损失函数 ? 0.5*tf.reduce_sum(tf.square(y_pred - y))
        loss = 0.5*tf.reduce_sum(tf.square(y_pred - y))# tf.reduce_sum 求和
    # TensorFlow自动计算损失函数关于自变量（模型参数）的梯度
    grads = tape.gradient(loss, variables)
    # TensorFlow自动根据梯度更新参数
    optimizer.apply_gradients(grads_and_vars=zip(grads, variables))
#结果用numpy格式展示
print(a.numpy(),b.numpy())





