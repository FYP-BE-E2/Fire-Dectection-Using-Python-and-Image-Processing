import cv2
import numpy as np


def yscript():
	restart = input("Would you like to restart this program?")
	if restart == "yes" or restart == "y":
		path = "E:/FYP/Fire Dataset/Fire-Detection-Image-Dataset-master/Fire images/_91753989_capture.jpg"
		img = cv2.imread(path)
		fromCenter = false
		r = cv2.selectROI("Image Crop",img,fromCenter)
		imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
		cv2.imshow('image',imCrop)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		yscript()
	if restart == "n":
		print("done")
    # if restart == "n" or restart == "no":
		# break
yscript()