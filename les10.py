#Open camera
import cv2
#0 camera hasoub 1 camera kharijiya
camera = cv2.VideoCapture(0)
while True:
    ret , frame = camera.read()
    newCam = cv2.resize(frame,(400,200))
    cv2.imshow('imad',newCam)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

