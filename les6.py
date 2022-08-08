# Save image after click in s
import cv2
img = cv2.imread('images/fiat-500-ge3d5919a2_1920.jpg',0)

cv2.imshow('image_grey',img)
k = cv2.waitKey(0)
if k == 27: # esc or q
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/fiat-grey.jpg',img)