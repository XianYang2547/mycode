'''
语法：lambda 参数：表达式
先写lambda关键字，然后依次写匿名函数的参数，多个参数中间用逗号连接，然后是一个冒号，冒号后面写返回的表达式。
使用lambda函数可以省去函数的定义，不需要声明一个函数然后使用，而可以在写函数的同时直接使用函数
lambda适用于多个参数、一个返回值的情况，可以用一个变量来接收，变量是一个函数对象，执行这个函数对象的结果与执行一个普通函数的结果一样。。
'''
#匿名函数与普通函数的对比
def sum_func(a, b, c):
    return a + b + c

sum_lambda = lambda a, b, c: a + b + c

print(sum_func(1, 100, 10000))
print(sum_lambda(1, 100, 10000))


# 无参数
lambda_a = lambda: 100
print(lambda_a())
# 一个参数
lambda_b = lambda num: num * 10
print(lambda_b(5))
# 多个参数
lambda_c = lambda a, b, c, d: a + b + c + d
print(lambda_c(1, 2, 3, 4))
# 表达式分支
lambda_d = lambda x: x if x % 2 == 0 else x + 1
print(lambda_d(6))
print(lambda_d(7))

#lambda作为一个参数传递
def sub_func(a, b, func):
    print('a =', a)
    print('b =', b)
    print('a - b =', func(a, b))
sub_func(100, 1, lambda a, b: a - b)
#       lambda a, b: a - b=fun

# member_list = [
#     {"name": "风清扬", "age": 99, "power": 10000},
#     {"name": "无崖子", "age": 89, "power": 9000},
#     {"name": "王重阳", "age": 120, "power": 8000}
# ]
# new_list = sorted(member_list, key=lambda dict_: dict_["power"])
# print(new_list)

'''
map() 第一个参数接受一个函数名，后面参数接受一个或者多个可迭代的序列
把函数依次作用在序列的每个元素上  返回一个列表
'''
number_list = [100, 77, 69, 31, 44, 56]
num_sum = list(map(lambda x: {str(x): x}, number_list))
print(num_sum)

def sq(x):
    return x**2
x=list(map(sq,[1,2,3,4]))
print(x)



