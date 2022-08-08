#change image width and height and window
import cv2
img = cv2.imread('images/fiat-500-ge3d5919a2_1920.jpg')
newImage = cv2.resize(img,(200,200))
cv2.imshow('fiat',newImage)
cv2.waitKey(0)