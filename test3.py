'''
编写程序，完成以下要求：
完成一个路径的组装
先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share
'''

path = ""
flag = 1
j = 1
while flag:
    aPath = input("请输入路径%d(输入exit终止)："%j)
    if aPath == 'exit':
        path = path[0:-1]
        break
    path =path + aPath + "\\"
    j += 1
print(path)