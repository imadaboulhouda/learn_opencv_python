#show video  and change to grey
import cv2
from cv2 import COLOR_RGB2GRAY
cam = cv2.VideoCapture('videos/1.mp4')
while True:
    ret , frame = cam.read()
    gray = cv2.cvtColor(frame,COLOR_RGB2GRAY)
    size = cv2.resize(gray,(300,400))
    cv2.imshow('imad',size)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
#cv2.waitKey(0)