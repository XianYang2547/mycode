# 函数的返回值
def add(a, b):
    result = a + b
    return result, result + 2


x, y = add(5, 8)
print(x, y)
'''
   return 后面可以是一个参数,接收的时候x=add(5, 8)   13
          可以是多个参数,将其放在元组中，将元组作为整体返回
          return result,result+2
          (13, 15)
    接收也可以是多个  return result,result+2
                x，y=add(5, 8)   打印的是：x=13 y=15
'''
'''加入购物车
判断用户是否登录，如果登录，成功加入购物车，否则提示登录后添加
成功True 不成功 False
def add_shoppingcart(goodsname)
    pass
def login(username,password)
    pass
    
    
输入用户名xy
输入密码123
登录成功
成功将某棒加入到购物车   
'''
# username=input('输入用户名')
# password=input('输入密码')
# islogin = False # 用于判断用户是否登录的变量  默认没有登录 值为false
#
#
# def login(username,password):
#     if username=='xy' and password=='123':
#         print('登录成功')
#         return True
#     else:
#         print('登录失败')
#         return False
# islogin=login(username,password)#islogin就等于这个函数返回的值，t or f
#
#
# def add_shoppingcart(goodsname):
#     if islogin and goodsname:#if 后面的为真 才继续
#         print('成功将{}加入到购物车'.format(goodsname))
#     else:
#         print('你还没有添加商品')
# add_shoppingcart('某棒')


username = input('输入用户名')
password = input('输入密码')

islogin = False  # 用于判断用户是否登录的变量  默认没有登录 值为false


def login(username, password):
    if username == 'xy' and password == '123':
        return True
    else:
        return False


islogin = login(username, password)


def add_shoppingcart(goodsname):
    global islogin ###
    if islogin:
        if goodsname:  # 如果goodsname不为空
            print('成功将{}加入到购物车'.format(goodsname))
        else:
            print('你还没有添加商品')
    else:
        print('登录失败，要重新登录吗：（y/n）')
        ans=input(':')
        if ans=='y':
            username = input('输入用户名')
            password = input('输入密码')
            islogin = login(username, password)#调用上面的那个函数

add_shoppingcart('某棒')








