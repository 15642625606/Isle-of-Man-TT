'''
编写程序，完成“名片管理器”项目
需要完成的基本功能：
添加名片
删除名片
修改名片
查询名片
退出系统
程序运行后，除非选择退出系统，否则重复执行功能
'''


def main():
    print("*"*50)
    print("欢迎进入名片管理器".center(35))
    print("                 1.添加名片\n"
          "                 2.删除名片\n"
          "                 3.修改名片\n"
          "                 4.查询名片\n"
          "                 5.退出系统")
    print("*"*50)
    print()

def add():
    name = input("姓名：")
    QQ = input("QQ：")
    iphone = input("联系电话：")
    address = input("联系地址：")
    mp_dict = {}
    mp_dict["name"] = name
    mp_dict["QQ"] = QQ
    mp_dict["iphone"] = iphone
    mp_dict["address"] = address
    mp_list.append(mp_dict)
    print("添加成功：\nname:%s\nQQ:%s\niphone:%s\naddress:%s" % (name, QQ, iphone, address))
    # print(mp_list)

def del_test():
    name = input("请输入要删除的姓名：")
    j = 0
    for temp in mp_list:
        if name == temp["name"]:
            del mp_list[j]
            print("删除成功")
            # print(mp_list)
        else:
            print("无此人信息")
            break
        j += 1

def rename():
    new_name = input("请输入要修改的姓名：")
    for temp in mp_list:
        if new_name == temp["name"]:
            print("已找到此人信息，请进行操作：")
            new_name1 = input("请输入修改后的姓名：")
            new_QQ = input("请输入修改后的QQ：")
            new_iphone = input("请输入修改后的iphone：")
            new_address = input("请输入修改后的adress：")
            temp["name"] = new_name1
            temp["QQ"] = new_QQ
            temp["iphone"] = new_iphone
            temp["address"] = new_address
            print(mp_list)
            break
    else:
        print("无此人信息")

def chaxun():
    find_name = input("请输入要查询的姓名：")
    for temp in mp_list:
        if find_name == temp["name"]:
            print("已找到", 'name:', temp['name'], 'QQ:', temp['QQ'], 'iphone:', temp['iphone'], 'address:',
                  temp['address'])
            break
    else:
        print("无此人信息")

main()
mp_list = []

while True:
    try:
        i = input("请输入选项：")
        i = int(i)
        if i == 1:
          add()
        elif i == 2:
            del_test()
        elif i == 3:
            rename()
        elif i == 4:
            chaxun()
        elif i == 5:
            print("结束运行")
            break
    except:
        print("异常输入")