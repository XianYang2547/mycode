import re

#使用正则模块方法 match
s='岁月为笔相思入墨岁月为笔相思入墨'
result=re.match('相思',s)#match匹配 从字符串开头匹配，匹配不到返回none
print(result)

#使用正则模块方法 search   有一个匹配的，就不往下找了
result=re.search('相思',s)#search进行正则字符串匹配方法，匹配整个字符串
print(result)#<re.Match object; span=(4, 6), （span匹配的位置）match='相思'>
result.span()#返回位置
result.group()#返回内容
print(result.span(),result.group())

#用re.findall来找全部满足正则内容的  找完了把结果放在列表中
result=re.findall('相思',s)
print(result)
#########################################################################
#给出正则，检测一个数字
s='哈哈5'
result=re.search('[0-9]',s)#搜索0-9之间的数
print(result)#<re.Match object; span=(2, 3), match='5'>

#给出正则，检测2个数字
s='哈哈59'
result=re.search('[0-9]+',s)#搜索0-9之间的数   这个也可以[0-9][0-9]
print(result)#<re.Match object; span=(2, 4), match='59'>

#给出正则，检测1个数字和1个字母
s='哈哈5s9'
result=re.search('[0-9][a-z]',s)#搜索0-9之间的数
print(result)#<re.Match object; span=(2, 4), match='5s'>

#新要求 找a7a a88a a7878a
msg='a7afgdgfda8a4545fdga7878agr'
"[a-z][0-9]+[a-z]  第一个字母 中间+号表示1个数字 或者多个数字  满足a7a a88a a7878a 最后一个字母"
result=re.findall('[a-z][0-9]+[a-z]',msg)
print(result)


"用正则验证qq号的输入 5-10位数 开头不能是0"
qq='1234567890'
'''^[1-9]表示开头第一位必须不是0 要1-9之间的数
[0-9]{4,9}中间的数字为0-9 最少匹配4次或者最多匹配9 次 $表示匹配到结束
'''
result=re.findall('^[1-9][0-9]{4,9}$',qq)
print(result)

"[0-9a-zA-Z]括号里可以多个范围"
#练习   用户名可以是字母或者数字或下划线 不能上数字开头，长度6位以上
name='admin45646854465'
'''^[a-zA-Z] 表示第一位不能是数字开头
[0-9a-zA-Z]表示剩下的位数可以是数字字母
{5,}表示最少要检测6位（前面检测了一位）且不指定总位数
'''
result=re.findall('^[a-zA-Z][0-9a-zA-Z_]{5,}$',name)
print(result)
########################################################################
#\w匹配任意的字母数字和下划线 \w   =    [0-9a-zA-Z_]
result=re.findall('^[a-zA-Z]\w{5,}',name)
print(result)

#找出字符串中的py文件
# .匹配.和其他任意符号，\b匹配字符串边界（空格等） 加r 取消转义\\
msg='a*py bb.py ccc.py xy.py dfsdf.txt'
result=re.findall(r'\w+\.py\b',msg)#\.不加\的话 会把a*py匹配到
print(result)

'''
总结
. 任意字符 \n除外
^ 开头  用match的话不用加这个  因为默认上从开头匹配
$ 结尾  用srarch的话 开头结尾都要加
[]  表示范围  [a-z*#$%]
|  或者 
正则预定义
\s 空白 （空格）
\b  边界
\d  数字
\w  字母数字下划线  [0-9a-zA-Z_]        
\加上他们的大写字母  就是反面  非数字...

表示数量的  匹配多个
* >=0
+ >=1  \w+  表示匹配多个任意字母下划线
？ 0 或者1位
手机号码正则
re.findall('^1[356789]\d{9}$')
^1第一位   [356789] d{9}后面9位

｛m｝  固定匹配多少位（多少次）
{m,}    匹配大于m次
{m,n}  匹配的一个范围

'''
#匹配数字0-100
n='99'
result=re.findall(r'^\d\d$|100',n)
# | 前面的一种匹配，匹配到00-99，只匹配2个数字  后面只匹配100
print(result)


''''[]里表示一位[0-9] 表示0-9间的一个数
(word1|word2|word3)用或者 表示一个单词 要么word1要么word2  3 
'''

"验证输入的邮箱 163 126 qq"
email='4856666@qq.com'
result=re.search(r'\d{5,}@(163|126|qq)\.com$',email)
print(result)


#再匹配电话号码  不能以 4 7 结尾
phone='12345678958'
result=re.match(r'1\d{9}[0-35-68-9]$',phone)
print(result)
result=re.match(r'1\d{9}[^47]$',phone)
print(result)

#分组  提取
phone='0817-8347884'
result=re.match(r'(\d{3,4})-(\d{7})$',phone)
#(\d{3,4}) 小括号把区号分为一组  可能是3位或者4位
#(\d{7})$  小括号把号码分为一组 7位
print(result)
#group(1)表示第一组的内容
print(result.group(1))
print(result.group(2))

#取出<>?<>
msg='<html>python<html>'
msg1='<hkldhas>lingxia<www>'
result=re.match(r'<\w+>(.+)<\w+>',msg)
print(result)
print(result.group(1))



#sub(正则，要改的内容，字符串)
mm=re.sub(r'\d+','100','java=90分，pathon=95分')
print(mm)#      java=100分，pathon=100分

#split
#        遇到=：就切一刀
mm=re.split(r'[=,]','java=90分，pathon=95分')
print(mm)#['java', '90分，pathon', '95分']

'''
re模块
re.match('正则'，字符串)
re.search('正则'，字符串)
re.findall('正则'，字符串)
re.sub('正则'，要替换的内容，字符串)
re.split('正则'，字符串)


'''


