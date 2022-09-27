'''
number=eval(input("输入一个数："))
if number%2==0:
    print("{}是偶数".format(number))
else:
    print("{}是奇数".format(number))
'''

'''
while(1):
    age=eval(input("输入年龄："))
    if 0<=age<=1:
        print("{}岁是婴儿".format(age))
    elif 1<age<=10:
        print("{}岁是儿童".format(age))
    elif 10<age<=18:
        print("{}岁是青年".format(age))
    elif 18<age<=120:
        print("{}岁是成年人".format(age))
    else:
        print("不是人")
'''

'''
number=eval(input("输入一个数："))
if number%7==0 and number%10==3:
    print("{}同时满足被7整除且最后一位数字为3".format(number))
else:
    print("{}不同时满足被7整除且最后一位数字为3".format(number))
'''

'''
str=input("输入一个字符串")
if str[::1]==str[::-1]:
    print("{}是回文".format(str))
else:
    print("{}不是回文".format(str))
'''

'''
number=input("输入一个正数：")
if int(number)<0:
    print("{}不是正数".format(number))
elif number[0]>=number[1] and number[0]>=number[2]:
    print("{}是{}中最大的值".format(number[0],number))
elif number[1]>=number[2]:
    print("{}是{}中最大的数".format(number[1],number))
else:
    print("{}是{}中最大的数".format(number[2],number))
'''

'''
while(1):
    password=input("输入8位密码，必须包含英文大小写和数字的组合：")
    if len(password)<8:
        print("密码长度不对，请输入8位")
    elif password.isdigit():
        print("密码强度不够，必须包括数字和英文大小写")
    elif password.islower() or password.isupper():
        print("密码强度不够，必须包括英文大/小写")
    else:
        print("恭喜你，密码设置成功！！")
'''