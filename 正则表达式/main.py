import re
import requests
# str1='123Qwe!_@#$^ 你我他\n\t'
# print(re.findall('\w',str1))
# print(re.findall('\W',str1))
# print(re.findall('\s',str1))
# print(re.findall('\S',str1))
# print(re.findall('\d',str1))
# print(re.findall("\D",str1))
# str2='你好吗，我很好'
# print(re.findall("^你好",str2))
# str3='我很好，你好'
# print(re.findall('^你好',str3))
# print(re.findall("你好$",str3))

# r=requests.get("http://www.baidu.com")
# r.encoding="UTF-8"
# # with open("百度.html",'w',encoding="UTF-8") as bai:
# #     bai.write(r.text)
# #print(re.findall('(<img hidefocus=true src=//)(.*)( width)',r.text))
# print("http://"+re.findall('(<img hidefocus=true src=//)(.*)( width)',r.text)[0][1])
# with open("baidu.png",'wb') as bai:
#     bai.write(requests.get("http://"+re.findall('(<img hidefocus=true src=//)(.*)( width)',r.text)[0][1]).content)

#str5="电话号码021-62232333"
#s='([0-9]{3}-[0-9]{8})'
# s="350124198310131229"
# n="^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$"
# m='^1(3[0-9]|5[0-3,5-9]|7[1-3,5-8]|8[0-9])\d{8}$'
#print(re.findall(s,str5))

# regex_obj=re.compile(r'\d+')
# regex_obj1=re.compile(r'[a-z]+',re.I)
# words="Today is March 28,2019."
# print(regex_obj.findall(words))
# print(regex_obj1.findall(words))
# m=re.search("be","To be,\nor not to be")
# print(m.group())
# print(m.span())
# r=re.match(r"(?P<Area>\d+)-(?P<No>\d+)","电话号码：021-62232333")
# print(r.groups())
# print(r.groupdict())

url='https://www.cnblogs.com/'
header={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"}
#temp=requests.get(url=url,headers=header)
#regex=re.compile(r'<a class="post-item-title" href=(.*) target="_blank">.*</a>')
regex=re.compile(r'<img src=.*? class="avatar" alt="博主头像" />.*?</a>\n(.*?)\n.*?</p>',re.S)
temp=regex.findall(requests.get(url=url,headers=header).text)
for i in temp:
    print(i.lstrip())
    print()
