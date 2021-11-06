'''
用函数作为参数
要有闭包的特点
不改变原来函数，往上面加东西
def text():
    print('-------wocao-------')

def func(x):
    print(text)#打印上面的函数
    text()#调用上面的函数
    print('结束了')
func(text)#调用func
'''
#定义一个装饰器  decorate 在装饰器里面再执行一遍 被装饰的函数
def decorate(text):
    a=100
    def wrapper():
        text()
        print('-------wocao-------')
        print('-------nima-------',a)
    return wrapper
#使用装饰器
@decorate
#text函数很单调，但在开发中其他地方也用到，不方便修改它本身，把它送进一个装饰器来增加它功能，
def text():#被装饰的函数
    print('-------wocao-------')#原来text里的内容


#先不调用text，以上代码，先把text函数送进装饰器，进行修饰后返回wrapper，当我们接下来调用的时候，wrapper相当于我们调用的函数，它和text的地址上一样的
text()#调text 相当于调wraper       调用还是调用text函数，和装饰器函数无关
print(text)#<function decorate.<locals>.wrapper at 0x000001B0F2F3B1F0>
'''
装饰后的text-------wocao-------
         -------wocao-------
           -------nima------- 100
           运行步骤
1.text被装饰函数
2.将被装饰函数作为参数传给装饰器decorate
3.自动执行decorate函数
4.将返回值赋给text   上面返回的wrapper 默认上用text去接的，
'''

import time
def decorate(funx):
    def wrapper(*args,**kwargs):#接收多个参数，默认参数等
        print('正在校验中----')

        time.sleep(0.1) #暂停1秒
        funx(*args,**kwargs)

        print('校验好了')
        print()
    return wrapper
@decorate#调用装饰器
def f1(n):
    print('----f1----',n)
f1(55)

@decorate
def f2(name):
    print('----f2----',name)
f2('yasou')

@decorate
def f3(students,classs=2010):
    print('{}班的学生如下'.format(classs))
    for i in students:
        print(i)
students=['bob','lili','sala']
f3(students)

#多层装饰器
#装饰器公司1
def zhuang1(funv):
    print('-------1 start')
    def wrapper(*args,**kwargs):
        funv()
        print('刷漆')
    return wrapper
#装饰器公司2
def zhuang2(funv):
    print('--------2 start')
    def wrapper(*args,**kwargs):
        funv()
        print('装门')
    return wrapper
@zhuang2
@zhuang1
#两层装饰器，优先使用离def house（）最近的装饰器
def house():
    print('我是毛坯房')
#调用
house()
'''我是毛坯房
刷漆
装门'''

#带参数的装饰器
'''在装饰器函数外面 再定义一个函数
def outer(a):
    装饰器函数
    return decorate
'''
def outer(a):#负责接受装饰器的参数    @outer(100)#带参数
    def decorate(func):#负责接受函数
        def wrapper(*args,**kwargs):#负责接受 被装饰函数的参数
            func(*args,**kwargs)
            print('铺地砖{}块'.format(a))
        return wrapper
    return decorate

@outer(100)#带参数
#被装饰函数
def house(time):
    print('我{}来看房，是毛坯房'.format(time))

house('8月8日')




#装饰器的应用  登录验证
islogin=False#默认没有登录
#登录程序      返回的true或者false 给到islogin
def login():
    username=input('输入用户名')
    password=input('输入密码')
    if username=='xianyang' and password=='123':
        print('登录成功')
        return True
    else:
        print('账号或者密码错误')
        return False
#装饰器 要运行pay（） 需进到这里面 来判断是否登录
def decorate(xx):
    def wrapper(*args,**kwargs):
        global islogin
        if islogin:#第二次调用pay（）时，islogin值为true
            xx(*args,**kwargs)#加形参
        else:
            print('未登录，请登录')
            islogin=login()
    return wrapper
@decorate
#付款程序
def pay(money):
    print('正在付款')
    print('付款{}元\n付款完成'.format(money))

pay(500)
pay(100)



import time,datetime
def zhuangshiqi(func):
    def run_time(*args,**kwargs):
        print(args)
        print(kwargs)
        start_time=datetime.datetime.now()
        func(*args,**kwargs)
        end_time=datetime.datetime.now()
        print('spend time :',end_time-start_time)
    return run_time

@zhuangshiqi
def test1(x,y,z=0):
    summm=x+y+z
    time.sleep(1)
    print(summm)
test1(3,4,z=5)








