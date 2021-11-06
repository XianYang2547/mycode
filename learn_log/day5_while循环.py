#while
for i in range(1,11):
	print(i)#打印1-10

i=1
while i<=10:
	print(i)
	i+=1   #i的值要增加，否则进入死循环
print('*'*20)
##打印1-30之间3的倍数
i=0
while i<=30:
	if i%3==0 and i!=0:
		print(i)
	i+=1
print('*'*20)

i=1
while i<=30:
	if i%3==0:
		print(i)
	i+=1
print('1111111111111111')
i=3
while i<=30:
	print(i)
	i+=3
print('*'*20)
#打印1-30中 是3的倍数也是5的倍数
i=0
while i<=30:
	if i%3==0 and i%5==0 and i!=0:
		print(i)
	i+=1#等于i=i+1
print('*'*20)
'''
使用while循环计算1：20的累加和

'''

i=1
s=0
while i<=20:
	s=s+i
	i=i+1
print(s)

#####用while和 for 打印**层数  x=0和x=1皆可
i=int(input('输入层数'))
x=0
while x<=i:
	print('*'*x)
	x+=1


i=int(input('输入层数'))
x=0
for x in range(i+1):
	print('*'*x)
	x+=1


#whlie 嵌套
ceng=1
while ceng<=5:
	count=1
	while count<=ceng:
		print('*',end='')
		count+=1
	ceng+=1
	print()

##打印乘法表
i=1
while i<=9:
	j=1
	while j<=i:
		print('%s*%s=%s\t'%(i,j,i*j),end='')
		j+=1
	i+=1
	print()

	
for i in range(1,10):
	for j in range(1,i+1):
		print('%s*%s=%s\t'%(j,i,i*j),end='')
	print()

for x in range(1,10):
	j=1
	while j<=x:
		print('%s*%s=%s\t'%(j,x,x*j),end='')
		j+=1
	print()


#pass   break结束循环    continue 跳过循环体中下方的语句不执行，直接进行下一次循环
#

#1-10不是3的倍数的数累加
s=0
for i in range(1,10):
	if i%3!=0:
		s=s+i
print(s)

for i in range(1,10):
	if i%3==0:
		continue
		s=s+i
print(s)
