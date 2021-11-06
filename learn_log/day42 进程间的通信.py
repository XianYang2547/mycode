# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/17 17:14
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day42 进程间的通信.py
# @Software: PyCharm

from multiprocessing import Process,Queue
from time import sleep


def download(q):
    images=['girl.jpg','boy.jpg','man.jpg']
    for image in images:
        print('正在下载:',image)
        sleep(0.5)
        q.put(image)# 存入队列

def getfile(q):
    while 1:
        try:
            file=q.get(timeout=2)#从队列里取  要循环取完
            print('{}保存成功'.format(file))
        except:
            print('全部保存完毕')#取完啦就break
            break

if __name__ == '__main__':
    q=Queue()#Queue是多进程安全的队列,可以使用Queue实现多进程之间的数据传递,提供了Put和Get两个方法
    p1=Process(target=download,args=(q,))
    p2=Process(target=getfile,args=(q,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()