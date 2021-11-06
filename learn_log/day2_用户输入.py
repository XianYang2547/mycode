#   day2   input() 输入（的都是字符串类型）
help(input)
#name=input('请输入你的名字：')
#print(name)
'''
练习：
游戏：捕鱼达人
输入参与游戏者的用户名
输入密码
充值：500
'''

# print('''
# ***************
#     捕鱼达人
# ***************
# 	''')
# username=input('请输入参与游戏者的用户名：')
# password=input('请设置你的密码：')
# print('你需要充值才能开始游戏')
# coins=input('请输入充值的金额：')
# #print('充值成功，你当前的游戏币为：{}' .format(coins) )
# money=int(coins)
# print('充值成功，你当前的游戏币为：%d' %money )
# print('游戏结束，欢迎下次再来' )


#赋值运算符  1. =号
name='admin'
name1=name
print(id(name),name)
print(id(name1),name1)#
#id() 查看变量的地址
print(id(name)==id(name1))
#扩展后的赋值符号  +=  -= *= /=
num=8
num+=5
print(num)#数学加号,先加 再等于
a='abc'
a+='def'
print(a)#字符串时，相当于连接
# a-='def'
# print(a) 字符串不能-= *= /= 


#+-*/运算符  扩展的算数运算符**幂运算  //整除   %取余
a=9
b=3
result=a*b
print(result)
result=a/b   # 9/3  结果是3.0
print(result)
result=a**b#  a的b次方。。9的3次方
print(result)
result=a//b #a整除b  9整除3  结果是3   9//2结果为4
print(result)
result=a%b  #求余 余数为0
print(result)
# 2421987168
# 97465635
# 邮箱辅助账号xy_mts@qq.com(1908346792) 邮箱独立密码xxqq2547   过去密码：chongzi.  
# 邮箱辅助账号android12345@qq.com（2421987168）邮箱独立密码xxqq2547过去密码：zhongxiang418 xxqq2547 xiangyang4569 12345678.