# day1 输出print
#python的语言标识符以字母下划线开头，后面可跟任意的字母数字下划线
#print函数
#1.用法
print('hello world')
name='小白'
print(name)
#2.用法：print(name,age,gender)
age=18
gender='boy'
print(name,age,gender)#结果：小白 18 boy

help(print)#查看print的用法 
'''Help on built-in function print in module builtins:
print(...)
    print(value, ...这是要打印的东西, sep=' 'value间的默认分隔符是空格, end='\n',转义字符\n,换行 (print打印完了默认换一行)   file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.    '''
print(name,age,gender,sep='*')#结果：小白*18*boy
#\n在字符串里起换行作用
print('hello\nkitty')#hello
                     #kitty
print('name,age\ngender')    
print('AAA',end='') ,print('BBB',end='') ,print('CCC',end='')#打印的结果未换行 AABBCC
print()
#练习
print('亲爱的xxx：\n\t\t请点击链接激活用户：激活用户')
#\t 转义字符 \t 制表符，（给出空格）

message='''666
777
888'''
print(message)#三引号的内容，里面（格式）是啥就是啥，是打印后不变
#三引号的作用1 作为多行注释使用，'''注释内容''' 2 保留格式的字符串使用
print('*'*30)
print('白嫖怪')
print('*'*30)



#字符串的格式化输出方式：1  使用占位符%s %d %f  2. 使用format
#格式化输出   %s  str
person='亚索 '
address='艾欧尼亚 '
phone='1234567 '
money=50
#'+'表示拼接 字符串+字符串.下面语句当money='50'才正确
#print('订单的收件人是：'+person+'收货地址是：'+address +'联系方式：'+phone+'死亡次数：'+money)
print('订单的收件人是：%s,收货地址是：%s，联系方式：%s，死亡次数%s'%(person,address,phone,money))
#类型转换str(int)
print('订单的收件人是：'+person+'收货地址是：'+address +'联系方式：'+phone+'死亡次数：'+str(money))

#            %d  digit 数字  取成整型
dead=51.11257 #int(51.1)---->51
print('死亡次数是：%d' %dead)
print('死亡次数是：%.2d' %dead)#%.2d=%d

#            %f float 浮点  小数点后面的位数，四舍五入
money=899.256
print('我的钱是：%.1f' %money)
print('我的钱是：%.2f' %money)
print('我的钱是：%.0f' %money)

movie='小电影'
ticket=45.9
count=35
total=ticket*count
message='''
电影：%s  
人数：%d
单价：%.1f
总票价：%.1f
'''%(movie,count,ticket,total)
# %s占位 %d取整 %f取小数点多少位
print(message)
#print(电影：%s,人数：%d,单价：%.1f,总票价：%.1f %(movie,count,ticket,total))

# format	相当于调用这个函数  . 表示调用,好像不考虑整型浮点型那些
age=0
s='已经'
message='压缩说：我今年{}岁了'.format(age)
print(message)
message='压缩说：我今年{}岁了，{}送了无数人头了'.format(age,s)
print(message)

