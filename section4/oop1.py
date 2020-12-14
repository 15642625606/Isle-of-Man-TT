'''
    类的定义
'''
class MyCar:
    pass

class Car(object):
    #方法
    def getCarInfo(self):
        print("这是一辆红色的smart")
    #移动
    def move(self):
        print("车在行驶")
    #鸣笛
    def toot(self):
        print("车在鸣笛...")



BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = 4 #轮子数量
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
