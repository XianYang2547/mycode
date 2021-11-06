# 函数的综合应用
'''
用户登录
输入用户名密码
输入验证码
'''
import random


# 定义验证码生成函数
def checkcode(n):  #    产生n位随机数
    s = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s)-1)
        code += s[ran]
    return code


username = input('输入用户名：')
password = input('输入密码')
# 得到验证码
code = checkcode(4) # 调用函数
print('你的验证马是(不区分大小写)：', code)
code1 = input('输入验证码')

# 定义登录函数
def login(username, password, code1):
    if code1.lower() == code.lower():
        if username == 'xy' and password == '123':
            print('登录成功')
        else:
            print('用户名或密码有误')
    else:
        print('验证码输入错误')

        
login(username, password, code1)


# global 声明全局变量
'''函数内部声明的变量  局部变量
声明在函数外是全局的，所有函数都可以访问
函数内能用外面的变量，要修改的 则在函数内声明 global 变量。
全局变量是不可变的，在函数中对它操作时 加global
        可变的，在函数中对他操作时不需要加
'''
name='月月'
list1=[1,2,3,4]
def func1(*x):
    name='西瓜'
    print(name)
func1() # 用函数自己的name    西瓜

def func2():
    global name
    name+='好小'
    print(name)
    list1.append(5)# 列表是可变的，不需用global来声明
    print(list1)
func2()# 用函数外面的变量，要修改的话，使用global