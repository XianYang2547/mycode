## 猜数
'''
产生随机数，可以猜多次 直到猜对为止，猜错了给出提示
统计猜了多少次
1次就中  2-5次中  6次中  的运气提示
'''
import random
ran=random.randint(1,50)
count=0
print(ran)
while 1:
    ans=int(input('输入你要猜的数1，50之间\n：'))
    count+=1
    if ans==ran and count==1:
        print('1次就猜对了')
        break
    if count>=2 and count<=5:
        if ans<ran:
            print('猜小了')
        elif ans>ran:
            print('猜大了')
        else:
            print('猜对了，运气还可以噻')
            break
    else:
        if ans<ran:
            print('猜小了')
        elif ans>ran:
            print('猜大了')
        else:
            print('猜对了，运气一般啊')
            break





