#第一题
# dic_student={}
# for i in range(5):
#     InputData=input("依次输入班级，姓名，年龄，身高和体重")
#     InputData=InputData.split(' ')
#     dic_student[InputData[0]+' '+InputData[1]]=InputData[2]+' '+InputData[3]+' '+InputData[4]
# for x in dic_student.keys():
#     print("{:7}{}".format(x,dic_student[x]))

#第二题
lst_staff=["李梅","张富","付妍","赵诺","刘江"]
dic_award={"张富":10000,"赵诺":150000}
for x in lst_staff:
    if x in dic_award:
        print("{:3}年终奖金为{}元".format(x,dic_award[x]))
    else:
        print("{:3}年终奖金为5000元".format(x))