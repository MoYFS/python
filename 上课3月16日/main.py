# import csv
# with open("studentname.csv",'a',newline='') as file:
#     witer=csv.writer(file)
#     witer.writerow(['张芳','女','19'])
#     witer.writerow(['王虎','男','19'])

# try:
#     a=int(input("a="))
#     b=int(input("b="))
#     c=a/b
# except ZeroDivisionError:
#     print("除数不能为0！")
# else:
#     print("c=",c)


import os
os.chdir(r'd:\pyprojects\上课3月16日')
try:
    file=open("data.txt",'r')
except IOError:
    print("data.txt不存在！")
else:
    r=file.read()
    print("data.txt内容为\n",r)
    file.close()