import random

def verifcode(n):
    seq = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    txt = ""
    for i in range(n):
        txt += random.choice(seq)
    return txt

if __name__=='__main__':
    print(verifcode(6))

# file=open("mydata.txt",'w')
# file.write("飞雪连天射白鹿\n")
# file.write("笑书神侠倚碧鸳\n\n")
# file.close()
# file=open("mydata.txt",'a')
# file.write("\t\t 充军行\n青海长云暗雪山，古城遥望玉门关。\n黄沙百战穿金甲，不破楼兰终不还。")
# file.close()
# file=open("mydata.txt",'r')
# print(file.read())
# file.close()