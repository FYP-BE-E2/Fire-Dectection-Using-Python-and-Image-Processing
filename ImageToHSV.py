import cv2
import numpy as np

get = cv2.VideoCapture(0)
_,backImage = get.read()

hsvBack = cv2.cvtColor(backImage,cv2.COLOR_RGB2GRAY)

print ("BackGround Image Done")

while True: 
	_,frame = get.read()
	currentHSV = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
	#img = cv2.subtract(currentHSV, hsvBack)
	img =  hsvBack - currentHSV
	cv2.imshow("Image show",img)
	
	if cv2.waitKey(10) == 27: # exit if Escape is hit
		break 
	
	



