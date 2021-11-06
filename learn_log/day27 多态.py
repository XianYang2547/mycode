# 封装（私有化） 继承（父类子类） 多态     面向对象的3大特点
class Animal():
    def who(self):
        print("I am an Animal")
class Duck(Animal):
    def who(self):
        print("I am a duck")

class Dog(Animal):
    def who(self):
        print("I am a dog")

class Cat(Animal):
    def who(self):
        print("I am a cat")
#多态顾名思义多种状态，在python中，不同的对象调用同一个函数，表现出不同的状态，称为多态
def func(obj):
    obj.who()
duck=Duck()
dog=Dog()
cat=Cat()##########创建对象

func(duck)
func(dog)
func(cat)#########用函数去调用对象






