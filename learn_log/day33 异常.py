'''
关键字	    关键字说明
try/except	捕获异常并处理
pass	    忽略异常
as	        定义异常实例（except MyError as e）
else	    如果try中的语句没有引发异常，则执行else中的语句
finally	    无论是否出现异常，都执行的代码   长把一些需要关闭的代码放在这里面 比如   f.close（）
raise    	抛出/引发异常

'''
'''
1           捕获所有异常
try:
     <语句>
except:
      print('异常说明')
      
2           捕获指定异常
try:
     <语句>
except <异常名>:
      print('异常说明')
      
3           万能异常
try:
     <语句>
except Exception:
      print('异常说明')      
'''
#用这个也可
try:
    pass
except Exception as err:
    print(err)#err的内容就是错误原因
##########################################################################################################
"采用traceback模块查看异常"'可以知道是在哪个文件哪个函数哪一行出的错'
import traceback

try:
    1/0
except Exception as e:
    traceback.print_exc()



