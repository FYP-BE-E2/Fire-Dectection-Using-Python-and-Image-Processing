import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import math
from PIL import Image, ImageChops
from numpy import genfromtxt
import win32api
#import natsort

vidcap = cv2.VideoCapture('E:/Hamayun/MAJU/FYP/Fire Dataset/FireVideo/Pelco_Colakli.avi')
success,image = vidcap.read()
count = 0
success = True
fps = vidcap.get(cv2.CAP_PROP_FPS)
fps = int(fps)
AvgDistanceAndCenterPoint = genfromtxt('E:/Hamayun/MAJU/FYP/CSV Data/AvgDistance.csv', delimiter=',')
# Saving Fram from Video
imgCounter = 1;
while success:
    success,image = vidcap.read()
    if count % (1 * fps) == 0 :
         cv2.imwrite('E:/Hamayun/MAJU/FYP/Fire Dataset/FireVideoImages/%d.jpg'%imgCounter,image)
         imgCounter += 1;
    count+=1

# Reading All Images from Source

imgSourcePath = 'E:/Hamayun/MAJU/FYP/Fire Dataset/FireVideoImages/'

# Storing All Images into Array

arr = os.listdir(imgSourcePath)

# Sorting Array

lsorted = sorted(arr,key=lambda x: int(os.path.splitext(x)[0]))

# subtracting Images

for x in range(len(lsorted)+1):
    print(x)
    orgImg1 = cv2.imread(imgSourcePath + lsorted[x], 1);
    orgImg2 = cv2.imread(imgSourcePath + lsorted[x+1], 1);

    img1 = cv2.cvtColor(cv2.imread(imgSourcePath + lsorted[x], 1), cv2.COLOR_RGB2GRAY)
    img2 = gray = cv2.cvtColor(cv2.imread(imgSourcePath + lsorted[x+1], 1), cv2.COLOR_RGB2GRAY)

    # Getting Diffrence

    DifImage = abs(img1.astype(np.float64) - img2.astype(np.float64))
    DifImage = DifImage.astype(np.uint8)
    #cv2.imshow('Difference Image', DifImage)

    # Applying Threshold

    ret, thresh1 = cv2.threshold(DifImage, 80, 255, cv2.THRESH_BINARY)
    copy = np.zeros((576,720 , 3), np.uint8)
    # copy = cv2.cv2.CreateImage((400, 256), 8, 3)
    copy[:,:,0]=thresh1
    copy[:,:,1]=thresh1
    copy[:,:,2]=thresh1
    #cv2.imshow('Th',thresh1)
    # gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    # thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_RGB2GRAY)
    mask = cv2.bitwise_and(orgImg2,copy)
    Z = mask.reshape((-1,3))
    #newaray = mask[~(mask==0).all(1)]
    withOutZero = Z[~np.all(Z == 0, axis=1)]
    CountOfFireMatch = []
    fireCounter = 0;
    for i in range(len(withOutZero)):
        for j in range(len(AvgDistanceAndCenterPoint)):
            dist = math.sqrt((AvgDistanceAndCenterPoint[j][2]-withOutZero[i][0])**2 + (AvgDistanceAndCenterPoint[j][3]-withOutZero[i][1])**2 + (AvgDistanceAndCenterPoint[j][4]-withOutZero[i][2])**2)
            if(dist < withOutZero[i][1]):
                fireCounter = fireCounter+1;
        if(fireCounter >= 6):
            win32api.MessageBox(0, 'Fire Fire Fire', 'Fire Alert !!') 
            fireCounter = 0;
            break
                
            
    # newimg = cv2.logical_and(img2, thresh1)

    #cv2.imshow('finalImge',mask)
    #cv2.waitKey(0)
