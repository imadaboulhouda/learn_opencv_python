# Color change to grey
import cv2
img = cv2.imread('images/fiat-500-ge3d5919a2_1920.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image_grey',grey)
cv2.waitKey(0)