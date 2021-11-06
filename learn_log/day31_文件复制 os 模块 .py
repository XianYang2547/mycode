'''
with open() as *
文件完整路径\会转义。用这个  open（r'路径'） 路径前加r
'''
'''
os.path常用函数
    dirname() 获取指定文件的目录
    join()拼接获取新的路径
    split()分隔文件目录和文件名
    getsize()获取文件大小
    isabs()判断是否上绝对路径
    isfile()判断是否是文件
    isdir()判断是否是文件夹
os模块下方法
os.getcwd()获取当前目录
os.listdir()浏览文件夹
os.mkdir()创建文件夹
os.rmdir()删除空的文件夹
os.remove()删除文件
os.chdir()切换目录
'''
import os

with open(r'E:\PYTHON\PythonCharm_code\lingxia.jpg', 'rb') as f:  # 打开文件  默认读文本文档，因为是图片 用rb 当二进制来读
    container = f.read()  # 全部读取
    "有时后不知道文件名字，通过以下获取名字" \
    "用f.name 得到完整的路径，再找到最后一个\的位置，截取的时候位置加1"
    file = f.name
    x = file.rfind('\\')  # 挂2个\转义
    print(file[x + 1:])  # lingxia.jpg
    # 将某个文件复制到当前路径
    path = os.path.dirname(__file__)  # 获取当前路径，返回一个字符串
    path1 = os.path.join(path, 'Lx.jpg')  # 给字符串拼接上文件名和后缀，传入open函数
    # 将某个文件复制到指定路径
    # with open(r'E:\PYTHON\PythonCharm_code\杂七杂八的\lingxia.jpg', 'wb') as m:  # 打开某个文件 没有就创建 要复制的路径和名字
    with open(path1, 'wb') as m:
        m.write(container)  # 将上面读入的 写入
path = r'E:\PYTHON\PythonCharm_code\lingxia.jpg'
result = os.path.split(path)
print(path)
'https://blog.csdn.net/menghuanshen/article/details/79055994?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522162821710816780262577310%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=162821710816780262577310&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduend~default-1-79055994.pc_v2_rank_blog_default&utm_term=os%E6%A8%A1%E5%9D%97+python&spm=1018.2226.3001.4450'
t = (1, 2, 3, 4, 5)
print(t[1:4])



#复制文件夹
def copy(nowfile, aimfile):
    if os.path.isdir(nowfile) and os.path.isdir(aimfile):  # 判断是不是文件夹
        filelist = os.listdir(nowfile)  # 把文件夹里的东西 放在一个列表里，便于遍历  ['新建文件夹', '新建文本文档 (2).txt', '新建文本文档 (3).txt', '新建文本文档.txt']
        for file in filelist:
            path = os.path.join(nowfile, file)  # 给路径加上文件名，返回字符串，便于传给open

            if os.path.isdir(path):  # 判断是不是文件夹
                os.mkdir(os.path.join(aimfile,file))# 在目标路径创建个文件夹
                copy(path, os.path.join(aimfile,file))  # 递归调用  一个参数是path  一个是目标路径
            else:
                with open(path, 'rb') as f:
                    container = f.read()#读入内容

                    path1 = os.path.join(aimfile, file)#拼接一个目标路径，传给下面的open
                    with open(path1, 'wb') as ff:
                        ff.write(container)
        else:
            print('复制完毕')

nowfile = 'E:\PYTHON\PythonCharm_code\学习日志\p1'
aimfile = 'E:\PYTHON\PythonCharm_code\杂七杂八的\p2'
copy(nowfile, aimfile)









