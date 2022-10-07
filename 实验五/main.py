
'''
a=1
for x in range(1,11):
    a=a*x
print("1*2*3*.....*10={}".format(a))
'''

'''
data=input("输入十个数以空格隔开")
data=data.rsplit(" ")
sum=0
uneven =0
even=0
for x in data:
    if int(x)%2==0:
        even+=int(x)
        sum+=int(x)
    else:
        uneven+=int(x)
        sum+=int(x)
print("奇数和为{}，偶数和为{},平均数为{}".format(even,uneven,sum/10))
'''

'''
sum=0
for x in range(1,101):
    if x%3==0 and x%5==0:
        sum+=x
print("100以内的被3和5整除的数之和为{}".format(sum))
'''

'''
print("水仙花数有：",end="")
for x in range(100,1000):
    if x==((x-x%100)/100)**3+((x%100-x%10)/10)**3+(x%10)**3:
        print(x,end=" ")
'''

'''
str=input("输入字符串：")
digit=majuscule=minuscule=blank=other=0
for x in str:
    if x.isdigit():
        digit+=1
    elif x.isupper():
        majuscule+=1
    elif x.islower():
        minuscule+=1
    elif x==" ":
        blank+=1
    else:
        other+=1
print("{}字符串中数字{}个，大写字母{}个，小写字母{}个，空格{}个，其他字符{}个".format(str,digit,majuscule,minuscule,blank,other))
'''
while(1):
    data=input("输入基本数据（包括年龄，工作经验，所学专业用空格间隔，输入负数则退出判断）：\n")
    if data<"0":
        print("退出程序")
        break
    else:
        data=data.rsplit(" ")
        if eval(data[0])<25 and data[2]=="计算机":
            print("获得面试机会")
        elif eval(data[1])>4 and data[2]=="电子":
            print("获得面试机会")
        elif data[2]=="通信":
            print("获得面试机会")
        else:
            print("抱歉，您不符合面试要求")

