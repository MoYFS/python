import qrcode
import cv2
import numpy as np
img=qrcode.make("nihao")
img.save("erweima.png")

inputimage=cv2.imread("erweima.png")

qrDecoder=cv2.QRCodeDetector()
data=qrDecoder.detect(inputimage)
src=qrDecoder.decode(inputimage,qrDecoder.detect(inputimage)[1])[0]
cv2.drawContours(inputimage, [np.int32(data[1])], 0, (0, 0, 255), 2)
cv2.imshow(src, inputimage)
cv2.waitKey(0)
