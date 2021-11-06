#包就是文件夹，但该文件夹下必须存在 __init__.py 文件。
# 1 调包里面的
from day30_bao import class01  # 从包中导入class01模块
#用模块名来调用
x = class01.max1(5, 8)
print(x)
y = class01.Person(123, 111)
y.login(123,111)


from day30_bao.class01 import *  # 从包中的class01模块导入所有的（函数 类）
#用模块里面的函数和类来调用
ans = max1(4, 8)  # 调用包中的class01 里面的max函数
print(ans)
person = Person('张三', 123)  # 调用包中的class01 里面的Persom类
person.login('张三', 123)
#__all__ = ['max1','Person']  min1没有放在__all__里，相当于通过 import * 方式导入没有找到它
# h=min1(8,9)
# print(h)


# 2 包里调外面的
#具体查看包day30_bao里面的study


# 3 包里调包里的 比如class01 调用study
'''
绝对路径：包里的py文件相互调用要导入 完整的  比如包里的某个文件要导入class01里面的东西 from day30_bao.class01 import Person
相对路径：
'''
# from .class01 import study
# 包里__init__.py文件的作用
"当导入包的时候，文件里的东西 默认执行" \
""
import day30_bao
#当导入时 包里的init.py文件里的  print('自动执行了')
day30_bao.creatapp()#里面的函数也被加载了，这是调用  此文件中的函数 变量等 通过包名直接调用就可以了
#from 包名 import *  这样导入的话，包里的都不能用，这时候要在init文件里 写 ————all————，加入【】里的才能用





