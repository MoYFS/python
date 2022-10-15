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
cout=0
for x in range(101,201):
    for i in range(1,x):
        if x%i==0 and i!=1:
            break
    else:
        cout+=1
        print("{}是一个素数".format(x))
print("一共有{}个素数".format(cout))
