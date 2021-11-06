import random
car_park=[]
#car_park=[{车牌号：[时间]},{},{}]
def enter():
    print('欢迎进入停车场')
    number=input('输入车牌号')
    #车牌号 和进入出去时间存为字典
    car={}
    x=random.randint(0,10)
    car[number]=[x]
    car_park.append(car)#进来的小时随机确定，要比出去的小
def out():
    number=input('输入车牌号')
    #判断你的车牌号是否在停车场里
    for car in car_park:
        if number in car:#此时的car是一个字典 number是输入的，没有int 打印出来是'123'，它就等于字典的键
            #生成随机数代表停了多长时间
            time=random.randint(10,24)
            #得到进入停车长的时间
            time_record=car.get(number)#由车牌号（键）得到相应的值  是一个列表
            time_record.append(time)
            parktime=time_record[1]-time_record[0]#计算出去的时间减去进来的时间
            total=parktime*4
            print('{}停车{}小时，应缴费{}'.format(number,parktime,total))
            break#不执行下面的了
    else:
        print('车未进场')
enter()
out()
