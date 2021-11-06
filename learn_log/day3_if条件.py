#  day3  and  or  not
a=3
print(bin(a))#结果是0b11  把10进制转为2进制
b=0b10111
print(int(b))#结果是23  把2进制转为10进制  二进制前面用0b  开头

#如果年龄大于18并且输入了名字，则打印xxx今年xxx岁了 必须完全符合条件才能进行下一步
while True:
	age=int(input('输入年龄'))
	username=input('输入名字')
	if age>18 and username:
		print('{}今年{}岁了'.format(username,age))
		print('进入下一环节')
		break
	# else:
	# 	age=int(input('重新输入年龄'))
	# 	if age>18 and username:
	# 		print('{}今年{}岁了'.format(username,age))
	# 		print('进入下一环节')

# import random
# print(random.randint(1,10))#产生1-10的随机数

# rand =str(random.randint(1,10))
# guess=input('输入一个数1-10:')
# if rand==guess:
# 	print(rand,'猜对了')
# else:
# 	print(rand,'猜错了')

#if elif 多个条件判断
# age=int(input('输入一个年龄：'))
# if age<=18:
# 	print('小了')
# elif age>18 and age<=25:
# 	print('差不多')
# elif age>25:
# 	print('太老了')
'''
if 条件:
	语句
------------
if 条件:
	语句
else:
	语句
-------------
if 条件1:
	if 条件2:
		语句
	else
		语句
else：
	语句
--------------
if 条件1:
	语句
elif 条件2:
	语句
elif 条件3:
	语句
'''