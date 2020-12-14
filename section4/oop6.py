'''
    id()
    __str__
'''

class Car:
    def __init__(self,name,color='red',wheelNum=4):
        self.name = name
        self.color = color
        self.wheelNum = wheelNum

    def move(self):
        print("%s颜色的汽车在行驶···" %self.color)

    def __str__(self):
        return "我是一辆%s汽车"%self.name

BMW = Car(name="宝马",color= "blue",wheelNum=4)
print(BMW)

Audio = Car(name="奥迪")
print(Audio)

