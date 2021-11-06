# == 比较的是内容，is 比较的是地址
s1='abc'
s2="abc"
s3='''
abc
'''
print(id(s1),id(s2),id(s3))
print(s1==s2)
print(s1 is s2)
print(s2==s3)
print(s2 is s3)
##三引号的内容在一行时，地址一样

#[]     通过[]可以结合位置 获取字母
#  p  i  c  t  u  r  e  .  p  n  g
#  0  1  2  3  4  5  6  7  8  9  10
filename='picture.png'
print(filename[5])
print(filename[0:7])#从0开始 picture
#[start:end] 类似于range（） range(0,10) [0:10]   0 1 ....9
print(filename[1:])#冒号后省略则取到结束
print(filename[:7])#冒号前省略，从0开始取

print(filename[::-1])#字符串取反 --->gnp.erutcip
print(len(filename))


###字母大小写
#capitalize()
message='yasuO is a gU er!'
mes=message.capitalize() #把字符串第一个 转成大写的形式
print(mes)               #Yasuo is a gu er!

# title() 
mes=message.title()      #把每个单词的首字母大写
print(mes)               #Yasuo Is A Gu Er!

#upper
mes=message.upper()      #将字符串全部转成大写
print(mes)               #YASUO IS A GU ER!

#lower
mes=message.lower()      #将字符串全部转为小写
print(mes)               #yasuo is a gu er!

'''
验证码产生
产生4个随机数
'''
s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
import random
code=''
for x in range(4): #产生一个4位数的验证码

	n=random.randint(0,len(s)-1)#从字符串s里随机产生一个
	code+=s[n]#[]从s中取随机数对应的值						#		每次串联一个字符

print(code)

#while 方法
# yanzhengma=''
# i=1
# while i<=4:
# 	n=random.randint(0,len(s)-1)
# 	yanzhengma+=s[n]
# 	i+=1
# print(yanzhengma)


user_input=input('输入验证码')
if user_input.lower()==code.lower():#把输入的字符和系统的字符统一转成小写
	print('验证通过')
else:
	print('失败')


