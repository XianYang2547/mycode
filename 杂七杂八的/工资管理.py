'''
编写一个简单的工资管理创新，系统可以管理一下4类人，工人，销售员，经理，销售经理
所有的员工都具有工号 姓名，工资等属性，有设置姓名 获取姓名 员工号 计算工资等方法
1 工人：具有工作小时和时薪的属性，工资计算方法为 小时数*时薪
2 销售员：具有销售额和提成比例的属性，工资计算方法为销售额*提成比例
3 经理：具有固定月薪的比例，工资计算方法为固定月薪
4 总经理：工资计算方法为销售额*提成比例+固定月薪
请根据以上要求设计合理的类，完成以下功能
1 添加所有类型的人员
2 计算月薪
3 显示所有人员工资情况
'''
class MangerSystem:
    def __init__(self,name,number,wage):
        self.name=name
        self.number=number
        self.wage=wage#基础工资
    def __str__(self):#这个方法是方便打印对象本身     名字：张三,工号是875504758，本月工资：1692
        return '名字：{},工号是{}，本月工资：{}'.format(self.name,self.number,self.pay())
class Worker(MangerSystem):
    def __init__(self,name,number,wage,worktime,salary):
        super().__init__(name,number,wage)
        self.worktime=worktime
        self.salary=salary
    def pay(self):
        meneyy=self.worktime*self.salary+self.wage
        return meneyy
class Salesman(MangerSystem):
    def __init__(self,name,number,wage,totalsales,ticheng):
        super().__init__(name,number,wage)
        self.totalsales=totalsales
        self.ticheng=ticheng
    def pay(self):
        meneyy=self.totalsales*self.ticheng+self.wage
        return meneyy
class Manger(MangerSystem):
    def __init__(self,name,number,wage):
        super().__init__(name,number,wage)
    def pay(self):
        return self.wage
class Salemanger(Manger):
    def __init__(self,name,number,wage,):
        super().__init__(name,number,wage)
    def pay(self):
        meneyy=self.totalsales*self.ticheng+self.wage
        return meneyy

f=Worker('张三',875504758,1500,8,12)##__str__里面调用了pay()，会计算
print(f)#打印对象本身，返回 __str__的信息
y=Salesman('李四',123456,2000,5000000,0.003)
print(y)
z=Manger('王五',1111,100000)
print(z)