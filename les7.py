# kitaba 3ala sora wa rassem achekal
import cv2
import numpy as np
img = cv2.imread('images/fiat-500-ge3d5919a2_1920.jpg')

#line - rectangle  - text
#cv2.line(img,(10,10),(200,10),(0,255,0),2)
#cv2.rectangle(img,(300,20),(600,300),(255,0,0),4)
cv2.putText(img,'Imad aboulhouda',(300,400),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
cv2.imshow('title',img)
cv2.waitKey(0)