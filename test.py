#编程实现对一个元素全为数字的列表，求最大值、最小值

import random
list = []
n = int(input("请输入你想要的数字个数，我们将为您随机生成0-100的数字："))
while n > 0:
    list.append(random.randint(0,100))
    n -= 1
print(list)

max = list[0]
min = list[0]
for value in list:
    if value > max:
        max = value
    if value <min:
        min = value

print("最大值：%d\n最小值：%d"%(max,min))