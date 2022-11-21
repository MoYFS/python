#第一题
# dic_student={}
# for i in range(5):
#     InputData=input("依次输入班级，姓名，年龄，身高和体重")
#     InputData=InputData.split(' ')
#     dic_student[InputData[0]+' '+InputData[1]]=InputData[2]+' '+InputData[3]+' '+InputData[4]
# for x in dic_student.keys():
#     print("{:7}{}".format(x,dic_student[x]))

#第二题
# lst_staff=["李梅","张富","付妍","赵诺","刘江"]
# dic_award={"张富":10000,"赵诺":150000}
# for x in lst_staff:
#     if x in dic_award:
#         print("{:3}年终奖金为{}元".format(x,dic_award[x]))
#     else:
#         print("{:3}年终奖金为5000元".format(x))

#第三题
# dic_repertory={"酱油":50,"醋":60,"盐":100,"糖":120,"鸡精":20,"麻油":40}
# dic_change={"酱油":100,"醋":80,"鸡精":50,"耗油":60}
# for x in dic_change:
#     dic_repertory[x]=dic_change[x]
# print("(1)对字典dic_repertory的内容进行更新并输出dic_repertory:\n{}".format(dic_repertory))
# dic_repertory=sorted(dic_repertory.items(),key=lambda x:x[1],reverse=True)
# print("(2)对更新后的字典按照商品数量进行降序排列，并输出dic_repertory:\n{}".format(dict(dic_repertory)))
# print("(3)输出当前库存数量最多的商品及最少的商品:\n最多：{}\n最少：{}".format\
#           (dic_repertory[0][0],dic_repertory[len(dic_repertory)-1][0]))

#第四题
# user={"小林":"1995","小彦":"0421","小俊":"0824"}
# temp=(input("请输入用户名和密码二者用空格隔开：")).split(" ")
# if temp[0] in user.keys():
#     if(temp[1]==user[temp[0]]):
#         print("登录成功！")
#     else:
#         print("密码不正确！")
# else:
#     print("用户名不正确！")

#第五题
# player=[["012",[90,94,97,86,85,89,88,85]],["005",[91,91,92,98,90,96,90,95]],\
#         ["108",[96,86,97,96,87,86,86,96]],["037",[95,95,94,93,97,98,99,95]],\
#         ["066",[95,87,94,94,93,99,96,97]],["020",[89,97,91,95,89,94,97,92]]]
# result={}
# for x in player:
#     result[x[0]]=round((sum(x[1])-min(x[1])-max(x[1]))/(len(x[1])-2),1)
# result=dict(sorted(result.items(),key=lambda x:x[1],reverse=True))
# for x in result:
#     print("选手{} 分数：{}".format(x,result[x]))

#第六题
dicTXL={'小新':[13913000001,18181220001],\
        '小亮':[13913000002,18191220002],\
        '小刚':[13913000003,18191220003]}
dicOther={'大刘':[13914000001,18191230001],\
          '大王':[13914000002,18191230002],\
          '大张':[13914000003,18191230003]}
dicTXL.update(dicOther)
dicWX={'小新':'xx9907','小刚':'gang1004','大王':'jack_w','大刘':'liu666'}
for x in dicTXL.keys():
    if x in dicWX.keys():
        dicTXL[x].append(dicWX[x])
    else:
        dicTXL[x].append(dicTXL[x][0])
print(dicTXL)