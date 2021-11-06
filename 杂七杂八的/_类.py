class Refrigerator:###Refrigerator 冰箱
    def __init__(self):#就跟一个self都行，可以在下面加
        self.food = []
        self.name = input('第一次使用冰箱，请给它起个名字：')
        f = open('{}.txt'.format(self.name),'a')
        f.close()
        while True:
            operate = input('欢迎使用{}冰箱，请输入对应序号执行操作：1.查询冰箱食物，2.放入食品，3.取出食品：'.format(self.name))
            if operate == '1':
                self.find_food()
                print(self.food)
            elif operate == '2':
                self.put_food()
            elif operate == '3':
                self.get_food()
            Next = input('是否继续操作？（n结束，任意键继续）')
            if Next == 'n':
                print('感谢使用{}冰箱，欢迎下次再来！'.format(self.name))
                break

    def find_food(self):
        self.food = []
        f = open('{}.txt'.format(self.name),'r')
        for food in f.readlines():
            self.food.append(food.strip())
        f.close()

    def put_food(self):
        f = open('{}.txt'.format(self.name),'a')
        self.put_foof_name = input('请输入要放入的食品名称：')
        self.food_num = int(input('请输入要放入的食品数量：'))
        for i in range(self.food_num):
            f.write(self.put_foof_name+'\n')
        print('操作成功')
        f.close()
        self.find_food()
        print(self.food)

    def get_food(self):
        self.find_food()
        self.getfood_name = input('请输入要取出的食品名称：')
        self.getfood_num = int(input('请输入要取出的食品数量：'))
        if not self.getfood_name in self.food:
            print('冰箱里已经没有{}了'.format(self.getfood_name))
        else:
            count = self.food.count(self.getfood_name)
            if self.getfood_num >= count:
                for i in range(count):
                    self.food.remove(self.getfood_name)
            else:
                for i in range(self.getfood_num):
                    self.food.remove(self.getfood_name)
        f = open('{}.txt'.format(self.name),'w')
        for food in self.food:
            f.write(food+'\n')
        f.close()
        self.find_food()
        print(self.food)
refrigerator = Refrigerator()