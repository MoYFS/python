
'''
number=eval(input("输入一个数："))
for i in range(1,number):
    if number%i==0 and i!=1:
        print("{}不是一个素数".format(number))
        break
else:
    print("{}是一个素数".format(number))
'''
import time

'''
for i in range(1,10):
    for x in range(1,i+1):
        print("{}*{}={}".format(x,i,x*i),end=" ")
    print()
'''

'''
for x in range(1,301):
    for i in range(1,x):
        if x%i==0 and i!=1:
            break
    else:
        print("{}是一个素数".format(x))
'''

'''
import random
degree=eval(input("输入测试次数："))
cout=0;
for x in range(degree):
    random.seed(time.time())
    i=random.randint(1,6)
    z=random.randint(1,6)
    if z+i==6:
        cout+=1
print("获胜概率为{},{}".format(cout/degree,cout))
'''

'''
import random
money=10
cout=0;
while(money>=0):
    #random.seed(time.time())
    i=random.randint(1,6)
    z=random.randint(1,6)
    cout+=1
    if z+i==7:
        money+=4
    else:
        money-=1
    print("还剩{}元，游玩{}次".format(money,cout))
'''
