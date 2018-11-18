import cv2
import numpy as np


path = "E:/FYP/Fire Dataset/Fire-Detection-Image-Dataset-master/Fire images/_91753989_capture.jpg"
img = cv2.imread(path)

r = cv2.selectROI(img)

#imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow('image',imCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()