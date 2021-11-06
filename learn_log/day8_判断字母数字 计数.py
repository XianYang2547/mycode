# 判断字符串里有没有数字 字母
# isalpha() 是否是字母  isdigit()是否是数字
s='sdaslkfhdsiof'
result=s.isalpha()
print(result)#判断字符串是不是字母 返回true  false

s='1234861234'
print(s.isdigit())

'''
计算3次输入的数字和,当输入的不是数字时，次数不变，只有输入数字才会扣除你的输入次数
必须是输入数字，输入其他的则要求重新输入
'''
count=3
s=0
while count>0:
	i=input('输入一个数：')
	if i.isdigit():
		i=int(i)#
		s+=i
		count-=1
	else:
		print('请重新输入一个数')
	
print(s)

try:
	i=1
	for i in range(5):
		print(10/i)
except:
	print('出错了')

###猜数游戏
import random
num=random.randint(1,1000)
count=0
while True:
	try:
		s=eval(input('请输入你要猜的数(1-1000)：'))
	except:
		print('请输入数字')
		#continue  #输入的不是数字 则返回重新输入，次数不增加
	else:
		count+=1
		if s>num:
			print('猜大了')
		elif s<num:
			print('猜小了')
		else:
			print('猜对了')
			break
	
print('你猜了{}次'.format(count))
