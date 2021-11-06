### enumerate()
#用于将一个可遍历的数据对象（如列表 字符串 元组） 组合成一个索引序列
#同时列出数据和数据下标，一般用在 for 循环当中。
#enumerate(可遍历的对象，start=0 )，位置从0 开始，也可以从1开始
ss=['a','bbb','ccc','gg']
for index,value in enumerate(ss):
	print(index,value)##index 下表，value
'''
0 a
1 bbb
2 ccc
3 gg
'''
list1=['1','2','3','4']
str1='1'
for index,value in enumerate(list1):
	list1[index]=str1+value#批量修改列表内的元素
print(list1)#['11', '12', '13', '14']


########################排序
number=[8,5,9,7]
for i in range(len(number)):#i从0到3  range（4）--> 0 1 2 3
	for j in range(i+1,len(number)):#j从1到3 range（1，4） -->1 2 3
		if number[i]>number[j]:
			number[i],number[j]=number[j],number[i]
print(number)
'''冒泡排序：第一轮for循环 取第一个i=0，然后进入下一个for循环，j=1 2 3用那一个依次跟后面的比较，
								  number[i]依次和number[j]比较，i不变，j递增
								  比他小的就交换位置，
			第二轮for循环 取第二个i=1，然后进入下一个for循环，j=2 3  ，，，

'''



