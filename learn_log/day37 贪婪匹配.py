import re
#默认是贪婪的  匹配到abc后，再匹配数字，+号匹配1个或多个
msg='abc123hhhh'
result=re.match(r'abc\d+',msg)
print(result)#<re.Match object; span=(0, 6), match='abc123'>
#改成非贪婪  abc\d+? 加上了问号，abc1 也是满足正则的
result=re.match(r'abc\d+?',msg)
print(result)#<re.Match object; span=(0, 4), match='abc1'>



path='<img src="https://img-home.csdnimg.cn/images/20210816091943.png" alt="" data-v-e8da5228="">'
result=re.match(r'<img src="(.+?)"',path)#只匹配一个" "里的内容
image=result.group(1)#https://img-home.csdnimg.cn/images/20210816091943.png
import requests#导入爬虫模块
response=requests.get(image)#模拟下载
with open('down_picture.jpg','wb') as f:
    f.write(response.content)#写入
