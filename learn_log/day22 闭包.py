# 闭包
# 调用函数里面定义的函数
'''

'''
def func():
    a=99
    def func1():
        b=22
        print(a,b)
    #调用
    return func1 # 不加括号
#调用
x=func() # 把里面定义的函数扔出来用x接住
x() # 100 99
# 这样也行
func()()
print('*'*20)
# 例
def hanshu(a,b):
    c=10
    def hanshu2():
        s=a+b+c
        print(s)
    return hanshu2
#调用 hanshu
i_hanshu=hanshu(1,2) # i_hanshu 就是hanshu2
# 调用反出来的内部函数
i_hanshu()

hanshu(1,2)() # 这样也行
print('*'*20)

# # 计数器
def countXX():
    count=[0]
    def add_one():
        count[0]=count[0]+1
        print('这是第{}次访问'.format(count[0]))
    return add_one
xy=countXX()
xy()
xy()
xy()
# 这是第1次访问
# 这是第2次访问
# 这是第3次访问

def bibao(a,b):
    c=10
    def son():
        s=a+b+c
        print(s)
    return son
tx1=bibao(4,4)#接住

tx2=bibao(2,2)
tx3=bibao(10,10)
tx1()
tx2()
tx3()
# 18 14 30  每调用一次  都开辟个空间存数据，所有3个tx的值不影响

'''闭包的缺点：1 作用阈没有那么直观
            2 因为变量不会被回收所有有一定的内存占有
 '''        

