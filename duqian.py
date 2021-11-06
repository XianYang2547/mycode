print('*'*30)
print('欢迎进入澳门赌场！！！')
print('*'*30)
answer =input('确定进入游戏吗(y/n):')
money=0
if answer!='y':
	print('欢迎下次再来')
if answer=='y':
	while money<2:
		n=int(input('请先充值金币（100元10个币，充值数必须是100的倍数）：'))
		if n%100==0 and n>0:
			money=(n//100)*10
	print('当前游戏币为：{}，玩一局游戏需要2个币'.format(money))
	print('进入游戏......')
	while True:
		import random
		t1=random.randint(1,6)
		t2=random.randint(1,6)
		print('系统洗牌完毕，请猜大小：')
		money-=2
		guess =input('输入大或小：')
		if ((t1+t2)>6 and guess=='小') or ((t1+t2)<=6 and guess=='大'):
		    money-=2
		    print('提示：金币减少2个,目前金币为：',money)
		if ((t1+t2)>6 and guess=='大') or ((t1+t2)<=6 and guess=='小'):
			money+=1
			print('恭喜你获得1个金币，目前金币为：',money)
		print('本轮结果展示:{}'.format(t1))
		print('本轮结果展示:{}'.format(t2))
		print()
		if money <2:
			print('金币不足请充值!')
			choose=input('是否进行充值？（y/n）')
			if choose == 'y':
				n=int(input('请充值（100元10个币，充值数必须是100的倍数）：'))
				money1=(n//100)*10
				money+=money1
				print('你目前的金币为：{}'.format(money))
			else:
				print('游戏结束！！欢迎下次再来！')
				break