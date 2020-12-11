'''
接收用户输入的生日，判断用户的星座
("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''

chinese_zodiacs = "鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪"
zodiac = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,19),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

chinese_zodiacs_dict = {}
for chinese_zodiac in chinese_zodiacs:
    chinese_zodiacs_dict[chinese_zodiac] = 0


times = [0,0,0,0,0,0,0,0,0,0,0,0]
chinese_zodiacs = "鼠、牛、虎、兔、龙、蛇、马、羊、猴、鸡、狗、猪"
for time,chinese_zodiac in zip(times,chinese_zodiacs):
    chinese_zodiacs_dict[chinese_zodiac] = time

#字典推导式
chinese_zodiacs_dict = {chinese_zodiac:0 for chinese_zodiac in chinese_zodiacs}
zodiac_dict = {zodiac:0 for  zodiac in zodiac}


while True:
    year = int(input("请输入您的出生年份"))
    month = int(input("请输入您的出生月份"))
    day = int(input("请输入您的出生日期"))

    num = 0
    for  zodiac_day in zodiac_days:
        if(month,day) > zodiac_day:
            num += 1
        elif month == 12 and day > 22:
            num = 0

    chinese_zodiacs_dict[chinese_zodiacs[year%12]] += 1
    zodiac_dict[zodiacs[num]] += 1


    print(chinese_zodiacs_dict)
    print(zodiac_dict)
