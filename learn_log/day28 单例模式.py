#================单例模式
"""
单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。
如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，
这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。
事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象，多个实例对象都指向一个地址。
"""

class Dog:
    def __init__(self,name):
        self.name=name
        pass

a=Dog('旺财')
b=Dog('大黄')
print(a,b)
#两个对象，地址不一样   <__main__.Dog object at 0x0000026025A15A90> <__main__.Dog object at 0x00000260259E8220>

#                                       基于__new__实现的单例模式（最常用）
#                                   通过定义一个私有化类属性，默认为空，等到创建第一个对象时，赋值一个地址给它，就不为空了，（<-----满足if条件）
#                                   当创建第二个时，不执行if 直接返回大黄，地址不变，确保类只有一个实例存在，节省内存资源
class Singleton:
     __dahuang=None#将单例的地址存在于此，私有化 又不能在外部访问 改   先默认是空的
     name='大黄'
     #重写__new__
     def __new__(cls, *args, **kwargs):
         if cls.__dahuang is None:#用__dahuang来判断             后面新创建的都不满足了，因为大黄已经不为空了
             cls.__dahuang=object.__new__(cls) #创建一个空间 给到大黄         ————new返回的给到了self
         return cls.__dahuang
     def show(self,n):
         print(Singleton.name,n)#用类名访问类属性
s1=Singleton()
s2=Singleton()
s1.show(1)#大黄 1
s2.show(2)#大黄 2
print(s1,s2)#两个对象，指向的地址上相同的  <__main__.Singleton object at 0x000002275750F280> <__main__.Singleton object at 0x000002275750F280>

#new 是init的大哥
class A:
	def __init__(self, name):
		print('执行 __init__')
		self.name = name

	def __new__(cls, *args, **kw):
		print('执行 __new__')
		return object.__new__(cls)  # 这里和使用super()方法是一样的 有的是返回 return super().__new__(cls)
a = A('wang')
#          先 执行 __new__             再  执行 __init__


#使用__new__和__init__的区别是一个在创建对象之前判断，一个在创建对象之后判断
class Person:
    def __new__(cls, age):
        if age>100:
            return "年龄age需小于100,对象未创建"
        else:
            return super().__new__(cls)
    def __init__(self, age):
        self.age = age

print(Person(200))
'年龄age需小于100,年龄age需小于200,对象未创建'


class Person:
    def __new__(cls, age):
        print("对象已经创建")
        return super().__new__(cls)

    def __init__(self, age):
        if age>100:
            print("wrong age,参数初始化失败")
        else:
            self.age = age

p = Person(200)
# p.age#对象没有创建成功，AttributeError: 'Person' object has no attribute 'age'
p.age
