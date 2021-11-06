name='\t吾之初♥，\n永世不忘   '
print(name)
print(name.lstrip())#去除左边空白
print(name.rstrip())#去除右边空白
print(name.strip())#去除两边的空白

with open('1234.txt','w') as f:#打开文件 没有就创建
    kk.append(f.write('i love pytgon\n'))#写入不堪入目的的东西
    kk.append(f.write(str(123456)))
for i in kk:
    print(i)