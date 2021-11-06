#私有化
'''
隐藏属性不被外界随意修改
也可以修改，通过类里面的函数......

直接print（dir（student）），查找出带有私有属性的标签，只是被重命名了
print(student._Student__name)

'''

#封装  1 私有化属性  只能在类里面修改和访问 2 定义公有set和get方法
class Student():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        self.__score=59
    #下面这个在调用对象名的时候能给出提示
    #使用__str__后，打印对象的时候不是显示地址，而是返回后的信息

    #定义公有set和get方法
    def set1(self,age,score):#改年龄分数
        if (age>0 and age<100) and (score>0 and score<100):
            self.__age=age#可加一些修改限制 if
            self.__score=score
        else:
            print('请输入正常的范围噢')
    def ste2(self,name):
        if len(name)<10:
            self.__name=name
        else:
            print('名字长度需小于10位')
    #拿出参数
    def get1(self):
        return self.__name#可拿出名字 年龄 分数
    def __str__(self):
        return '名字是{}，年龄是{}，成绩是{}'.format(self.__name,self.__age,self.__score)
#调用
student=Student('tom',25)
print(student)#名字是tom，年龄是25，成绩是59
print(student.get1())#拿出名字
# print(student.age,student.name,student.__score)   提示在Student中没有__score，私有化了，在外部不能访问
student.set1(50,60)
student.ste2('xianyang')
print(student)
print(student.get1())#拿出名字









