import pandas as pd
import numpy as np

# s1 = pd.Series([1, -2, 2.3, 'hq'], index=['a', 'b', 'c', 'd'])
# print(s1['a':'b'])
# s2=s1.value_counts()
# print(s2)

# ss1=pd.Series([10,'hq',60,np.nan,20]) #np.nan为空值（nan值）
# tt1=ss1[~ss1.isnull()]
# tt2=ss1[ss1.notnull()]
# ss11=ss1
# tt3=ss11.dropna()
# print(ss1,'\n',tt1,'\n',tt2,'\n',tt3)

# data={'a':[2,2,np.nan,5,6],'b':['kl','kl','kl',np.nan,'kl'],'c':[4,5,6,np.nan,6],'d':[7,9,np.nan,9,8]}
# df=pd.DataFrame(data)
# df1=df.dropna()
# df2=df.fillna(0)
# df3=df.fillna({'a':10,'b':'kl','c':80,'d':6})
# print(df)

# with open('test1.txt','r',encoding='utf-8') as file:
#     data=file.readlines()
# data=[dat.split(',') for dat in data]
# print(data)

# pd=pd.read_table('test1.txt',sep=',',header=None)
# print(pd)
# pd1=pd.loc[pd[0]=='小红',:]
# print(pd1)
# pd2=pd.loc[pd[0]=="张明",:]
# print(pd2)
# pd3=pd.loc[pd[0]=="小江",:]
# print(pd3)
# pd4=pd.loc[pd[0]=="小李",:]
# print(pd4)


