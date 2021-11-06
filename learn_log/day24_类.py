import time,datetime
#类  模型而已
class Student():#类名
    #类属性
    name='xianyang'
    age=25
    #方法  def
#new个对象。用类创建个对象
new_object=Student()
print(new_object.name)
#改age
new_object.age=28 #  先在自己里面找，再去类里面找。在自己里找到了new_object.age=28，它就是对象属性
print(new_object.age)
#改类属性的值 用类名来操作
# Student.age=80


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车的里程"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

#继承
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """ 初始化父类的属性"""
        super().__init__(make,model,year)
        self.batteryt_size=72
    def describle_battery(self):
        print('电瓶大小为：'+str(self.batteryt_size))
        # return self.batteryt_size

my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describle_battery()
my_tesla.update_odometer(50)
my_tesla.increment_odometer(20)
my_tesla.read_odometer()
#类方法
class Dog:
    #定任意一个类属性
    __aa='sss' #加__成为私有的
    #定义方法们
    def __init__(self,nickname):
        self.nickname=nickname
    def run(self):
        print('{}跑飞了'.format(self.nickname))
    def eat(self):
        print('吃饭')
        self.run()#调用上面的
    #类方法中 参数cls 不是一个对象，而是类
    #类方法中，只能使用类属性  像  aa
    @classmethod#只能访问类属性和方法
    def test(cls):#定义个类方法 cls就是上面的Dog  cls==Dog
            #里面不能调self相关的 也不能调用上面的def
        print('类方法')
        print(cls)#<class '__main__.Dog'>
        cls.__aa+='555' ###不创建对象 对属性进行修改
        print(cls.__aa)#使用类属性

    @staticmethod#只能访问类属性和方法
    def text1():#没有cls
        print('静态方法')
        print(Dog.__aa)##要调用出aa，类方法用的cls 这里不传参，用类名来调用访问  Dog.__aa
d=Dog('小黑')
d.eat()
d.test()
Dog.test()#用类名 来调用test 没有对象d 都可以调用
Dog.text1()

#类装饰器
class TakeUpTime:
    def __init__(self, func):
        self.func = func

    # 对于该例子，*args, **kwargs可以去掉
    def __call__(self, *args, **kwargs):
        start_time = datetime.datetime.now()
        self.func()
        end_time = datetime.datetime.now()
        print('执行结束,执行时间为：', end_time - start_time)
#self.func = func   通过初始化函数接收被装饰函数，赋值给类属性，
# 以便下方的__call__函数调用。函数调用的时候才需要加()，
# 所以__call__中是func()。传递的时候不需要加()，所以__init__中是func。

@TakeUpTime
def test():
    for i in range(3):
        time.sleep(1)


test()







