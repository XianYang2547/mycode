# 爱生活，爱Python
# -- coding: UTF-8  --
# @Time : 2021/8/20 15:34
# @Author : Xianyang
# @Email : xy_mts@163.com
# @File : day46 gevent和猴子补丁.py
# @Software: PyCharm


'''Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。
gevent是第三方库，通过greenlet实现协程，其基本思想是：
当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，
经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
'''

"gevent自动切换协程，避免io操作的等待"


import time
import gevent
#    g1=gevent.spawn(a)  spawn是gevent里的
from gevent import monkey #monkey不是

monkey.patch_all()#只要有延迟，先执行下一步

def a():#任务a
    for i in range(5):
        print('a'+str(i))
        time.sleep(0.2)
def b():#任务b
    for i in range(5):
        print('b'+str(i))
        time.sleep(0.2)
def c():#任务c
    for i in range(5):
        print('c'+str(i))
        time.sleep(0.2)

if __name__ == '__main__':
    g1=gevent.spawn(a)##放进协程的“池子”
    g2=gevent.spawn(b)
    g3=gevent.spawn(c)

    g1.join()
    g2.join()
    g3.join()

print('*'*10)
###############################
"协程案例"
import requests#爬虫模块
import gevent
from gevent import monkey
monkey.patch_all()

def download(url):
    response=requests.get(url)
    content=response.text
    print('下载了{}的数据，长度{}:'.format(url,len(content)))
urls=['http://www.163.com','http://www.qq.com','http://www.baidu.com']

if __name__ == '__main__':
    g1=gevent.spawn(download,urls[0])
    g2=gevent.spawn(download,urls[1])
    g3=gevent.spawn(download,urls[2])
    # g1.join()
    # g2.join()
    # g3.join()
    gevent.joinall((g1,g2,g3)) #一起阻塞 joinall的参数是列表











