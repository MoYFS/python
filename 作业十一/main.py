#第一题
# def isOdd(temp):
#     if temp%2==1:
#         return True
#     else:
#         return False
# print(isOdd(2))

#第二题
# def receive(temp):
#     lst=[k for k in temp if k>(sum(temp)/len(temp))]
#     lst.insert(0,sum(temp)/len(temp))
#     return tuple(lst)
# Data=list(map(int , input("输入任意多个实数：").split(' ')))
# print(receive(Data))

#第三题
def acronym(temp:str):
    temp=temp.split()
    return (''.join([k[0] for k in temp])).upper()
Data=input("输入字符串：")
print("{}的首字母缩写为：{}".format(Data,acronym(Data)))



