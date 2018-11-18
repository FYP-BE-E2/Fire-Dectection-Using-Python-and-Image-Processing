import cv2
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
count1 = 0
success = True

while success:
	success,image = vidcap.read()	
	cv2.imwrite("C:/Users/Faraz-Pc/Anaconda3/envs/[FYP]/Images/frame%d.jpg" % count, image)
	img_cam0 = cv2.imread("C:/Users/Faraz-Pc/Anaconda3/envs/[FYP]/Images/frame%d.jpg"% count,0)
	cv2.imwrite("C:/Users/Faraz-Pc/Anaconda3/envs/[FYP]/Images/frame1%d.jpg" % count1, image)  # save frame as JPEG file
	img_cam1 = cv2.imread("C:/Users/Faraz-Pc/Anaconda3/envs/[FYP]/Images/frame1%d.jpg"% count1,0)
	
	#image subtraction
	cv2_subt = cv2.subtract(img_cam0,img_cam1)
	cv2.imshow("test",image)
	cv2.imshow('image',cv2_subt)
	#end image subtraction
	
	count += 1
	count1 += 1
	if cv2.waitKey(10) == 27: # exit if Escape is hit
		break