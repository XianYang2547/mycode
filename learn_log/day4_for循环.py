'''
for 循环
结构：
	for 变量名 in 集合:
		语句
	for x in xrange(1,10):变量x 以及范围
	pass
'''
#使用系统给定rangr（）完成范围指定  range（n）----->0到n-1  range(m,n) m--->n-1
for i in range(1,23,3):
	print(i)#1--22,步长为3   1 4 7 10 13 16 19 22
for i in range(10,1,-3):
	print(i)#步长为负
print(range(8))  # range(0, 8) 包含0 不包含8  0 1 2 3 4 5 6 7
# 打印3次hello
for i in range(3):
	print('hello------>',i)#i取0时打印一个hello，取1 取2
#循环吃5个馒头
for x in range(5):
	print('某某正在吃第{}个馒头'.format(x))
# 某某正在吃第0个馒头
# 某某正在吃第1个馒头
# 某某正在吃第2个馒头
# 某某正在吃第3个馒头
# 某某正在吃第4个馒头

for x in range(5):
	print('某某正在吃第{}个馒头'.format(x+1))
# 某某正在吃第1个馒头
# 某某正在吃第2个馒头
# 某某正在吃第3个馒头
# 某某正在吃第4个馒头
# 某某正在吃第5个馒头
# for x in range(1,6):
# 	print('某某正在吃第{}个馒头'.format(x))  #等价于上面x+1

##不吃第三个
for i in range(1,6):
	if i==3:
		print('不吃第三个')
	else:
		print('某某正在吃第{}个馒头'.format(i))

#指定范围批量打印
for i in range(8,15):
	print('hello------>',i)



#### for ...else
   # else 适用于for执行完或者没有循环数据时，需要做的事
# for i in 范围:
# 	有数据时，执行这部分语句
# else：
#  	没有数据执行
#pass 空语句


num=int(input('请输入你要干几碗饭'))
for i in range(num):
	print('正在干第{}碗饭'.format(i+1))
else:
	print('我没有饭干了')
print('---------------')

if 10>7:
	print('10比7大')
else:
	pass
#else 的内容不知道写啥的时候，填pass
print('---判断结束---')

## 用户的账户密码登录且只能登录3次，三次未成功就锁定
for i in range(3):
	username=input('请输入账号：')
	password=input('请输入密码：')
	if username=='xianyang' and password=='123456':
		print('登录成功！')
		print('请充钱')
		break#跳出循环，for对应的else语句也不执行
	else:
		print('账户或密码有误！')
else:
	print('账户被锁定')
# 乘法表
for i in range(1,10):
	for j in range(1,i+1):
		print('{}*{}={}'.format(i,j,i*j),end=' ')
	print()