# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/17 16:49
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day41 阻塞式进程.py
# @Software: PyCharm
#阻塞式进程
import os
import random
import time
from multiprocessing import Pool


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
        pool.apply(task,args=(i,))# def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
    pool.close()#添加任务结束

    pool.join()# 先阻止程序运行结束
    '''
    开始做任务啦 左爱
完成-左爱-任务！用时 1.3138232231140137 进程id 3484
开始做任务啦 唱歌
完成-唱歌-任务！用时 1.8643608093261719 进程id 5628
开始做任务啦 泡面
完成-泡面-任务！用时 0.5535399913787842 进程id 12356
开始做任务啦 打游戏
完成-打游戏-任务！用时 1.1681640148162842 进程id 3484
开始做任务啦 吃饭
完成-吃饭-任务！用时 0.6638526916503906 进程id 5628'''

'''
总结
进程池
pool=Pool(max)
pool.apply()阻塞的
pool.apply_async()非阻塞的
pool.close()停止添加任务
pool.join() 让程序主进程让步，主进程结束了 就都不执行了
'''