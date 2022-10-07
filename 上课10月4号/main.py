'''
string="zxcvbnmasdfghjklqwertyuiop1234567890ZXCVBNMASDFGHJKLQWERTYUIOP"
a=b=c=0
for x in string:
    if x.islower():
        a+=1
    elif x.isupper():
        b+=1
    elif x.isdigit():
        c+=1
    else:
        print("该字符不属于大小写字母和数字")
print("大写字母有{}个，小写字母有{}个，数字有{}个".format(a,b,c))
'''

'''
sum=0;
for x in range(101):
    sum+=x
print(sum)
'''

'''
singular=even=0;
for x in range(101):
    if x%2==0:
        even+=x
    else:
        singular+=x
print("单数为{}，偶数为{}".format(singular,even))
'''

'''
n=eval(input("输入整数："))
for x in range(1,n+1):
    if n%x==0:
        print(x)
'''
count=0;
sum=0;
while(1):
    x=eval(input("输入一个值，当小于零时退出算平均值："))
    if x>=0:
        sum+=x
        count+=1
    else:
        break
print("平均值：{}".format(sum/count))