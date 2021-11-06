#字典
# 符号{}，关键字dict，保存的元素是  key：value
'''
列表		元组		字典
[]		()		{}
list	tuple	dict

'''
#建空字典,2个方法
dict1={}
dict2=dict()

dict3={'id':'511231254666','name':'yasou'}

#列表可转成字典，列表中的元素要成对出现
dict4=dict([(1,2),(3,4),(4,5),(7,8)])
print(dict4)

###字典的增删改
#增加：		dict[key]=value
dict5={}
dict5['name']='bob'#加入 name:bob  如果key和原来的相同，则会把value替换了
print(dict5)#{'name': 'bob'}
#dict5是这样的  {'name': 'bob'}
dict5['name']='bobbob'#把原来的值覆盖了
print(dict5)#{'name': 'bobbob'} 

'''
写一个注册系统，能保存用户的信息
# '''
# data=[]
# while 1:
# 	s={}
# 	username=input('输入用户名：')

# 	password=input('输入密码：')
# 	repassword=input('确认密码：')
# 	s['username']=username
# 	if password==repassword:
# 		s['password']=password
# 	else:
# 		print('密码不一致')
# 		continue# 就不执行下面这些语句了

# 	email=input('输入邮箱：')
# 	phone=input('输入电话：')
# 	s['email']=email
# 	s['phone']=phone
# 	data.append(s)
# 	answer=input('是否继续y/n：')
# 	if answer!='y':
# 		break

# print(data)#循环一次保存一条用户信息到字典里，再添加到data列表中，循环多次则保存多条字典信息




''' 增加元素 （key：value）
dict[key]=value---->{key:value}
key 在字典里是唯一的，value值可以不唯一
和列表对比
列表 list1=[]  list1.append(??)
字典 dict={}   dict1[key]=value

	修改元素
	dict1[key]=newvalue
	查询元素
	dict1[key]---->找到value

	'''
dict6={1: '傻逼', 3: '幺儿', 4: '删掉', 7: 'sdasda'}
print(dict6[3])#幺儿  根据key就找到对应的value


'''#字典里的函数：拿字典去.
items() 将字典的键值对转成列表保存的形式
 values()  取出字典里所有value，保存到列表中
  keys() 获取键值对所有得key

#找出这几个同学中成绩大于80分的名字  items()'''
'''法1'''
dict7={'张三':'55','李四':'74','王五':'85','赵六':'90'}
for i in dict7:#遍历字典时，拿到的是key  i就是 张三李四...
	if dict7[i]>'80':
		print(i)
print('*'*10)
'''法2'''
dict7={'张三':'85','李四':'89','王五':'91','赵六':'99'}
for key,value in dict7.items():#items 将字典的键值对转成列表保存的形式
	if value>'90':			#[(key,value),(key,value),(key,value)...]
		print(key)			#把(key,value)对应赋给  key,value 拆包
print(dict7.values())#(['85', '89', '91', '99'])
					#  .values() 把所有值取出来
print('*'*30)
#求平均分 values() 
zongfen=0
socre=dict7.values()#把所有分数取出来
for i in socre:#遍历要取得每个值
	zongfen+=int(i)#计算总分
average=zongfen/len(dict7) #求平均分
print(average)


print(dict7.keys())#取所有的key （名字）
#获取了就可以遍历了
for i in dict7.keys():
	print(i)

print('*'*30)
#根据key获取值
print(dict7['李四']) # --->89 没有要找的key会报错
#用get获取值
print(dict7.get('李四'))#--->89 找不到李四对应的值不会报错，返回none
	#dict7.get('李四'，default)	#能取到值，就取。若没有，可以返回一个默认值


###						删除 通过key来删除
dict7={'张三':'85','李四':'89','王五':'91','赵六':'99'}
del dict7['张三']  #要是没有那个key时 删除就会报错
print(dict7)


dict7={'张三':'85','李四':'89','王五':'91','赵六':'99'}
#用这个来删除 list1.pop(key)
#根据key删除字典里的键值对，删除成功了返回的是对应的value 
#pop()里除了key 还可以加默认值，如果删除的时候没有找到键，可以用默认值来充当提示
result=dict7.pop('李四')
print(result)# 返回的李四的value  89
print(dict7)#{'张三': '85', '王五': '91', '赵六': '99'}

s=dict7.pop('傻批','没有此键')
print(s)
print('*'*30)


############popitem()  随机删除键值对（一般是从末尾删除
dict7={'张三':'85','李四':'89','王五':'91','赵六':'99'}
result=dict7.popitem()
print(result) #看看删了谁  把赵六删了
print(dict7)#打印删了后的字典
print('*'*30)


################ 把2个字典并成一个  update()
dict8={1:'11',2:'22',3:'33'}
dict9={1:'000',4:'44'}
dict8.update(dict9)#
print(dict8)#{1: '000', 2: '22', 3: '33', 4: '44'}
print('*'*30)

############fromkeys(??)   将？？转成字典的形式，如果没有指定默认的value则用none
#							如果指定默认值，就用默认值代替
list0=['name','tall','hight']
new_dict=dict.fromkeys(list0)
print(new_dict)#{'name': None, 'tall': None, 'hight': None}


new_dict=dict.fromkeys(list0,10)
print(new_dict)#{'name': 10, 'tall': 10, 'hight': 10}


