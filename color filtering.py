import cv2
import numpy as np
img=cv2.imread("Red.jpg")
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
low_red=np.array([155,225,35])
upp_red=np.array([200,255,255])
mask=cv2.inRange(hsv,low_red,upp_red)
res=cv2.bitwise_and(img,img,mask=mask)
kernel=np.ones((5,5),np.float32)/25
smoothed=cv2.GaussianBlur(res,(15,15),0)
cv2.imwrite('original.jpg',img)
cv2.imwrite('red_color.jpg',res)
cv2.imshow("drone",img)
cv2.imshow("drone1",hsv)
cv2.imshow("filter",res)
cv2.imshow("mask",mask)
cv2.imshow("drone1",smoothed)
cv2.waitKey(0)
cv2.detroyAllWindows()
