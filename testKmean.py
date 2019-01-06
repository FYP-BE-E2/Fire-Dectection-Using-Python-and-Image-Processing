import cv2
import numpy as np
import glob

firstImg = "E:/Hamayun/MAJU/FYP/Fire Dataset/FireImageSample/Image1/1.png"
img1 = cv2.imread(firstImg, 1) #cv2.cvtColor(, cv2.COLOR_BGR2RGB)
files = glob.glob("E:/Hamayun/MAJU/FYP/Fire Dataset/FireImageSample/Image1/*.png")
for myFile in files:
    img = cv2.imread(myFile, 1)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img1 = np.hstack((img1, img))
Z = img1.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 12
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img1.shape))
cv2.cvtColor(res2, cv2.COLOR_RGB2BGR)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()