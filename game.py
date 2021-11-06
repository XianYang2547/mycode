#% %%%%%%%%%%%%%%%%%%%%%%%%%%选择人物%%%%%%%%%%%%%%%%%%%%%%%%%%%
import random
print('*'*40)
print('欢迎来到氦金游戏')
print('*'*40)
print('请选择你的英雄')
people=('赌马','赌球','赌球二代','隐藏方案','冰冰')
print(people)
coins=750000
beibao=[]
while 1:
	try:
		choose=int(input('请选择游戏人物(输入对应的序号12345)'))
		for i in range(1,6):
			if choose==i:
				p=people[i-1]
				print('你选择的是'+people[i-1])
		break
	except:
			print('你在瞎几把输')
print('欢迎{}来到氪金游戏世界，你的初始金币是{}'.format(p,coins))
print('&'*20)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%选择功能%%%%%%%%%%%%%%%%%%%%%%%%%%%
while 1:
	print('进入游戏功能选择')
	print('1.购买好东西  2.干架  3.删除  4. 查看  5. 退出')
	choice=int(input('请选择：'))
	if choice==1:
		print('进入shopping')
		wuqi=[['大棒',50000],['大棒1号',40000],['某棒',30000],['某套',20000],['小内',15000]]
		print(wuqi)
		choice=int(input('请输入要购买的好东西序号(12345):'))
		for i in range(1,6):
			if choice ==i:
				print(wuqi[i-1])
				answer=input('你确定要购买吗1/2:')
				if answer=='1' and coins>=(wuqi[i-1][1]):
					print('购买成功')
					coins-=(wuqi[i-1][1])
					beibao.append(wuqi[i-1][0])
					print('你买了{},还剩{}金币'.format(wuqi[i-1][0],coins))
				else:
					print('欢迎下次来购买')
	elif choice==2:
		if beibao==[]:
			print('你什么都没买，去买个好东西再来吧')
		else:
			print('请使用你购买的好东西来干架吧,进入背包中...\n','你背包里有：\n',beibao)
			zhandouli=0
			while 1:
				j=int(input('输入你背包里的好东西的顺序，并装备它:'))		
				if 	j>len(beibao): #or j.isalpha()==1:
					print('你的输入超出了你背包容量')
				elif beibao[j-1] == wuqi[0][0]:
					zhandouli+=50
					break
				elif beibao[j-1] == wuqi[1][0]:
					zhandouli+=40
					break
				elif beibao[j-1] == wuqi[2][0]:
					zhandouli+=30
					break
				elif beibao[j-1] == wuqi[3][0]:
					zhandouli+=20
					break
				elif beibao[j-1] == wuqi[4][0]:
					zhandouli+=10
					break
			print('你已经装备了{}'.format(beibao[j-1]))
			print('即将进入PK....')
			print('你的对手是：终极舔狗')
			s1=random.randint(1,100)
			s2=random.randint(1,100)
			if coins>=10000:
				if s1>(s2+zhandouli):
					print('华仔胜,你扣除10000金币')
					coins-=10000
					print('你的金币还有{}'.format(coins))
				elif s1<(s2+zhandouli):
					print('你赢啦，金币加20000')
					coins+=20000
					print('你的金币还有{}'.format(coins))
				else:
					print('平局')
				print('华仔本场战斗力：',s1,'你的战斗力',s2,'你的装备加成为：',zhandouli,'你总共战斗力为:',s2+zhandouli,'*'*20)
			else:
				print('你金币不足，无法PK，快去卖PY吧')

	elif choice==3:
		print('正在进入删除**页面...')
		if beibao==[]:
			print('你这里面啥没有')
		else:
			print('选择你要删除的**：\n',beibao)
			answer=int(input('输入你要删除的物品序号:'))
			if answer in range(len(wuqi)):
				del beibao[answer-1]
				coins+=(wuqi[i-1][1])
				print('你的背包里还有：',beibao,'你的金币还有',coins)
			else:
				print('输入错误，已返回游戏功能列表')

	elif choice==4:
		print('正在进入背包查看你的**....')
		if beibao==[]:
			print('你这里面啥没有')
		else:
			print('你已经拥有了：',beibao)

	elif choice==5:
		print('你正在选择退出')
		answer=input('Y/N：')
		if answer=='Y':
			break
	else:
		print('输入错误，请重新输入')