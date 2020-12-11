#编程实现对一个元素全为数字的列表，求最大值、最小值

#方法1
a = [1,2,3,4,5,6,7,11,10,9,]
i = 1
b = a[0]

while i <= len(a):
    for k in a:
        if b >= k:
            pass
        else:
            b = k
    i +=1
print(b)

#方法2
res = max(a)
print(res)
res = min(a)
print(res)