import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from PIL import Image, ImageChops
#import natsort

vidcap = cv2.VideoCapture('E:/FYP/Fire Dataset/FireVideo/ForestFire1.avi')
success,image = vidcap.read()
count = 0
success = True
fps = vidcap.get(cv2.CAP_PROP_FPS)
fps = int(fps)
# Saving Fram from Video
imgCounter = 1;
while success:
    success,image = vidcap.read()
    if count % (1 * fps) == 0 :
         cv2.imwrite('E:/FYP/Fire Dataset/FireVideoImages/%d.jpg'%imgCounter,image)
         imgCounter += 1;
    count+=1

# Reading All Images from Source

imgSourcePath = 'E:/FYP/Fire Dataset/FireVideoImages/'

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
    cv2.imshow('Difference Image', DifImage)

    # Applying Threshold

    ret, thresh1 = cv2.threshold(DifImage, 80, 255, cv2.THRESH_BINARY)
    copy = np.zeros((256, 400, 3), np.uint8)
    # copy = cv2.cv2.CreateImage((400, 256), 8, 3)
    copy[:,:,0]=thresh1
    copy[:,:,1]=thresh1
    copy[:,:,2]=thresh1
    cv2.imshow('Th',thresh1)
    # gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    # thresh1 = cv2.cvtColor(thresh1, cv2.COLOR_RGB2GRAY)
    mask = cv2.bitwise_and(orgImg2,copy)
    # newimg = cv2.logical_and(img2, thresh1)

    cv2.imshow('finalImge',mask)
    cv2.waitKey(0)
