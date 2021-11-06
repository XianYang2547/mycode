#字符串的查找 替换
# find() 
#find('要查找的字符'，start，end) 
#rfind()  right find 从字符串右边开始找
s1='index lucy lucky goods'
result='x' in s1 #看看x 是否在s1里面
print(result)

position = s1.find('r')#位置=。。。 返回值是-1 代表没有找到
print(position)

position = s1.find('l')#能找到的话 返回它第一次出现的位置
print(position)

position=s1.find('l', position,len(s1))#从指定位置开始查找
print(position)

ur1='https://i1.hdslb.com/bfs/face/a326fa.png'
position=ur1.rfind('/')#从右边开始找 /
print(ur1[position+1:]) #打印出ur1字符串中 / 后面的所有字符 位置+1(不包括/的位置)

#index ( 要查找的内容，start，end=len(s1))
#跟find一样，找不到的话find报 -1 而index报异常【substring not find】

#replace() 替换
#replace('旧的','新的','替换多少个')
s1='index lucy lucky goods'
s2=s1.replace(' ','#') #把空格换成#
print(s2)
s3=s1.replace(' ','')#把空格换成。。。去掉空格
print(s3)

###encode编码   decode解码
message='我操，好多好多野鸭子!!!'
result=message.encode('utf-8')#默认是utf-8
print(result)
mm=result.decode('utf-8')
print(mm)


### startswith()  endswith()
### p判断是否以xxx开头 或者 结尾  返回true false
#文件上传，只能上传固定格式 jpg png等等
filename='笔记.doc'
result=filename.endswith('doc' or 'jpg')#
print(result)

s='qqwweerrttt'
kaitou=s.startswith('Q')#区分大小写，也能判断qqww
print(kaitou)

'''

文件上传  输入你的路径，再判断是否是相应的格式
先找到位置，切片找到文件名 再判断
'''
#https:C:sers\faultuser0\AppData\LocalLow.png等等
filename=input('输入你要上传文件的路径：')
position=filename.rfind('\\')#路径里是、\*\*\*\*  \\转义一下
file=filename[position+1:]
print(file)
if file.endswith('png'):
	print('上传成功')
else:
	print('上传失败，不是相应的格式')


'''
上传一个文件，只能上传格式为txt或png或jpg得文件
如果上传错了，允许重新上传，符合上传规则则上传成功
'''
while True:
	filename=input('输入路径选择文件：')
	possion=filename.rfind('\\')
	wenjianming=filename[possion+1:]
	if wenjianming.endswith('txt') or wenjianming.endswith('png') or wenjianming.endswith('jpg'):
		print('允许上传')
		break
	else:
		print('请重新选择')










