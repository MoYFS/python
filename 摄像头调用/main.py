import cv2
from aip import AipFace
import base64
import time
from PIL import ImageFont, ImageDraw, Image
import numpy
from datetime import datetime

#显示中文
def chineseText(image,text,px,py):
    font_size = 30
    py-=font_size
    font_color = (0, 0, 255)
    font_path = 'simhei.ttf' # 字体文件路径
    font = ImageFont.truetype(font_path, font_size)
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    draw.text((px,py), text, font=font, fill=font_color)
    cv2_img = cv2.cvtColor(numpy.array(pil_img), cv2.COLOR_RGB2BGR)
    return  cv2_img

#连接百度云
APP_ID='31750985'
API_KEY='60RRqY8GCNue1igjdOL80jyM'
SECRET_KEY='TSaTeQ08kiIUlLfEzObDQOp2bA6HamsD'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

#开启摄像头
cp=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

#识别标志
flag=0

start_time = time.time()#记录开始时间

while True:
    retval, image=cp.read()
    image = cv2.flip(image, 1, dst=None)
    cv2.putText(image,str(cp.get(cv2.CAP_PROP_FRAME_HEIGHT))+" "+str(cp.get(cv2.CAP_PROP_FRAME_WIDTH)),(0,24),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    face_image=image
    px,py=-100,-100
    for (x,y,h,w) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        px,py=x,y
        face_image=image[y:y+h,x:x+w]
    if flag==0:
        _, img_encode = cv2.imencode('.jpg', face_image)
        img_base64 = base64.b64encode(img_encode.tobytes())
        result = client.search(str(img_base64, 'utf-8'), 'BASE64', 'Student')
        if result['error_code']==0:
            group_id=result['result']['user_list'][0]['group_id']
            name=result['result']['user_list'][0]['user_id']
            #name='张家瑞'
            score=result['result']['user_list'][0]['score']
            flag=1
            print("{}在{}打卡成功!".format(name,datetime.now()))
            if score>90:
                with open('打卡日志.txt', 'a+') as f:
                    f.write(group_id + "组的" + name + "在" + str(datetime.now()) + " 打卡成功\r\n")
        elif result['error_code']==222202:
            print("图片中没有人脸")
            flag=1
        elif result['error_code']==222207:
            print("未找到匹配用户")
            flag=1
    elif flag==1:
        current_time = time.time()# 记录当前时间
        elapsed_time = current_time - start_time #计算经过的时间
        if flag == 1 and elapsed_time >= 10:
            flag=0
            start_time = time.time()# 记录开始时间
        image=chineseText(image,name,px,py)
        #cv2.putText(image, name, (px,py), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
    cv2.imshow("image", image)
    if (cv2.waitKey(1) & 0xFF)==ord('q'):
        break
cp.release()
cv2.destroyAllWindows()