#第一题
"""
revenue=98765
costs=40000
profit=revenue-costs
print(profit)
"""
#第二题
"""
math=80
chinese=85
english=75
print(" 总分：",english+chinese+math,'\n',"平均分：",(english+chinese+math)/3)
"""
#第三题
"""
import math
radius=float(input())
print(" 球的表面积为：%.4f"%(4*math.pi*radius*radius),'\n',"球的体积为：%.4f"%((4*math.pi*radius*radius*radius)/3))
"""
#第四题
"""
name=input("请输入姓名：")
print("姓名：",name)
"""
#第五题
"""
age=int(input(“请输入年龄：”))
print(age+2)
"""
#第六题
"""
name=input(“请输入姓名：”)
age=int(input("请输入年龄："))
print("哇塞，",name,"今年",age,"岁",sep='')
"""
#第七题
"""
number=int(input("请输入一个数："))
number1=int((number%10))*100+int(((number/10)%10))*10+int(number/100)
print(number1)
"""
#第八题
"""
import math
x=int(input("请输入一个数："))
print(math.cos(x)*math.cos(x)+math.sin(x)*math.sin(x))
"""
#第九题
"""
import math
print("x1=",(-2-math.sqrt(2*2-4*(-3)))/2,"x2=",(-2+math.sqrt(2*2-4*(-3)))/2)
"""
#列表学习
"""
list3=['1','2','3','4','5']
print(list3)
list3.append("nihao")
print(list3)
a='.'.join((list3))
print(a)
"""
"""
a=12
b=234
a=a+b
b=a-b
a=a-b
a,b=b,a
print(a,b)
"""
import turtle
import time
turtle.setup(1080,1080,0,0)
turtle.color('red', 'pink')
turtle.pensize(2)
turtle.penup()
turtle.goto(-128,0)
turtle.pendown()
turtle.setheading(150)
turtle.begin_fill()
turtle.fd(50)
turtle.circle(50 * -3.75, 45)
turtle.circle(50 * -1.431, 165)
turtle.left(120)
turtle.circle(50 * -1.431, 120)
turtle.left(120)
turtle.circle(50* -1.431,120)
turtle.left(120)
turtle.circle(50*-1.431,165)
turtle.circle(50 * -3.75, 45)
turtle.fd(50)
turtle.left(-60)
turtle.fd(50)
turtle.circle(50*-3.75,40)
turtle.left(140)
turtle.circle(50*-3.75,40)
turtle.fd(50)
turtle.end_fill()
time.sleep(10)
