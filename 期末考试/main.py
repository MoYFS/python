#第一题
# temp=(input("输入：")).split(' ')
# print("输出：\n我的名字是{}，来自{}，我的爱好是{}！".format(temp[0],temp[1],temp[2]))

#第二题
# temp=input("输入:")
# for i in range(len(temp)):
#     if 'a'<=temp[i]<='z':
#         print(chr((ord(temp[i])+3)),end='')
#     elif 'A'<=temp[i]<='Z':
#         print(chr((ord(temp[i])+5)),end='')
#     else:
#         print(temp[i],end='')

#第三题
# s=(input("输入：")).split('.')
# if len(s)<4:
#     print("NO")
# else:
#     for i in s:
#         if int(i)<0 or int(i)>255:
#             print("NO")
#             break
#     else:
#         print("Yes")

#第四题
# import random
# temp=("B C E F G H J K M P Q R T V W X Y 2 3 4 6 7 8 9").split(' ')
# n=eval(input("输入："))
# for i in range(n):
#     temp1=""
#     for x in range(5):
#         for m in range(5):
#             temp1+=random.choice(temp)
#         temp1+='-'
#     temp1=temp1[0:len(temp1)-1:]
#     print(temp1)

#第五题
# lst_floor=[1,4,2,7,3]
# print("（1）输出电梯的运行路线（↑表示上一层，↓表示下一层），结果：")
# temp=lst_floor[0]
# for i in lst_floor:
#     temp1=i-temp
#     if temp1>0:
#         for m in range(temp1):
#             print("↑",end='')
#     elif temp1<0:
#         for m in range(-temp1):
#             print("↓",end='')
#     temp=i
# print("\n第二题")
# lst="↑↑↓↓↓↑↑↓↑↑↑↑"
# k=2
# print(k,',',end='')
# for i in lst:
#     if i=='↑':
#         k+=1
#         print(k,',',end='')
#     if i=='↓':
#         k-=1
#         print(k,',',end='')

#第六题
# goods=[
# {"name":"电脑","price":4999},
# {"name":"鼠标","price":80},
# {"name":"游艇","price":200000},
# {"name":"别墅","price":2000000}]
# property=eval(input("输入：\n资产："))
# xuhao=eval(input("序号："))
# print("输出：")
# if xuhao>len(goods):
#     print("无该序号！")
# else:
#     for i in range(len(goods)):
#         print("{} {}".format(i,goods[i]["name"]))
#     if goods[xuhao]["price"]>property:
#         print("账户余额不足,先去赚钱吧！")
#     else:
#         print("恭喜你成功购买一个某商品")

#第七题
dic1 = {'Tom':21,'Bob':18,'Jack':23,'Ana':20}
dic2 = {'李雷':21,'韩梅梅':18,'小明':23,'小红':20}
n = int(input())
if n > len(dic1):
    n = len(dic1)
print ( sorted(dic1.keys())[:n])
print( sorted(dic2.items(), key = lambda item:item[1])[:n])

#第九题
# temp=input("输入：\n")
# if len(temp)<32 or len(temp)>32:
#     print("data error!")
# for i in temp:
#     if i>1 or i<0:
#         print("data error!")
# i=0
# while(1):
#     if i<len(temp):
#         print(int(temp[i:i+8:],2),end='')
#     else:
#         break
#     print(".",end='')
#     i+=8