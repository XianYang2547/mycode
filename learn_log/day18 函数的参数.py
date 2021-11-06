# day18
# #############################可变参数
# def add(a, b):
#     pass
# add(1) add这里缺失了一个参数b
# 方法
# 求你想輸入的几个数的和。。。。。当不知道输入的参数的个数时 用*args

# def add(*args): # arge是一個元組
#     sum = 0
#     if len(args) > 0:
#         for i in args:
#             sum += i
#             print(sum)
#     else:
#         print('沒有元素可計算', sum)
# add(1, 5)##送值方式


# -----------不可变参数结合可变参数  * 系统准备一个元组
# def add(不可变参数，*args): # arge是一個元組。(不可变参数，*args)=(‘sb’，1, 5)
#     sum = 0#                           sb赋给不可变参数  1，5 赋给arge
#     if len(args) > 0:
#         for i in args:
#             sum += i
#             print(sum)
#     else:
#         print('沒有元素可計算', sum)
# add(‘sb’，1, 5)


# #############################参数的默认值
def add(a, b=10, c=2):
    result = a + b + c
    print(result)


add(5)  # 15   a=5 b=10 c=2
add(5, 2)  # 16 a=5 b=11, c=2 把默认值10覆盖了
# 默认一次赋值，先给b赋值，再轮到c
add(5, c=4)  # a=5 b=10 c=4

# ** 看到**系统就准备一个字典
dict1 = {'1': 'py', '2': 'c+', '3': 'java'}


def func0(user, **language):
    print('{}喜欢的语言是：'.format(user))
    mm = language.items()  # 获取键值对
    for i, j in mm:
        print('排行{}，是：{}'.format(i, j))


func0('小明', **dict1)




#
def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2)  # 1 2 () {}  1 2 赋给 a b
bb(1, 2, 3, 4)  # 1 2 (3, 4) {} ...3 4 赋给c 元组形式
bb(1, 2, 3, x=10)  # 1 2 (3,) {'x': 10}  3 赋给c x=10赋给d 字典形式
bb(1, 2, x=100, y=100)  # 1  2 () {'x': 100, 'y': 100} x=100, y=100 赋给d


'''
无参数函数
def func():
    pass
func() ---->调用

有参数函数
    1.普通参数
    def func(name,age)
        pass
    func(a,b)----->传2个参数

    2.可变参数
    A   def func(*args)
            pass
        func()----->函数调用时，参数可以没有，也可以多个参数
    
    B   def func(**kwargs)
            pass
        func(a=1,b=2)----->函数调用时参数可以没有，也可以多个参数
    
    C    func(*args,**kwargs)
            pass
            list1=[1,30]
            dict1={'a':'1','b':'2'}
          func(*list1,**dict1)
        
    D    def func(name, *c, **d):
            pass
         func('bob') name的参数一定要给，其他不一定要给
    3.默认值
    def func(a,b=5):
        pass
    func(5)
    func(5,3)


'''

