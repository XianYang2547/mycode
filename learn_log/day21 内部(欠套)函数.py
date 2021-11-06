# 内部(欠套)函数
'''函数里面又声明了函数
可以访问外部函数的变量
内部函数func3 可以修改外部函数  n list1的值
nonlocal声名此变量与外层同名变量为相同的变量。
nonlocal关键字只能用于嵌套函数中，并且外层函数中必须定义了相应的局部变量，否则会发生错误
'''


def func():
    # 声明变量
    n = 100  # 局部变量
    list1 = [7, 1, 9, 4]  # 局部变量

    def func2(): # 对list1操作。它是
        nonlocal n
        # 在python中内嵌函数可以引用外层函数作用域中的变量，并且可以通过某种操作来对其进行修改。
        # 这里我们就可以使用到nonlocal语句来进行声名。nonlocal作用于外部内嵌函数的变量
        for index,i in enumerate(list1): # 返回下标和值
            # 对list里每个元素+n
            list1[index] = i+n
        list1.sort()
        # 修改n
        n += 100
    func2()

    print(n)
    print(list1) # [6, 9, 12, 14]


func()



# 再例
a=100 #全局变量
def func3():
    b=99
    def func4():
        c=22
        print(a,b,c)
    #调用
    func4()
#调用
func3()#100 99 22




x=82 #全局变量
def func3():
    y=99
    def func4():
        global x
        nonlocal y
        z=22
        #尝试修改值
        z+=78#能直接修改自己的
        y+=1#修改它外面函数的不可变变量加nonlocal
        x+=18#修改最外面的不可变变量用global

        print(x,y,z)
    #调用
    func4()
#调用
func3()