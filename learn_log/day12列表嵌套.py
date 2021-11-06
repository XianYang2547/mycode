####列表的嵌套：列表里还有列表，二维列表
list1=[[1,'说的',3],[4,5,6,7],[8,9]]
print(list1[0][1])#取列表第三个[4,5,6,7] 再取第一个数  5

#列表*3  和字符串一样的
list2=[1,2,3]
print(list2*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]

'''
类型转换：
str() 转成字符
int() 转成整型
list()转成列表。
'''
list(range(1,10,3))#的结果是？range(1,10,3) 是1 4 7
print(list(range(1,10,3)))#[1, 4, 7]

s='abc'# 字符转成列表    数字不能转
print(list(s))#['a', 'b', 'c']




##删除  del list[i]
##     remove(x)  删除列表中第一次出现的元素x  返回值是none 要是没有找到要删除的，报异常
##     pop()     移除列表里最后一个元素，括号里默认没有参数。
##				 （x）也可以指定元素位置下标删除
##		clear()		清楚列表

s=['1','2','3','4','5','5','6','7','8','9']
s.remove('5')
print(s)

s=['1','2','3','4','5','5','6','7','8','9']
s.pop()
print(s)

s=['1','2','3','4','5','5','6','7','8','9']
s.pop(-2)
print(s)

s=['1','2','3','4','5','5','6','7','8','9']
s.clear()
print(s)

###拿列表去调用，和把列表扔在函数里的区别
###将列表改变顺序，倒序形式，此操作改变列表本身顺序  而s[：：-1] 不改变本身，只是打印出来
s=['1','2','3','4','5','5','6','7','8','9']
s.reverse()
print(s)

s=[1,5,6,8,9,7,3,5,6,10]
s.sort()
print(s)#原来的s变了

s=[1,5,6,8,9,7,3,5,6,10]
print(sorted(s)) #排序后打印出来，不改变列表本身
print(s)#原来的s不变









