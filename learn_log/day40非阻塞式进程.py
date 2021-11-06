# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/17 14:37
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day40非阻塞式进程.py
# @Software: PyCharm



'''
当需要创建的子进程数量不多时，可以直接利用multiprocessing中的Process动态生成多个进程，day39中的p1p2
要创建大量的进程，使用multiprocessing中的Pool方法
初始化时，可以指定一个最大进程数，当满了后，有新的进程提交的话，会等待，直到有进程结束了再运行
非阻塞式 全部添加到队列中，立刻返回了，再赶紧添加下一个，并没有等其他进程执行完毕
阻塞式  添加一个执行一个，如果一个任务不结束，另外一个就进不来
'''
from multiprocessing import Pool#导入能批量创建进程的池子
import time
import random
import os
#非阻塞式进程
def task(task_name):
    print('开始做任务啦',task_name)
    start=time.time()
    #使用sleep 休眠几秒钟
    time.sleep(random.random()*2)
    end=time.time()
    print('完成-{}-任务！用时'.format(task_name),end-start,'进程id',os.getpid())

if __name__ == '__main__':
    pool=Pool(3)#创建3个进程

    tasks=['左爱','唱歌','泡面','打游戏','吃饭'] #有5个任务，先进去3个任务，等完成其中一个了，后面的任务才能进去
    for i in tasks:
        #                          可加回调函数callback
        pool.apply_async(task,args=(i,))# def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
    pool.close()#添加任务结束

    pool.join()# 主程序等待子进程结束
'''创建一个进程池，再把5个任务加入进去，只能先加3个，分配3个id 进去后就随机数时间休眠，谁的时间短，就先完成，后2个任务再排队进入池中，对应空的进程id
开始做任务啦 左爱
开始做任务啦 唱歌
开始做任务啦 泡面
完成-唱歌-任务！用时 0.2278578281402588 进程id 14120

开始做任务啦 打游戏
完成-打游戏-任务！用时 0.6281688213348389 进程id 14120
开始做任务啦 吃饭
完成-泡面-任务！用时 1.5786042213439941 进程id 16376
完成-吃饭-任务！用时 0.8816616535186768 进程id 14120
完成-左爱-任务！用时 1.881688117980957 进程id 7780'''
########################################################################################################


