"节省内存"
#定义一个0 3 6 9 12...的生成器
g=(x*3 for x in range(10))
print(g)#<generator object <genexpr> at 0x000001E30BBB0120>
#   方式一通过__next__（）调用得到元素
print(g.__next__())#0
print(g.__next__())#3
print(g.__next__())#6
#   方式二
print(next(g))#9
print(next(g))#12
#每调用一次产生一个元素

m=(x*2 for x in range(5))#0 2 4 6 8
while 1:
    try:
        e=next(m)
        print(e)
    except:
        print('没有更多元素拉')
        break

#定义生成器  借助函数完成
#只要函数中出现了yield关键字 就是生成器了
'''步骤
1 定义一个函数，函数中使用yield关键字 yield后的 东西 就是要往外面仍的
2调用函数 接受调用的结果
3得到的结果就是生成器
4 借助next（）或者————next（）
'''
def func():
    n=0
    while 1:
        n+=1
        yield n# 到了这儿就暂停 扔出n

g=func()
print(g.__next__())#1
print(next(g))#2
print('*****************')


#生成数列 0 1 1 2 3 5 8 13 21 24 55....
def fib(length):
    a,b=0,1
    n=0
    while n<length:
        yield a#往外扔 a 或者b都可
        a,b=b,a+b
        n+=1
    return '没有更多元素了'#没有元素时返回错误信息
g=fib(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
