import random
print('*'*30)
print('欢迎来到骰子大富翁游戏')
print('*'*30)
class Game():
    def __init__(self):
        self.name=''
        self.gold_coin=''
    def game(self):
        #游戏主程序
        #输入用户名字以及初始化金币
        gold_coin=0
        username=input('注册游戏送1个金币，输入你的用户名：')
        ##检查你的金币 提示充钱
        gold_coin+=1
        if gold_coin<=5:
            message='请先充钱\n比如：冲10快得20金币\玩一局消耗5个金币'
            print(message)
            while 1:
                try:
                    coin=int(input('输入充值的数目：'))
                except:
                    print('不要瞎几把输，请输入10的整数倍')
                else:
                    gold_coin+=coin*2
                    print('你目前的金币为：{}'.format(gold_coin))
                    ans=input('请主要！！！按q退出,按其他的就继续充钱')
                    if ans=='q':
                        break
        if gold_coin>=5:
            print('即将进入游戏...')
        count=0
        while 1:
            gold_coin-=5
            count+=1
            print('游戏开始，金币-5你现在有{}金币'.format(gold_coin))
            print('正在随机化骰子点数....')
            x1=random.randint(1,6)
            x2=random.randint(1,6)
            print('请猜大小')
            guess=int(input('请输入大|小，用1和0表示：'))
            if guess==1 and x1+x2>=6:
                gold_coin+=2
                print('你猜对了,金币加2目前金币为{}'.format(gold_coin))
            elif guess==0 and x1+x2<6:
                gold_coin+=2
                print('你猜对了,金币加2,目前金币为{}'.format(gold_coin))
            else:
                print('猜错了，没有奖励')
            print(x1,x2)
            print('*'*10)
            if count%5==0:
                print('你玩了{}局啦，可以选择退出了'.format(count))
                try:
                    ans=input('按q退出游戏,输入其他的继续游戏')
                except:
                    print('继续游戏....')
                else:
                    if ans=='q':
                        print('你的金币是{}，你总共玩了{}局'.format(gold_coin,count))
                        break


#调用
f=Game()
f.game()





















