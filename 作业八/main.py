#第一题
# rate=[[2006,0.57],[2007,0.56],[2008,0.57],[2009,0.62],\
#       [2010,0.69],[2011,0.72],[2012,0.75],[2013,0.76],\
#       [2014,0.743],[2015,0.74]]
# su=0
# m=0
# for x in range(10):
#     su=su+rate[x][1]
#     if rate[m][1]<=rate[x][1]:
#         m=x
# print("第一题平均数为{}".format(su/10))
# print("第二题录取率最高的年份为{}".format(rate[m][0]))

#第二题

# l1=[11,22,33,55]
# l2=[22,33,44,66,77]
# l3=[]
# for x in l1:
#     for m in l2:
#         if x==m:
#             l3.append(x)
# print("第一题{}".format(l3))
# l4=l1.copy()
# for m in l3:
#     l4.remove(m)
# print("第二题{}".format(l4))
# l5=l1+l2
# for x in l3:
#     l5.remove(x)
# print("第三题{}".format(l5))

#第三题

# crew=[["王平","男",[1,1,0,0]],["李丽","女",[0,1,0,1]],["陈小梅","女",[0,0,1,0]],\
#       ["孙洪涛","男",[0,1,1,1]],["方亮","男",[1,0,1,0]]]
# count=0
# for x in crew:
#     if x[2].count(1)>=2:
#         count+=1
# print("第一题：有{}人".format(count))
# woman=0;
# for x in crew:
#     if x[1]=="女":
#         woman+=1
# print("第二题：有{}人".format(woman))
# print("第三题：\n")
# for x in crew:
#     if x[2][1]==1:
#         print("姓名:{} 性别：{}".format(x[0],x[1]))

#第四题

# lst=["甲","乙","丙","丁"]
# for x in lst:
#     if (x !="甲")+(x=="丙")+(x=="丁")+(x!= "丁") ==3:
#         print("{}做了好事".format(x))

#第五题

# lst_weather=[["周一","16℃","26℃","多云","1级","优"],\
#              ["周二","17℃","27℃","晴","2级","优"],\
#              ["周三","16℃","28℃","晴","3 级","优"],\
#              ["周四","16℃","25℃","阴","2级","良"],\
#              ["周五","15℃","24℃","阴","2 级","良"],\
#              ["周六","15℃","25℃","晴","3级","优"],\
#              ["周日","14℃","23℃","小雨","3级","良"]]
# you=[x for x in lst_weather if x[5]=="优"]
# print("第一题：\n空气质量为优的天数{}".format(len(you)))
# print("分别是：",end="")
# for x in you:
#     print(x[0],end=' ')
# print()
# fen=[x for x in lst_weather if x[4]<="3级" and x[2]<="25℃"]
# print("第二题:\n风力低于3级且最高气温不超过25℃的天数：{}".format(len(fen)))
# print("分别是：",end="")
# for x in fen:
#     print(x[0],end=' ')
# print()
# qm=[x for x in lst_weather if (int(x[1][:2:])+int(x[2][:2:]))/2<=20]
# print("第三题:\n平均气温低于20℃的天数{}".format(len(qm)))
# print("分别是：",end="")
# for x in qm:
#     print(x[0],end=' ')

#第六题

# student=[['001','李梅',19],['002','韩磊磊',20],['003','张亮',18]]
# student.append(['004','王大锤',20])
# student.append(['006','刘大刀',18])
# print("第一题{}".format(student))
# for x in range(len(student)):
#     if student[x][0]>"005":
#         student.insert(x,['005','赵钱孙',20])
#         break
# print("第二题{}".format(student))
# for x in range(len(student)):
#     if student[x][0]=='004':
#         print("第三题{}".format(student[x]))
# print("第四题：姓名：",end='')
# for x in student:
#     print(x[1],end=' ')
# print()
# print("第五题：")
# for x in student:
#     if x[2]>=19:
#         print(x,end=" ")

#第七题

# s = "I want to study Python perfectly"
# s=s.split(" ")
# for x in range(len(s)):
#     print(s[x],end=' ')
#     if x%2==1:
#         print()

#第八题

food=[("提拉米苏",15),("芝士蛋糕",20),("三明治",10)]
drinks=[("红茶",6),("咖啡",12),("橙汁",8)]
commodity=[]
for x in food:
    for m in drinks:
        commodity.append(tuple([x[0],m[0],round((x[1]+m[1])*0.8)]))
print(commodity)