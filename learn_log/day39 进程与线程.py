#实现多任务的方式  进程 线程 协程
from multiprocessing import Process # 包里的类
from time import sleep
import os
"Process(target=task2,name='任务2',args=(2,'bb')) 开启进程"
m=1
def task1(s,name):
    global m
    while 1:
        sleep(s)
        m+=1
        print('这是任务1......',os.getpid(),name,m)
def task2(s,name):
    global m
    while 1:
        sleep(s)
        m+=1
        print('这是任务2......',os.getpid(),name,m)


if __name__=='__main__':
    print('父进程的pid号',os.getpid())#执行这个py文件时 就是个主进程
    #创建一个进程并运行
 # 要这个进程干的事（task1）调用函数名       取名字    args=(2,)给函数传参  要传可迭代的  传了2个 函数接受参数里用2个参数去接def task1(s,name):
    p1=Process(target=task1,name='任务1',args=(1,'aa'))
    p1.start()
    print(p1.name)#打印此进程的名字


    p2=Process(target=task2,name='任务2',args=(2,'bb'))
    p2.start()
    print(p2.name)#打印此进程的名字
    # task2()#不用多进程的话 任务1没执行完 任务2就不会执行
'''
from multiprocessing import Process
process=Process(target=函数名，name=进程的名字，arges=给函数传递的参数  元组 列表等)
process对象
对象调用方法
process.start()启动进程并执行任务
process.run()只是执行了任务 但没有启动进程
process.terminate()结束  可在子进程中结束 也可在主进程中结束
多进程对于全局变量访问，在每一个进程里面都放一个m
保证每个进程访问变量都不干扰  两个进程的m值不干扰
而线程则不是

'''

"继承Process的方式开启进程   要重写run"
# from multiprocessing import Process
# class MyProcess(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     #重写run方法
#     def run(self):
#         n=1
#         while 1:
#             print('{}自定义进程n:{}'.format(n,self.name))
#             n+=1
#             if n==6:
#                 break
# if __name__ == '__main__':
#     p=MyProcess('小明')
#     p.start()
#     p1=MyProcess('小红')
#     p1.start()

