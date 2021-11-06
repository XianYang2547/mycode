#列表推导式 字典推导式 集合推导式
# 旧的列表----->新的列表
#格式  [表达式 for 变量 in 旧列表]或者[表达式 for 变量 in 旧列表 if 条件]
#过滤长度小于3的人名 首字母大写

names=['bob','lily','abc','steven','ton','jerry']
result=[name.capitalize() for name in names if len(name)>3]
#     这个name 就是符合条件的name
print(result)
#下面函数等于上面的列表推导式
def func(names):
    newlist=[]
    for name in names:
        if len(name)>3:
            name=name.title()
            newlist.append(name)
    return newlist
print(func(names))

#将1-100之间能被3整除的数，组成一个新的列表
result=[i for i in range(1,101) if i%3==0 and i%5==0]
print(result)#[15, 30, 45, 60, 75, 90]



###################################################################################
#0-6之间的偶数 和 0-11之间的奇数 组成元组
#[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9)]

#                               推导式
result=[(i,j) for i in range(6) if i%2==0 for j in range(11) if j %2!=0]
print(result)
#                               函数
def func():
    newlist=[]
    for i in range(6):
        if i %2==0:
            for j in range(11):
                if j %2!=0:
                    newlist.append((i,j))
    return newlist
print(func())

#集合
list1=[1,2,1,3,2,5,5,8]
set1={x for x in list1}#把列表的元素放在集合中  去重
print(set1)#{1, 2, 3, 5, 8}


#字典
dict1={'a':'A','b':'B','c':'C','d':'C'}
dic1={value:key for key,value in dict1.items()}#遍历字典取出键值对，值键颠倒组成新字典
print(dic1)#{'A': 'a', 'B': 'b', 'C': 'd'} 键C只能有一个，C：c C：d  后面的覆盖前面的

