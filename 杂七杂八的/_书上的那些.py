# # #3-1
# # names=['bob','python','c++','java']
# # for i in names:
# #     print(i)
# # #3-2
# # for i in range(len(names)):
# #     print(names[i].title()+' hello')
# # #3-3
# # go_out=['walking','running','bick0','car']
# # for i in range(len(go_out)):
# #     print('I like to go out by '+go_out[i].title())
# # print('*'*20)
# # #3-4
# # name=['bob','python','c++','java']
# # print(name[0]+' please eat dinner')
# #
# # #3-5
# # name[2]='sex'
# # print('c++无法赴约')
# # print(name[0]+' please eat dinner') #name[0 1 2 3]
# # #3-6
# # print('i found a large table')
# # name.insert(0,'111')
# # name.insert(3,'111')
# # name.append('333')
# # print(name)
# # #3-7
# # print(' only 2 person can eat dinner')
# # for i in range(len(name)):
# #     w= name.pop()
# #     print(w+' i am sorry,you are pass')
# #     if len(name)==2:
# #         break
# # print(name)
# # for i in name:
# #     print(i+' you can eat')
# #
# #
# # #4-8
# # lifang=[]
# # for i in range(1,11):
# #     lifang.append(i**3)
# # print(lifang)
# #
# # #列表解析
# # lifang=[i**3 for i in range(1,11)]
# # print(lifang)
# #
# # #5-11
# # nums=[1,2,3,4,5,6,7,8,9]
# # for num in nums:
# #     if num==1:
# #         print(str(num)+'st')
# #     elif num==2:
# #         print(str(num)+'nd')
# #     elif num==3:
# #         print(str(num)+'rd')
# #     else:
# #         print(str(num)+'th')
# # while 1:
# #     x=input('输入')
# #     if x!='quit':
# #         print(x)
# #     else:
# #         break
# # mag=['魔术师1号','魔术师2号','魔术师3号']
# # def show_magicians(magicians):
# #     for magician in magicians:
# #         print(magician)
# # show_magicians(mag)
#
# # mag=['魔术师1号','魔术师2号','魔术师3号']
# # new_make_great=[]
# # def make_great(magicians):
# #
# #     while magicians:
# #         ss=magicians.pop()
# #         ss='the great '+ss
# #         new_make_great.append(ss)
# # make_great(mag[:])#使用列表的副本
# # print(new_make_great)
# # print(mag)
#
# # def pizze(*xda):
# #     print(xda)
# # pizze('apple','photo')
# #
# # def car_informations(shop,data,**xda):#**xda接受输入的值对 信息
# #     informations={}
# #     informations['shop']=shop
# #     informations['data']=data
# #     for key,value in xda.items():
# #         informations[key]=value
# #     return informations
# # car=car_informations('bmw','2018',color='blue',price='cheep')
# # print(car)
# # class restaurant(): #创建一个类  修改里面的值，让他递增
# #     def __init__(self,restaurant_name,restaurant_type): #包含里面2个属性
# #         self.restaurant_name=restaurant_name
# #         self.restaurant_type=restaurant_type
# #         self.number_served=0
# #         #定义了2个函数
# #     def describe_restaurant(self):
# #         print('this restaurant name is '+self.restaurant_name,'and it type is '+self.restaurant_type )
# #     def open_restaurant(self):
# #         print('正在营业')
# #     def eat_number(self,num):
# #         self.number_served=num
# #         # print('目前有'+str(self.number_served)+'人就餐过')
# #     def now_number(self,num):
# #         self.number_served+=num
# #     def total_number(self):
# #         print('目前有'+str(self.number_served)+'就餐')
# #
# # my_res=restaurant('世宏小炒','五星级')#根据类 创建了一个实例，保存在my _res中
# # print('restaurant name is '+str(my_res.restaurant_name) )
# # print('restaurant type is '+str(my_res.restaurant_type))
# # #调用里面的函数
# # my_res.describe_restaurant()
# # my_res.open_restaurant()
#
# # #修改就餐人数
# # my_res.eat_number(50)
# # my_res.total_number()
# # my_res.now_number(20)
# # my_res.total_number()
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.login=0
#     def increase(self):
#         self.login+=1
#     def decrease(self):
#         self.login-=self.login#直接减去本身置0
#     def show(self):
#         print('login的值 ',self.login)
#     def describe_user(self):
#         print('user name is '+self.first_name+self.last_name )
#     def greet_user(self):
#         print('hello '+self.first_name)
# my_user=User('xian','yang')
# # my_user.describe_user()
# # my_user.greet_user()
# my_user.increase()
# my_user.show()
# my_user.increase()
# my_user.show()
# my_user.increase()
# my_user.show()
# my_user.decrease()
# my_user.show()
# # my_user.decrease()
# # my_user.show()
# # my_user.decrease()
# # my_user.show()#递增然后递减
# class Privileges():
#     def __init__(self,privileges=['you are sexy','you are crazy']):
#         self.privileges=privileges
#     def show_privileges(self):
#         print('管理员权限')
#
# class Admin(User):#继承上面的类
#     def __init__(self,first_name,last_name):
#         super().__init__(first_name,last_name)
#         self.privileges=Privileges()
#
# admin=Admin('xian','y')
# admin.privileges.show_privileges()
#
#
#
# class Car():
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印汽车的里程"""
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """将里程表读数增加指定的量"""
#         self.odometer_reading += miles
#
# #继承
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """ 初始化父类的属性"""
#         super().__init__(make,model,year)
#         self.batteryt_size=72
#     def describle_battery(self):
#         print('电瓶大小为：'+str(self.batteryt_size))
#         # return self.batteryt_size
#
# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_descriptive_name())
# print(my_tesla.describle_battery())
#
#
# #导入随机数模块 定义一个类  定义一个方法 生成一个范围内的随机数，---骰子   扔10次
# from random import randint
# class Die():
#     def __init__(self,sldes=6):
#         self.sldes=sldes
#     def roll_die(self):
#         print(randint(1,self.sldes))
# my_Die=Die(10)
# for i in range(10):
#     my_Die.roll_die()
#
#
# class Employee:
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("雇员的数量为：", Employee.empCount)
#
#     def displayEmploe(self):
#         print("姓名：%s  工资：%f" %(self.name,self.salary))
#
# emp1 = Employee("zhangsan",23.5)
# emp1.displayEmploe()
# emp1.displayCount()
# emp2 = Employee("lisi",89.88)
# emp2.displayEmploe()
# emp2.displayCount()
#
# with open('123.txt','w') as f:#打开文件 没有就创建
#     f.write('i love pytgon\n')#写入不堪入目的的东西
#     f.write(str(123456))
#
# with open('123.txt') as f:#打开文件开始读取
#     for i in f:
#         print(i.strip())#去除空白
#
# # import math
# # import time
# # scale=10
# # print("执行开始")
# # t=time.process_time()
# # for i in range(scale+1):
# #     a,b='**'*i,'..'*(scale-i)
# #     c=(i/scale)*100
# #     π=4*(4*math.atan(1/5)-math.atan(1/239))
# #     print("[{}{}->%{}]".format(a,b,c))
# #     time.sleep(0.1)
# # print(π)
# # print("程序用时：{:.2f}s".format(t))
# # print("执行结束")
#
#目标 把txt里的值输出成 Π  3.144564987441567413416576854
with open('pai_value.txt') as file_object:
    lines=file_object.readlines()#readlines 读取每一行 将其储存到列表里  lines是个列表
for line in lines:
    print(line.strip(),end='')#打印初每行

#以上不方便计算出长度
# 建一个空字符串，遍历一次 就加到里面去，再去除空格 再计算长度
print()
# 169页 作业
with open('pai_value.txt') as f:
    #打印方法1 直接读取完全部打印
    # x=f.read()
    # print(x)
    #打印方法2 打开文件后遍历
    # for i in f:
    #     print(i.strip())
    #打印方法3 把读取的内容存为列表，在其他地方打印
    things=f.readlines()
for i in things:
    print(i.strip())

#172 作业
# def get_name():
#     name=input('输入名字，以便于存放：\n')
#     with open('guest.txt','w') as f:
#          f.write(name)
# get_name()

# while 1:
#     name=input('输入名字')
#     if name=='q':
#         break
#     print('欢迎{}大佬'.format(name))
#     with open('guest_book.txt','a') as f:#a追加 不覆盖之前的记录
#         f.write('{}\n'.format(name))

# while 1:
#     print('你在干什么？')
#     thing=input('输入你目前做的事:')
#     if thing=='q':
#         break
#     with open('do_things.txt','a') as f:#a追加 不覆盖之前的记录
#         f.write('{}\n'.format(thing))

###异常处理，常发生在用户输入的时候
# while 1:
#     try:
#         num1=int(input('\n输入一个数：'))
#         num2=int(input('\n输入第二个数：'))
#         ans=num1/num2
#     except:
#         print('请不要输入0或其他字符')
#         get=input('按q退出...'
#                   '键入其他的可继续运算：')
#         if get=='q':
#             break
#     else:
#         print('{}除以{}的结果是\n{}'.format(num1,num2,ans))
## 依赖于try 中的代码块成功执行的代码 放到else中


####输入一个东西，创建一个json文件，把它存入。再导入，读取它
# import json
# f_number=input('输入一个东西：\n')
# with open('num.json','w') as f:
#     json.dump(f_number,f)
#
# with open('num.json') as f:
#     xx=json.load(f)
#     print(xx)

# import json
# def numm():#如果存储了一个字符，就显示出来，要是没有存入的话，就提示输入一个
#     try:
#         with open('num.json') as f:
#             xx=json.load(f)
#     except:
#         print('没找到，请重新存入')
#         f_number=input('输入一个东西：\n')
#         with open('num.json','a') as f:
#             json.dump(f_number,f)
#             print('存入成功')
#     else:
#         print(xx)
# numm()























