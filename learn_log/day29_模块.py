#自定义模块
#使用系统模块
#只要导入了某个模块 里面的东西就全部被加载了

"                       导入模块的方法"
'''         模块名                                         函数
import  calculatepy                  使用模块 calculatepy.max（）
from    calculatepy import max,min     使用模块         add() min()
from    calculatepy import *   导入模块中的所有内容
        用*能导入模块的所有内容，但是在模块中使用__all__=[ ] 加在列表里的函数 才能被*号发现
'''
#把下面的存为一个calculatepy文件
# 在模块中定义变量
a = 10
b = 20
# 在模块中定义函数
def max1(x, y):
    """加法"""
    return x + y

def min1(x,y):
    """减法"""
    return x-y

# 在模块中定义类
class calculator: # 定义一个加法计算器
    @classmethod #导入计算器模块
    def sum(cls,*nums):
        res = 0
        for i in nums:
            res += i
        return res
'''
__name__ 属性是模块的内置属性，每个模块中都有该属性，当该
.py文件是主执行文件，直接被执行时，其值为 __main__ ，就可以执行if __name__ == '__main__' : 后面的内容了    print(__name__）  =__main__ 
当该.py文件是被调用，导入执行文件时，其值为 调用的模块名，if不成立
                                                                                                    print(__name__）  =模块本身的名字
'''
# print(__name__）# 如果这么直接这么测试，被导入文件执行时，导入文件也会打印该内容

#程序入口，类似于java中的main()方法，只在当直接调用该文件时才会执行，用来执行测试
if __name__ == '__main__' : #在模块本身运行，就满足条件
    print(max(5,2),min(10,1),calculator.sum(1,2,3)) # 只有在当前界面执行才会打印该内容，其他文件中不会执行。









