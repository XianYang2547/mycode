
# s=['hello','good','word','digit','alpha']#列表[]里可以放字符串整型浮点型
# print(s)
# x=input('输入hello，在s中删掉：')
# i=0
# l=len(s)
# while i<l:##################因为删除后总长度要减少，用for长度是固定的，所以用while
# 	if 'hello' in s[i]:
# 		del s[i]
# 		l-=1
# 	i+=1
# print(s)
# print('*'*20)


# 漏删的情况
s=['word','good','gooo','hello','digot','phah','0sd']
print(s)
w=input('请输入一个单词,以便于在s中删掉')
l=len(s)
i=0
while i<l:
	if w in s[i]:          ##用in  输入的不一定等于列表中的，可以是一部分，如果用== 单词就要完全匹配才能删除
		del s[i]
		l-=1
		# continue #删除一个 字符串总长减1，而i值继续增加，若两个连续的单词需要删除，就会出现漏删
		#加上continue后，长度减1，i值先不计数
	i+=1
print(s)



# ####列表的切片（截取的结果也是一个列表）
y=['hello','good','word','digit','alpha']
#	 0		 1		 2		3		 4
#	 -5		 -4		 -3		-2		 -1
#跟字符串切片差不多



####列表的添加 append  									11111111111111111111111111111
#往空列表里添加数字，按Q推出
# XX=[]
# while 1:
# 	num=input('输入数字：')
# 	if num =='q':
# 		break
# 	else:

# 		XX.append(num)# xx.append() [append 是往列表后面追加数据]

# 	print(XX)


###### extend 列表的合并（一次添加多个元素） 也可以用 +号	2222222222222222222222222222
# names1=['张三','隶属函数']
# names1.extend(y)# 把列表y加到列表name1 里面
# print(names1)#['张三', '隶属函数', 'hello', 'good', 'word', 'digit', 'alpha']


#### insert  指定位置插入									33333333333333333333333333333333333333333
y=['hello','good','word','digit','alpha']
y.insert(1,'python')
print(y)

#insert(位置，‘要插入的内容’)





'''
产生10个随机数，将其保存到列表中
'''
import random
s=[]
for i in range(10):
	x=random.randint(1,10) #范围小的话，产生的随机数相同的概率就大
	s.append(x)# 		XX.append(num)# xx.append(x) [append 是往列表后面追加数据]
print(s)
####思路：产生一个范围的随机数，使用循环产生10个，每产生一个数，把它加到列表中去


##产生10个不同的随机数，将其保存到列表中
import random
s=[]
i=1
while i<=10:
	x=random.randint(1,10) 
	if x not in s: #如果产生的随机数不在s列表里，就把它加入进去，同时i加1
		s.append(x)
		i+=1
	# else:
	# 	del 	#如果产生的随机数在s列表里，就删掉，i值不变
	# 	i=i 	#可以不要这两行 或者else： pass
print(s)

#  s 是列表
####给一个列表排序sorted   升序  大小 max min
print(sorted(s),max(s),min(s))
####sorted(s)---->升序
####sorted(s,reverse=True)  --->降序
print(sorted(s,reverse=1))


