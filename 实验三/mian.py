'''
str1='www.hufe.edu.cn'
str2=str1[:3:1]
print(str2)
str2=str1[12::1]
print(str2)
str2=str1
print(str2)
str2=str1[7::1]
print(str2)
str2=str1[2]
print(str2)
print("str1的长度为：",len(str1))
str2=str1.replace('.','-')
print(str2)
t="123"
t1=t[::-1]
print(t1)
str2=str1.split('.',4)
print(str2)
'''
'''
a ="aAsar3ide4bgs7Dlsf9eAF"
print("i第一次出现的位置为：",a.find('i'))
print("a出现代次数为：",a.count('a'))
print(a.swapcase())
str1=a[::-1]
print(str1)
'''
'''
str1=input()
str1=str1.split(' ')
str2=''
for x in range(len(str1)):
    str2=str2+str1[x][0]
print(str2)
'''
'''
months ="JanFebMarAprMayJunJulAugSepOctNovDec"
number=eval(input())*3
monthsv=months[number-3:number]
print(monthsv)
'''
'''
money=input("请输入要兑换的人民币币值，以￥结束：")
money=float(money.replace('￥',''))
print("{}元人民币可以兑换{:.2f}美元".format(money,money*0.146))
'''
'''
dollar=input("请输入要兑换的美元币值，以$结束:")
dollar=float(dollar.replace('$',''))
print("{}美元可以兑换人民币{:.2f}元".format(dollar,dollar*6.868))
'''
money=input("请输入要兑换的货币币值，可以以¥或$结束：")
symbol=money[-1];
money=float(money[:-1:1])
if symbol=='¥':
    print("{}元人民币可以兑换{:.2f}美元".format(money,money*0.146))
elif symbol=='$':
    print("{}美元可以兑换人民币{:.2f}元".format(money,money*6.868))
else:
    print("无该{}汇率换算".format(symbol))
