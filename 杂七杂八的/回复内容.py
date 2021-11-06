'''
要求：
反复回复：
1.回复的内容不能为空、
2. 不能存在一些敏感词汇
3. 最多评论20个字
4.回复的内容不能有空格
'''

#看到一个漂亮的小姐姐，要不要表白
while 1:
    name=input('输入你的名字：')
    re=[]
    mes=input('输入你的回复：')
    re.append(mes)
    list1=['fuck','shit','操','草']
    if mes=='':
        print('你不能输入空内容')
    if len(mes)>20:
        print('你不能输入超过20个字')
    for i in re:
        for  j in list1:
            if j in i:

                print('不能输入敏感词汇')
    for i in mes:
        if i ==' ':
            print('输入的内容不能有空格')

