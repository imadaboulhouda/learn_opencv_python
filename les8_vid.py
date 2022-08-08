#show video 
import cv2
cam = cv2.VideoCapture('videos/1.mp4')
while True:
    ret , frame = cam.read()
    cv2.imshow('imad',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
#cv2.waitKey(0)