#afficher les dimensions des images et pixel (imginfo)
import cv2
img = cv2.imread('images/fiat-500-ge3d5919a2_1920.jpg')
pixel = img.size

dimenssion = img.shape
print("Nbr pixel is :",pixel)

print("Nbr dimmesion is :",dimenssion)
cv2.imshow('image',img)
cv2.waitKey(0)
#print("Nbr of dim",dimenssion)