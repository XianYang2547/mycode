# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from ch04.two_layer_net import TwoLayerNet

# 读入数据
#训练图像,训练标签 , 测试图像, 测试标签
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
'''大小：
x_train  60000*784
 t_train) 60000*10
 (x_test 10000*784
  t_test 10000*10
'''
network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000  # 适当设定循环的次数
train_size = x_train.shape[0]#60000
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)# 从60000中随机抽取100个
    #从选取的100个中，拿出它对应的图像数据  和  正确解标签数据
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 计算梯度
    #grad = network.numerical_gradient(x_batch, t_batch)
    grad = network.gradient(x_batch, t_batch)

    # 更新参数
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    #计算损失函数的值，并把该值添加到数组中
    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    '''i 是1到10000，iter_per_epoch=60000/100=600
    i % iter_per_epoch == 0迭代中，每600代 if表达式成立(成立17,i=0时算一次) 大约经历17个epoch'''
    if i % iter_per_epoch == 0:
        "训练数据 测试数据 计算识别精度"
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        #结果添加到列表中，画图时用作y轴   epoch用作x轴
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))

# 绘制图形
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))

plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')

plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)

plt.legend(loc='lower right')#设置图例位置  右下角
plt.show()