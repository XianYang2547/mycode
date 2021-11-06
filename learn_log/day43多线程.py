# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/19 9:04
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day43多线程.py
# @Software: PyCharm



#多线程和多进程最大的不同在于，多进程中，同一个变量，
# 各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被
# 任何一个线程修改，因此，线程之间共享数据最大的危险在
# 于多个线程同时改一个变量，把内容给改乱了。
"线程是进程的一部分"


from time import sleep
from threading import Thread, Lock  # 导入进程模块,锁模块

# def download(n):
#     images=['girl.jpg','boy.jpg','man.jpg']
#     for image in images:
#         print('正在下载:',image)
#         sleep(n)
#         print('下载{}成功'.format(image))
#
# def listenmusic():
#     musics=['千题之恋','活埋','回忆总想哭']
#     for music in musics:
#         sleep(0.5)
#         print('正在听'+music)
#
# if __name__ == '__main__':
#     #创建2个线程
#     t1=Thread(target=download,args=(1,))
#     t1.start()
#
#     t2=Thread(target=listenmusic)#函数要传参的话 用args
#     t2.start()
'''正在下载: girl.jpg
正在听千题之恋
正在听活埋
下载girl.jpg成功
正在下载: boy.jpg
正在听回忆总想哭
下载boy.jpg成功
正在下载: man.jpg
下载man.jpg成功'''
#################################################################################
####线程可以共享全局变量，多个线程共同对某个数据修改，可能会出错
n=0
def task1():
    global n
    for i in range(1000000):
        n+=1
def task2():
    global n
    for i in range(1000000):
        n+=1
if __name__ == '__main__':
    #创建、启动线程
    t11=Thread(target=task1)
    t22=Thread(target=task2)
    t11.start()
    t22.start()
    print(n)#当数据过大了，539415 结果差太多， 先加1在赋值，加了1后，赋值这一步的时候被其他进程抢占
"数据不安全，每个线程加上锁，但耗时，耗时操作，爬虫等，用多线程" \
"python底层当我们在使用线程时默认加了锁，当数据过大时就把锁释放了，导致数据不安全，计算用进程好些"
'''
import threading
lock = threading.Lock()
from threading import Thread, Lock'''
#解决  加了锁就变成单线程
#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定会被释放。
'''
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            函数
        finally:
            # 改完了一定要释放锁:
            lock.release()'''


lock=Lock()
list1=[0]*10#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def tas():
    lock.acquire()#获得一个🔒
    for i in range(len(list1)):
        list1[i]=1#把0-9放入列表中
        sleep(0.2)
    lock.release()#释放🔒

def tass():
    lock.acquire()
    for i in range(len(list1)):
        print(i)
        sleep(0.2)
    lock.release()#释放🔒
if __name__ == '__main__':
    #创建、启动线程
    t111=Thread(target=tas)
    t222=Thread(target=tass)
    t111.start()
    t222.start()


