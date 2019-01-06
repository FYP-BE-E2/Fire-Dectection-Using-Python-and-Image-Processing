import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
from collections import namedtuple
import math

def getKey(item):
    return item[0]

if __name__ == "__main__":
    firstImg = "E:/Hamayun/MAJU/FYP/Fire Dataset/FireImageSample/Image1/1.png"
    img1 = cv2.cvtColor(cv2.imread(firstImg, 1), cv2.COLOR_BGR2RGB)
    files = glob.glob("E:/Hamayun/MAJU/FYP/Fire Dataset/FireImageSample/Image1/*.png")
    
    for myFile in files:
        img = cv2.imread(myFile, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img1 = np.hstack((img1, img))
    
    Z = img1.reshape((-1,3))
    Z = np.float32(Z)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K=12
    ret, label1, center1 = cv2.kmeans(Z, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    print(label1)
    label1 
    
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img1.shape))
    output = [img1, output3]
    titles = ['Original Image','K=12']
    for i in range(2):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    print('Making Array in progress ....')
    data = []
    counter=0;
    for x in range(51198):
        data = np.append(data,(label1[counter][0]))
        data = np.append(data,(Z[x][0]))
        data = np.append(data,(Z[x][1]))
        data = np.append(data,(Z[x][2]))
        counter += 1;
    data = data.reshape((-1,4))
    print('Making Array Done')
    
  
      #print('Removing Duplication')
    #uniques = []
    #for arr in data:
        #if not any(np.array_equal(arr, unique_arr) for unique_arr in uniques):
            #uniques.append(arr)
    #array = np.asarray(uniques)
    #print('Removing Duplication Done')
    
    
    print('Sorting Array')
    sorted_by_first = sorted(data, key=lambda tup: tup[0])
    sorted_by_first = np.asarray(sorted_by_first)
    print('Sorting Array Done')
    
    
    print("Making Array With Class Label, Center Point Value,Image Class Value, Distance")
    CenterCounter = 0
    DistanceAll = []
    Lang = namedtuple("Lang", ("LabelClass", "Center_Point_Value_0","Center_Point_Value_1","Center_Point_Value_2","Image_Value_0","Image_Value_1","Image_Value_2","Distance"))
    for i in range(12):
        for x in range(len(sorted_by_first)):
            if CenterCounter == int(sorted_by_first[x][0]):
                dist = math.sqrt((center1[i][0]-sorted_by_first[x][0])**2 + (center1[i][1]-sorted_by_first[x][1])**2 + (center1[i][2]-sorted_by_first[x][2])**2)
                DistanceAll.append(Lang(sorted_by_first[x][0],center1[i][0],center1[i][1],center1[i][2],sorted_by_first[x][1],sorted_by_first[x][2],sorted_by_first[x][3],dist))
        CenterCounter = CenterCounter + 1
    DistanceAll = np.asarray(DistanceAll)
    print("Making Array Done")
    
    print("Calculating Avg Distance")
    distanceIndexCounter = 0
    AvgDistance = 0
    DistanceLabel = 0
    AvgDistanceAsPerLabel = []
    TotalElement = 0
    for i in range(len(DistanceAll)):
        if  distanceIndexCounter == DistanceAll[i][0]:
            TotalElement =+ 1;
            AvgDistance = AvgDistance + DistanceAll[i][7]
        else:
            AvgDistance = AvgDistance/TotalElement;
            distanceIndexCounter = distanceIndexCounter + 1;
            AvgDistanceAsPerLabel.append((distanceIndexCounter,AvgDistance))
            AvgDistance = 0
            TotalElement = 0
    AvgDistanceAsPerLabel = np.asarray(AvgDistanceAsPerLabel)
    np.savetxt("AvgDistance.csv", AvgDistanceAsPerLabel, delimiter=",")
    np.savetxt("CenterPoint.csv", center1, delimiter=",")
    np.savetxt("DistanceAll.csv", DistanceAll, delimiter=",")
    print("Distance Calculate Done")
    
    
    
        
    