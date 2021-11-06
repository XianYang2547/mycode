'''情况一：子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。

情况二：子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。

情况三：子类重写__init__()方法又需要调用父类的方法：使用super关键词：'''
class Road:
    def __init__(self,road_name,road_long):
        self.road_name=road_name
        self.road_long=road_long
class Car(Road):#继承上面那个类
    def __init__(self,road_name,road_long):
        super().__init__(road_name,road_long)#调用父类对象,和父类的参数一样
        self.car_name='BMW'
        self.car_speed='40km/小时'
    def get_time(self):
        time=30#input('输入时间')
        print('{}在{}上以{}的速度行驶了{}分钟'.format(self.car_name,self.road_name,self.car_speed,time))
    def car_information(self):
        print('车的名字是{}，车的速度是{}'.format(self.car_name,self.car_speed))

f=Car('和平大道','80KM')
f.get_time()
f.car_information()
f=Car('成渝地区大桥','20KM')
f.get_time()
f.car_information()
######子类不能继承父类的私有属性

###多继承
#继承的父类中有相同的方法时，广度优先 搜索
class A:
    def test(self):
        print('------a')
class B:
    def test1(self):
        print('------b')
class C(A,B):
    def test2(self):
        print('------c')
c=C()
c.test()
c.test1()
c.test2()







