'''
mydic={"汉堡":15,"鸡翅":10,"薯条":6}
print("第一题：输出“汉堡”对应的值：{}".format(mydic["汉堡"]))
mydic["鸡翅"]=8
print("第二题：修改“鸡翅”对应的值为8：{}".format(mydic))
mydic["奶茶"]=12
print("第三题：增加键“奶茶”,其值为12：{}".format(mydic))
if "鸡块" in mydic:
    print("第四题：判断“鸡块”是否在字典内：{}在{}中".format("鸡块",mydic))
else:
    print("第四题：判断“鸡块”是否在字典内：{}不在{}中".format("鸡块",mydic))
temp=mydic.pop("薯条")
print("第四题：删除并返回“薯条”对应的值:{}".format(temp))
print("第五题：用get的方法，分别获取“鸡翅”和“鸡块”对应的值，\n\
如果“鸡翅”或“鸡块”不在字典中，则返回“抱歉，无此商品！”:\n鸡翅{}\n鸡块{}".format(\
    mydic.get("鸡翅","抱歉，无此商品！"),mydic.get("鸡块","抱歉，无此商品！")))
mydic.clear()
print("第六题：清空字典{}".format(mydic))
'''


'''
mydic={"color":{"red":12,"green":23,"blue":15},"shape":{"circle":18,"square":20,\
    "triangle":12}, "pattern":{"dot":24,"line":26}}
print("第一题：输出“pattern”对应的值：{}".format(mydic["pattern"]))
print("第二题：输出“square”对应的值:{}".format(mydic["shape"]["square"]))
colorDic=dict(mydic["color"].items())
print("第三题：将“color”对应的值输出并存在字典colorDic中：\n{}".format(colorDic))
temp=sorted(colorDic)
print("第四题：用sorted对colorDic进行排序，输出结果:{}".format(temp))
del colorDic
'''

'''
mydic={"语文":[85,89,76,88],"数学":[88,92,96],"英语":[98,90,95]}
for x in mydic:
    temp=0
    print("{}的平均分为:".format(x))
    for i in mydic[x]:
        temp=temp+i
    print(round(temp/len(mydic[x]),1))
'''


'''
dict = {"k1":"v1","k2":"v2","k3":"v3"}
print("第一题：请循环遍历出所有的key:")
for x in dict.keys():
    print(x,end=' ')
print()
print("第二题：请循环遍历出所有的value:")
for x in dict.values():
    print(x,end=' ')
print()
print("第三题：请循环遍历出所有的key和value")
for key in dict.keys():
    print(key,dict[key])
print("第四题：请在字典中增加一个键值对,k4:v4，输出添加该键值对后的字典：")
dict["k4"]="v4"
print(dict)
print("第五题：请删除字典中键值对'k1':'v1',并输出删除后的字典：")
del dict["k1"]
print(dict)
'''


'''
myDict={"辣条":9.9,"快乐肥皂水":99,"盲盒":199,"拖把":299}
print("第一题：使用字典myDict存放上表的信息，产品名称为键，价格为值:\n{}".format(myDict))
print("第二题：输出所有在售产品的价目表。格式为 辣条.........9.9元:")
for key in myDict:
    print("{}.........{}元".format(key,myDict[key]))
print("第三题：输出价格超过100的所有商品：")
for key in myDict:
    if myDict[key]>=100:
        print(key)
'''


'''
scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96,\
          "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78, "Wu Shi": 99,\
          "Dong Shiyi": 60}
print("(1)最高分：{}".format(max(scores.values())))
print("(2)最低分：{}".format(min(scores.values())))
print("(3)平均分：{}".format(round(sum(scores.values())/len(scores)),1))
for x in scores:
    if scores[x]==max(scores.values()):
        print("(4)最高分同学:{}".format(x))
        break
'''


'''
import functools
scores = {"Zhang San": [45,60,80], "Li Si": [78,80,90], "Wang Wu": [40,59,60]}
print(scores)
print("第一题：")
temp={"数学":0,"python":0,"英语":0}
for x in scores.values():
    temp["数学"]=temp["数学"]+x[0]
    temp["python"]=temp["python"]+x[1]
    temp["英语"]=temp["英语"]+x[2]
temp["数学"]=round(temp["数学"]/len(scores),1)
temp["python"]=round(temp["python"]/len(scores),1)
temp["英语"]=round(temp["英语"]/len(scores),1)
print(temp)
print("第二题：")
m=-1
for x in temp:
    str=x+' '
    flag=0
    m+=1
    for i in scores:
        if scores[i][m]<60:
            str=str+i+'、'
            flag=1
    str+="不及格"
    if flag==1:
        print(str)
del str
del temp
print("第三题：")
temp=list(scores.items())
def require(x,u):
    if x[1][0]>=u[1][0]:
        return -1
    else:
        return 1
temp.sort(key=functools.cmp_to_key(require))
for x in temp:
    print(x)
del temp
'''

scores = {"Zhang San": [45,60,80], "Li Si": [78,80,90], "Wang Wu": [40,59,60]}
temp={"数学":0,"python":0,"英语":0}
for i,m in zip(range(len(temp)),temp):
    for x in scores.values():
        temp[m]+=x[i]
for m in temp:
    temp[m]=round(temp[m]/len(scores),1)
print("第一题：平均分{}\n第二题：".format(temp))
for x,m,i in zip(temp,range(len(temp)),scores):
    str=x+' '
    for i in scores:
        if scores[i][m]<60:
            str=str+i+'、'
    if len(str)>len(x)+1:
        print(str[:len(str)-1:]+"不及格")
del str,temp
temp=sorted(scores.items(),key=lambda x:x[1][0],reverse=False)
print("第三题：")
for x in temp:
    print("姓名：{:9} 数学：{} python：{} 英语：{}".format(x[0],x[1][0],x[1][1],x[1][2]))
