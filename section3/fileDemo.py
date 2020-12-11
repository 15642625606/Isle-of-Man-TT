'''
读取name.txt中的名字，存放在列表中
'''
from typing import names

f = open('./name.txt','r+')
print(f.read().split("|"))

for name in names:
    print(name)



'''
读取weapon.txt中的武器
'''
f1 = open('./weapon.txt','r+',encoding="utf-8")
#print(f1.readlines())
index = 0
for line in f1.readlines():
    data = line.strip()
    if index%2 == 0:
        print(data)
    index += 1



'''

'''