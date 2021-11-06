#list 列表   [] 存放字符 数字等
names=['sb1','sb2','sb3','sb4','sb5','sb1']
		#  0	 1	 2		3	  4
		# -5	-4	 -3	   -2	 -1
print(names[0],names[-1])#获取里面的元素
print(len(names))#找列表元素的个数

for i in names: #列表也支持遍历
	print(i)

#改其中 某个元素
names[2]='SB33'# z找到要改的那个元素，赋值修改
print(names)
print('*'*35)


#不知道元素在列表的位置时，用for
for i in range(len(names)):
	#i是0 1 2 3 .。。
	if 'sb5' in names[i]:
		names[i]='SB55'
print(names)
print('*'*35)


for i in range(len(names)):
	if names[i]=='sb5':
		names[i]='SB55'
print(names)
print('*'*35)


mm=['1','2','3','4','5']
#删其中 某个元素
l=len(mm)
i=0
while i<l:
	if mm[i]=='3':
		del mm[i]
		l-=1
	i+=1
print(mm)
print('*'*35)

