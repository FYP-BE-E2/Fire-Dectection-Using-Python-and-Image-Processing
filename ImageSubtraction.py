#importing Open Cv2 library
import cv2
#importing Numpy Library
import numpy as np
# storing video from primary camera in to variable
vidcap = cv2.VideoCapture(0)
#https://docs.opencv.org/3.0-beta/doc/tutorials/video/background_subtraction/background_subtraction.html
#this method take first image and store into fgm varible this image will be our base image.
fgm = cv2.createBackgroundSubtractorMOG2()

#unlimited loop
while True:
	#rate is result bool variable which true or false after executing the function because this method return true or false
	#frame is variable which store image 
	rate,frame = vidcap.read()	
	#this method take array of image as first parameter this method has diffrent overload 
	#in below code this is subtracting current image from first taken image
	fgMask = fgm.apply(frame);
	
	#this is to display image 
	cv2.imshow("test",frame)
	#this is to show subtracted image
	cv2.imshow('image',fgMask)
	
	if cv2.waitKey(10) == 27: # exit if Escape is hit
		break
		
