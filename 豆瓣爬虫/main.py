import json
#import requests

# r=requests.get("http://www.baidu.com")
# r.encoding="UTF-8"
# with open("百度.html",'w',encoding="UTF-8") as bai:
#     bai.write(r.text)

# import requests
# w=requests.get("https://www.hufe.edu.cn/images/xxlogo.png")
# if w.status_code==200:
#     with open("hufe.png",'wb') as b:
#         b.write(w.content)
# else:
#     print("未爬取到数据")

import requests
url='https://movie.douban.com/j/chart/top_list'
params={'type': '20','interval_id': '100:90','action':'' ,'start': '0','limit': '299'}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'}
r=requests.get(url=url,params=params,headers=headers)
#print(r.json())
count=1
if r.status_code==200:
    with open("豆瓣恐怖电影排行榜.txt",'w',encoding="UTF-8") as file:
        for i in r.json():
            titl=i["title"]
            score=i["score"]
            file.write(str(count)+' 片名：《'+titl+'》'+' 分数：'+score+'  上映日期:'+i['release_date']+'  演员：'+','.join(i['actors'])+'\n')
            count+=1
            with open('恐怖/'+i["title"]+'.jpg','wb') as b:
                b.write(requests.get(i['cover_url']).content)
    print("爬取数据成功并成功写入文件！")
else:
    print("获取数据失败！")
