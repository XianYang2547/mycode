##   ' '.join() 连接一些字符  '' 间可随意指定符号
new_str='-'.join('abc')# 用-连接abc   
print(new_str)#a-b-c

list1=['a','b','c','o','9']
result=' '.join(list1)#用空格连接
print(result)#a b c o 9


##  lstrip rstrip strip  去除字符串左边 右边  左右两边的空格
s='   111hello111   '
s1=s.lstrip()
print(s1)

s2=s.rstrip()
print(s2)

s3=s.strip()
print(s3)
'''				111hello111   
				   111hello111
				111hello111
'''

# split() 分割字符串  
s='hello world hello kitty'
print(s.split(' '))#以空格分隔，取出4个单词
#结果输出到数组中 ['hello', 'world', 'hello', 'kitty']


print(s.count(' '))#求s字符串中空格的个数 ***s.count('o'),求o的个数

'''练习：
1.输入一行字符，统计有多少个单词 每2个单词之间以空格隔开

2.输入两个字符串，从第一字符串中删除第二个字符串中所有的字符
'''
#法1
# s1=input('字符串1：')
# s2=input('字符串2：')
# for i in s1:
# 	if (i in s1) and (i in s2):
# 		s1=s1.replace(i,'')
# print(s1)
#法2
# s1=input('字符串1：')
# s2=input('字符串2：')
# for i in s2:
# 		s1=s1.replace(i,'')
# print(s1)

'''
							字符.upper()  .........
大小写： upper() lower()		
查找：find()
替换：replace(old,new)
分割：	split('分割符')
个数：count() 	统计x的个数  xxx.count('x')
连接： join()
编码： indoce() decode()
去空格：strip() lstrip() rstrip()
用于判断：	startwith() 判断是不是以  开头
			endswith() 判断是不是以  结尾
			isalpha() 判断是不是字母
			isdigit() 判断是不是数字
'''

