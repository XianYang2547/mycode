#集合 set  无序的不重复的  {}
s1=set()
s2={}	#{元素1，元素2，元素3}
#可用来去除重复项，比如说生成随机数去重
#把一个列表往set(list)扔


#1.。。。#################  add()添加一个元素到集合中
s1.add('野猪佩奇')
s1.add('123')
s1.add('yasuo')
print(s1)#不是按顺序添加的
##################  update() 添加多个元素
						#可把要添加的多个元素扔在列表 元组里
l=['pp','ll','lk']
s1.update(l)
print(s1)
print('*'*19)
#2.############### s.remove(??)  s.pop()  s.claer() 
s1={'123', 'lk', 'll', '野猪佩奇', 'pp', 'yasuo'}
s1.remove('123')# 使用remove删的时候，若有那个元素就删，若没有，会报错
print(s1)

################# discard(**) 移除不存在的元素时不会报错
#			s1.discard(**)
#生成10个不重复的数
import random
s2=set()
i=0
while i<50:
	ran=random.randint(1,20)
	s2.add(ran)
	if len(s2)==10:
		break
	i+=1
print(s2)
# #输入一个数字 从s2中删掉它
# num=int(input('输入一个数字'))
# s2.discard(num)
# print(s2)
print('*'*19)

##########   交集 并集  差集#########

set1={1,2,3,5}
set2={1,2,3,5,6,7}

set3=set2-set1	 
print(set3)#{6, 7}
set4=set2.difference(set1) #差集
print(set4)#{6, 7}
print('*'*19)

set5=set2 & set1
print(set5)
set6=set2.intersection(set1) #交集
print(set6)
print('*'*19)

set7=set2 | set1
print(set7)
set8=set2.union(set1)		#并集
print(set7)
print('*'*19)
'''
已知两个列表：
l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]
找出两个列表的不同元素
找出共同元素'''
l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]
l1=set(l1)#转成集合
l2=set(l2)
print(l1.difference(l2))
print(l1.intersection(l2))
print('*'*19)


#不可变类型：int str float tuple
#对象所指向的内存中的值是不可以改变的

#可变类型：dict list
#对象所指向的内存中的值是可以改变的













