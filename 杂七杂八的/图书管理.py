
library=[    {'书名 ':'活着','作者 ':'余华','价格 ':500,'库存 ':5},
             {'书名 ':'笑着','作者 ':'张三','价格 ':100,'库存 ':8},
             {'书名 ':'我的26岁女房客','作者 ':'坦克','价格 ':1000,'库存 ':7},
             {'书名 ':'我在风花雪月里等你','作者 ':'大坦克','价格 ':758,'库存 ':5},
             {'书名 ':'我爱你','作者 ':'于光中','价格 ':500,'库存 ':9}]
def main():#主程序
    print('欢迎来到图书管理系统')
    while 1:
        try:
            answer=int(input("请选择功能序号\n1 查询(书名/作者) 2 借书 3 还书 4 查看所有书 5 退出:"))
        except:
            print('请输入功能序号,别瞎几把输')
        else:
            if answer==1:
                lookfor_book()
            elif answer==2:
                borrow_book()
            elif answer==3:
                returen_book()
            elif answer==4:
                check_book()
            elif answer==5:
                break
            else:
                print('请输入功能序号,别瞎几把输')
def lookfor_book():#查要借的书
    booklist=[]
    ans1=input('请输入你要查询的书名或作者：')
    print('查询结果如下')
    for book in library:
        for key,value in book.items():
            if ans1==book[key]:
                print(book)
                booklist.append(book)
        return book
def borrow_book():#借书
    message=('请选择你要借的书\n输入序号：')
    chioce=int(input(message))-1
    for i in len(lookfor_book()):
        if chioce==i:

def returen_book():#还书
    #还书后 相应的增加
    pass

def check_book():#查看图书馆的书
    for i in library:
        print(i)
main()
####有bug 进入程序不能借书  借了后图书馆对应的库存没法减少