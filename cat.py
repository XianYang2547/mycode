import numpy as np
import h5py
import matplotlib.pyplot as plt

def load_dataset():
    train_dataset = h5py.File('E:\PYTHON\AI_HomeWork/datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('E:\PYTHON\AI_HomeWork/datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes

def sigmoid(z):
    s = 1/(1+np.exp(-z))
    return s

def initialize_with_zeros(dim):
    "初始化w，b参数"
    w = np.zeros((dim,1))
    b = 0
    return w, b

def propagate(w, b, X, Y,):
    """
    实现前向和后向传播的成本函数及其梯度。
    参数：
        w  - 权重，大小不等的数组（num_px * num_px * 3，1）
        b  - 偏差，一个标量
        X  - 矩阵类型为（num_px * num_px * 3，训练数量）
        Y  - 真正的“标签”矢量（如果非猫则为0，如果是猫则为1），矩阵维度为(1,训练数据数量)
    返回：
        cost- 逻辑回归的负对数似然成本
        dw  - 相对于w的损失梯度，因此与w相同的形状
        db  - 相对于b的损失梯度，因此与b的形状相同
    """
    m = X.shape[1]

    # 正向传播
    A = sigmoid(np.dot(w.T,X)+b)
    cost = -1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))#计算成本
    # 反向传播
    dw = 1 / m * np.dot(X, (A - Y).T)
    db = 1 / m * np.sum(A - Y) 


    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())

    grads = {"dw": dw, 
             "db": db}
    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    '''    参数：
        w  - 权重，大小不等的数组（num_px * num_px * 3，1）
        b  - 偏差，一个标量
        X  - 维度为（num_px * num_px * 3，训练数据的数量）的数组。
        Y  - 真正的“标签”矢量（如果非猫则为0，如果是猫则为1），矩阵维度为(1,训练数据的数量)
        num_iterations  - 优化循环的迭代次数
        learning_rate  - 梯度下降更新规则的学习率
        print_cost  - 每100步打印一次损失值

    返回：
        params  - 包含权重w和偏差b的字典
        grads  - 包含权重和偏差相对于成本函数的梯度的字典
        成本 - 优化期间计算的所有成本列表，将用于绘制学习曲线。
        '''
    costs = []

    for i in range(num_iterations):
        #计算当前参数的成本和梯度，使用propagate（）
        grads, cost =propagate(w, b, X, Y)

        dw = grads["dw"]
        db = grads["db"]

        #使用w和b的梯度下降法则更新参数
        w = w - learning_rate * dw
        b = b - learning_rate * db
        # 打印成本数据
        # print ("Cost after iteration %i: %f" %(i, cost))#i 迭代次数

    params = {"w":w,
              "b":b}

    grads = {"dw": dw,
             "db": db}

    return params,grads,costs

def predict(params,X):
    w = params["w"]
    b = params["b"]
    y_hat = sigmoid(np.dot(w.T,X)+b)
    return y_hat

train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes = load_dataset()

m_train = train_set_y_orig.shape[1] #训练集里图片的数量。
m_test = test_set_y_orig.shape[1] #测试集里图片的数量。
num_px = train_set_x_orig.shape[1] #训练、测试集里面的图片的宽度和高度（均为64x64）。train_set_x_orig 是一个维度为(m_​​train，num_px，num_px，3）的数组
print ("训练集的数量: m_train = " + str(m_train))#209
print ("测试集的数量 : m_test = " + str(m_test))#50
print ("每张图片的宽/高 : num_px = " + str(num_px))#64
print ("每张图片的大小 : (" + str(num_px) + ", " + str(num_px) + ", 3)")#(64, 64, 3)
print ("训练集_图片的维数 : " + str(train_set_x_orig.shape))#(209, 64, 64, 3)
print ("训练集_标签的维数 : " + str(train_set_y_orig.shape))#(1, 209)
print ("测试集_图片的维数: " + str(test_set_x_orig.shape))#(50, 64, 64, 3)
print ("测试集_标签的维数: " + str(test_set_y_orig.shape))#(1, 50)

''''将形状（a，b，c，d）的矩阵X平铺成形状（b * c * d，a）的矩阵X_flatten
X_flatten=X.reshape(X.shape[0],-1).T #T代表转置
将训练集和测试集的维度降低并转置,-1会让程序自动帮你算原本有多少列'''
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

print("训练集降维最后的维度：" + str(train_set_x_flatten.shape))
print("测试集降维之后的维度: " + str(test_set_x_flatten.shape))
#标准化数据集：
train_set_x = train_set_x_flatten/255.0
test_set_x = test_set_x_flatten/255.0

dim = train_set_x.shape[0]
w,b = initialize_with_zeros(dim)
params,grads,costs = optimize(w,b,train_set_x,train_set_y_orig,2000,0.005,True)

y_test_hat = predict(params,test_set_x)
print(str(y_test_hat))
print("Num of test figure is " + str(np.shape(test_set_y_orig)[1]))
print("Results of prediction as\r\n")
print(test_set_y_orig - y_test_hat)

Loop = True
index = 0
while Loop:
    index = int(input("Please input the index to verify i<50\r\n"))
    if index < 0 or index >= 50:
        Loop = False
        break
    if test_set_y_orig[0][index]== 1:
        first_statement = "predicted :"
    else:
        first_statement = "predicted :"
    if y_test_hat[0][index] >0.8:
        second_statement = " Cat"
    else:
        second_statement = " Not Cat"
    plt.matshow(test_set_x_orig[index])
    plt.title(first_statement + second_statement+"\r\ny_hat =" + str(y_test_hat[0][index]))
    plt.show()
