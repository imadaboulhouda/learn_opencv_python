# import the necessary packages
import numpy as np
import cv2




# open webcam video stream
cap = cv2.VideoCapture(0)



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

   
    # Display the resulting frame
    
    classnames = [] # ليست او array
    classfile  = 'files/thing.names'

    with open(classfile, 'rt') as f :
        classnames = f.read().rstrip('\n').split('\n')
    #print(classnames)
    p = 'files/frozen_inference_graph.pb'
    v = 'files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

    net = cv2.dnn_DetectionModel(p,v) # الكشف والفحص
    net.setInputSize(320,230)         # العرض والارتفاع
    net.setInputScale(1.0/127.5)      # القياس
    net.setInputMean((127.5,127.5,127.5))
    net.setInputSwapRB(True)          # نظام الالوان

    classIds ,confs , bbox = net.detect(frame, confThreshold=0.5)
   
    if len(confs) > 0:
        for classId , confidence , box in zip(classIds.flatten(),confs.flatten(),bbox):
                cv2.rectangle(frame,box,color=(0,255,0),thickness=3)
                cv2.putText(frame,classnames[classId-1],
                            (box[0]+10,box[1]+20),
                            cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),thickness=2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# and release the output

# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
