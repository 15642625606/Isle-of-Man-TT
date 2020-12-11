'''
编写程序，完成以下要求：
统计字符串中，各个字符的个数
比如：“hello world” 字符串统计的结果为： h:1 e:1 l:3 o:2 d:1 r:1 w:1
'''

aStr = input("请输入您的字符串，我们将进行字符串统计：")
list = list(aStr)       #字符串转列表
print(list)
count = dict()          #dict()函数用于创建一个字典
for item in list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
print(count)