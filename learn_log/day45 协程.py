# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/20 14:12
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day45 协程.py
# @Software: PyCharm

#两个线程的通信，生产者和消费者
'''
1.创建线程
t=Thread(target=func,args=())
t.start()
join()
2.自定义线程
class MyThread(Thread):
    def run(self)
        重写run

    t=MyThread()传参要定义init方法
    t.start()
3.数据共享
    进程是每一个进程中都有一份
    线程是公用一个数据  数据安全性问题
    lock=Lock()
    lock.acquire()上锁
    ....
    lock.release()  释放锁
4.线程间通信
    生产者：线程
    消费者 ：线程
    import queue
    q=queue.Queue()
    q.put()
    q.get()
'''
#  进程>   线程>协程
#Process  Threaad   生成器完成的-->greenlet-->gevent
#协程：微线程  切换任务
#用生成器完成
import time

from greenlet._greenlet import greenlet


def task1():
    for i in range(3):
        print('a'+str(i))
        yield
        time.sleep(0.2)

def task2():
    for i in range(3):
        print('b'+str(i))
        yield
        time.sleep(0.2)
if __name__ == '__main__':
    #得到2个生成器
    g1=task1()
    g2=task2()

    while 1:
        try:
            next(g1)
            next(g2)
        except:
            break
'''
a0
b0
a1
b1
a2
b2'''
print('*'*10)
#############################
"greenlet 完成协程任务,手动切换"

def a():#任务a
    for i in range(5):
        print('a'+str(i))
        gb.switch() #在它睡觉的时候切换到下一个
        time.sleep(0.2)
def b():#任务b
    for i in range(5):
        print('b'+str(i))
        gc.switch()  # 在它睡觉的时候切换到下一个
        time.sleep(0.2)
def c():#任务c
    for i in range(5):
        print('c'+str(i))
        ga.switch()  # 在它睡觉的时候切换到下一个
        time.sleep(0.2)

if __name__ == '__main__':
    ga= greenlet(a)
    gb= greenlet(b)
    gc= greenlet(c)
    ga.switch()
    print('*' * 10)

####################################


