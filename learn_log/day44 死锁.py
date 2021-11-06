# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/20 12:17
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day44 死锁.py
# @Software: PyCharm

#######################
#死锁
'''
避免出现死锁
重构代码
accquire（）加上timeout超时

'''
from threading import Thread,Lock
import time
lockA=Lock()
lockB=Lock()#给2把锁
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        if lockA.acquire():#如果可以拿到锁，返回真
            print(self.name+'获取了A锁')# 不定义init方法，这就是Thread默认的名字
            time.sleep(0.2)
            if lockB.acquire(timeout=3):#超时了，if为假，不获取B锁，再释放A锁，下面的B锁就能获得A锁
                print(self.name+'又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()

class MyThread1(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        if lockB.acquire():#如果可以拿到锁，返回真
            print(self.name+'获取了B锁')
            time.sleep(0.2)
            if lockA.acquire(timeout=3):
                print(self.name+'又获取了A锁，原来还有B锁')
                lockA.release()
            lockB.release()
if __name__ == '__main__':
    m1=MyThread('A🔒')#传参，给锁取名
    m2=MyThread1('B🔒')
    m1.start()
    m2.start()
    m1.join()
    m2.join()
"线程1拿到A锁，睡觉了，线程2拿到B锁，睡觉了，线程1醒了，拿不到B锁，一直等待，释放不了拿到的A锁，线程2醒了，拿不到A锁"

