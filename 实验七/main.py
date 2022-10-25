'''
#第一题
print("第一题：")
ls=[54,36,75,28,50]
print("初始列表:{}".format(ls))
ls.append(42)
print("①在列表尾部插入元素42：{}".format(ls))
ls.insert(-3,66)
print("②在28前面插入元素66：{}".format(ls))
temp=ls.pop(-3)
print("③删除并输出元素28：列表{}，元素{}".format(ls,temp))
ls.sort(reverse=True)
print("④ 将列表按降序排序：{}".format(ls))
del ls[:]
print("⑤ 清空整个列表：{}".format(ls))
'''

'''
#第二题
score =[68,87,92,100,76,88,54,89,76,61]
print("(2)输出 score 列表中第5 个元素的数值：{}".format(score[4]))
print("(3)输出 score 列表中第 1~6 个元素的值：{}".format(score[0:5]))
score.insert(2,59)
print("(4)调用 insert()函数，在 score 列表第 3 个元素之前添加数 59：\n{}".format(score))
num=76
print("(5)利用变量 num 保存数值 76,调用 count()函数，查询 num 变量值在 score 列表中出现的次数：{}".format(score.count(num)))
score.sort()
print("(6)调用 sort()函数，对列表中所有元素进行排序，输出考试的最高分和最低分：\n排序后：{}\n最高分：{}\n最低分：{}".format(score,score[-1],score[0]))
print("(7)查找元素100在列表的位置：{}".format(score.index(100)+1))
print("(8)求列表所有元素的平均值：{}".format(sum(score)/len(score)))

'''

'''
#第三题
num=[]
for x in range(3,101):
    if x%3==0:
        num.append(x)
print("第三题：\n100以内所有能被3整除的数：\n{}".format(num))
'''

'''
#第四题
import random as rd
english=[]
for x in range(5):
    english.append(rd.randrange(40,101))
print("生成的列表：{}".format(english))
english.sort(reverse=True)
print("降序排列：{}".format(english))
'''
#第五题
import random
lst_who=['我','你','他']
lst_where=['在宿舍','在教室','在操场']
lst_what=['学习','打游戏','睡觉']
for x in range(10):
    print(lst_who[random.randint(0,2)]+lst_where[random.randint(0,2)]+lst_what[random.randint(0,2)])