# def fun(a, b, opt):
#     print 
#     "a =", a
#     print 
#     "b =", b
#     print 
#     "result =", opt(a, b)

# fun(1, 2, lambda x,y:x+y)
# a = 1
# b = 2
# result = 3


stub = [
    {"name":"hangman", "age":18}, 
    {"name":"lis", "age":19}, 
    {"name":"wang", "age":17}
]

#按name排序：
stub.sort(key = lambda x:x['name'])
stub
[{'age': 19, 'name': 'lis'}, {'age': 17, 'name': 'wang'}, {'age': 18, 'name': 'hangman'}]

#按age排序：
stub.sort(key = lambda x:x['age'])
stub
[{'age': 17, 'name': 'wang'}, {'age': 18, 'name': 'hangman'}, {'age': 19, 'name': 'lis'}]

