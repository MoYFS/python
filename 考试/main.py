#第一题
# temp=input("输入成绩，依次为语文、数学、英语用空格间隔：")
# temp=list(map(float,temp.split()))
# print("总分：{}\n平均值：{}\n最高分：{}\n最低分：{}".format(sum(temp),\
#                         round(sum(temp)/len(temp),2),max(temp),min(temp)))

#第二题
# str1 = 'www.hufe.edu.cn'
# print("（1）截取字符串的第一位到第三位的字符:{}".format(str1[:3:]))
# print("（2）截取字符串最后三位的字符:{}".format(str1[-3::]))
# print("3）截取字符串的六个字符:{}".format(str1[:6:]))
# print("（4）输出字符串的长度:{}".format(len(str1)))
# print("（5）将字符串中所有的'.'换成'-'并输出:{}".format(str1.replace('.','-')))
# print("（6）统计字符w出现的次数:{}".format(str1.count('w')))

# #第三题
# a,n=map(int,input("请输入a,n:").split())
# s=temp=0
# for i in range(n):
#     temp=temp*10+1
#     s+=a*temp
# print(s)

#第四题
# lst_busstop=["金星路","西湖公园","溁湾镇","湘江中路","橘子洲","五一广场"]
# dict_place={"金星路":["菜园","早古塘"],"西湖公园":["西湖鱼巷","58小镇"], \
#             "溁湾镇":[ "武警医院","岳麓山"], "湘江中路":[ "老长沙","万达广场"],\
#             "橘子洲":[ "湘江","橘子洲头"], "五一广场":[ "IFS","太平老街"]}
# print(lst_busstop)
# first,second=input("请输入起始站，终点站：").split()
# if not(first in lst_busstop) or not(second in lst_busstop):
#     print("有不属于不属于这条线路的站点")
# else:
#     if lst_busstop.index(first)>lst_busstop.index(second):
#         print("需要乘坐反方向线路")
#     else:
#         print("需乘坐{}站".format(lst_busstop.index(second)-lst_busstop.index(first)))
# temp=input("输入两地点信息：").split()
# for k in dict_place.keys():
#     if dict_place[k]==temp:
#         print("['{}':{}]".format(k,dict_place[k]))
#         break
# else:
#     print("未找到")

# 第五题
def menu():
    print('''\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存''')
    while(1):
        operate=eval(input("输入操作："))
        if operate==1:
            temp=input("输入姓名电话专业P：").split()
            dic[temp[0]]=[temp[1],temp[2]]

        elif operate==2:
            temp=input("输入需删除的姓名：")
            if temp in dic.keys():
                for i in dic.items():
                    print(i)
                print("Success")
            else:
                print("No Record")
            print(dic)

        elif operate==3:
            temp=input("输入需修改的姓名：")
            if temp in dic.keys():
                temp=input("输入信息：").split()
                dic[temp[0]]=[temp[1],temp[2]]
            else:
                print("不存在{}".format(temp))

        elif operate==4:
            temp=input("输入查找的姓名：")
            if temp in dic.keys():
                print("{}:{}".format(temp,dic[temp]))
            else:
                print("{}查无此人！".format(temp))

        elif operate==5:
            for i in dic.items():
                print(i)

        elif operate==6:
            return

        else:
            print("ERROR")

dic={'张自强': ['12652141777', '材料'],\
'庚同硕': ['14388240417', '自动化'],\
     '王岩': ['11277291473', '文法']}
menu()

# import cv2

