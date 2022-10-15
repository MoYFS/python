'''
a=eval(input("a为1到9的整数："))
n=eval(input("n为正整数："))
s=0
temp=0
for i in range(1,n+1):
    temp=temp*10+1
    s=s+a*temp
print(s)
'''

'''
count=0
for x in range(101,201):
    for i in range(1,x):
        if x%i==0 and i!=1:
            break
    else:
        count+=1
        print("{}是一个素数".format(x))
print("一共有{}个素数".format(count))
'''

'''
count=uneven=even=0
while(1):
    temp=input("输入整数，当输入A时结束：")
    if temp=='A':
        print("奇数和为{},偶数和为{}，平均数为{}".format(uneven,even,(even+uneven)/count))
        break
    else:
        count+=1
        if int(temp)%2==0:
            even+=int(temp)
        else:
            uneven+=int(temp)
'''

'''
StartValue=10
while(1):
    if StartValue%5==1 and StartValue%6==5 and StartValue%7==4 and StartValue%11==10:
        print("韩信一个拥有{}名士兵".format(StartValue))
        break
    else:
        StartValue+=1
'''

'''
StratValue=day=1
while(day<=365):
    if 0<day%7<=5:
        StratValue*=1.01
    else:
        StratValue*=0.99
    day+=1
print("武力值为{:.2f}".format(StratValue))
'''

'''
for cock in range(20):
    for hen in range(33):
        chick = 100 - cock - hen
        if 5 * cock + 3 * hen + chick / 3 == 100:
            print('公鸡: {}只, 母鸡: {}只, 小鸡: {}只' .format(cock, hen, chick))
'''


'''
import random
import math
#data=random.randint(0,100)
#random.seed(data)
#print("RND1:{},RND2：{}，最大公约数：{}，最小公倍数：{}".format(data,random.randint(0,100),math.gcd(data,random.randint(0,100)),(data*random.randint(0,100))/math.gcd(data,random.randint(0,100))))
#以上为单变量实现版本
RND1=random.randint(0,100)
RND2=random.randint(0,100)
print("RND1:{},RND2：{}，最大公约数：{}，最小公倍数：{}".format(RND1,RND2,math.gcd(RND1,RND2),(RND1*RND2)/math.gcd(RND1,RND2)))
'''

'''
import random
count=eval(input("输入测试次数（建议大于1000次）："))
front=reverse=0
while(count):
    if random.randint(0,1)==1:
        front+=1
    else:
        reverse+=1
    count-=1
print("正面{}次，反面{}次".format(front,reverse))
'''
import random
target=random.randint(1,100)
count=0
while(1):
    temp=eval(input("输入一个100以内的整数："))
    if temp>target:
        count+=1
        print("遗憾，太大了")
    elif temp<target:
        count+=1
        print("遗憾，太小了")
    else:
        count+=1
        print("预测{}次，你猜中了！".format(count))
        break