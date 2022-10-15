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
