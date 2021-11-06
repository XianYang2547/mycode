# 定义函数：随机数的产生
# import random
import random
#
#
def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


generate_random()
print('*' * 20)

# 带参数的函数
# 求多少多少个随机数


# def suiji(count):
#     for i in range(count):
#         ran = random.randint(1, 20)
#         print(ran)
#
# count=int(input('输入你要产生的随机数个数:'))
# suiji(count)

# def add(a, b):
#     result = a+b
#     print(result)
#
# a=int(input('a'))
# b=int(input('b'))
# add(a, b)

'''定义一个登录函数，参数是 username password
函数体：
判断参数传过来的username password 是否正确，正确则登录成功，反之
'''


# def login(username, password):
#     name = 'admin'
#     word = '123'
#     for i in range(3):
#         if username == name and password == word:
#             print('登录成功')
#             break
#         else:
#             print('登录失败,你还有2此机会')
#             username = input('输入用户名：')
#             password = input('输入密码')
#     else:
#         print('锁定了')


# 調用
# username = input('输入用户名：')
# password = input('输入密码')
# login(username, password)


# 找列表中最大的那個[5,6,3,4,7,8,1,9]
# def max1(x):
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             if i > j:
#                 l[i, j] = l[j, i]
#     print('最大值是：', l[-1])
#
#
# l = [5, 6, 3, 4, 7, 8, 1, 9]
# max1(l)


