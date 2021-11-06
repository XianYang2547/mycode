#猜拳游戏
'''
三局2胜
'''
import random
n=2
m=0
g=0
while n>=0:
    #规定0是剪刀  1是石头 2 是布
    list0=['剪刀','石头','布']
    guess=int(input('0是剪刀 . 1是石头 .2 是布\n请输入：'))
    print('你出的是{}'.format(list0[guess]))
    # mchine_dict={'剪刀':0,'石头':1,'布':2}
    mchine_number=random.randint(0,2)
    # for key,value in mchine_dict.items():
    #     if mchine_number==value:
    #         print(key)
    print('电脑出的是{}'.format(list0[mchine_number]))
    if (guess==0 and mchine_number==1) or (guess==1 and mchine_number==2) or (guess==2 and mchine_number==0):
        m+=1
        print("电脑赢一局")
    elif (guess==0 and mchine_number==2) or (guess==1 and mchine_number==0) or (guess==2 and mchine_number==1):
        g+=1
        print('你赢了一局')
    else:
        print('平局')
    n-=1
if m==g:
    print('平局')
elif g>m:
    print('我赢了')
else:
    print('电脑赢了')
























