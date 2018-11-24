import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image

def main():
    X_data = []
    files = glob.glob ("E:/FYP/Fire Dataset/FireImageSample/Image1/*.png")
    for myFile in files:
	    print(myFile)
	    img = cv2.imread(myFile,1)
	    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	    #cv2.imshow('img',img)
	    #cv2.waitKey(0)
	    #cv2.destroyAllWindows()
	    #im = Image.open(myFile,'r')
	    Z = img.reshape((-1,3))
	    Z = np.float32(Z)
	    #X_data.append (Z)
	    #print(X_data)
	    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	    K=2
	    ret, label1, center1 = cv2.kmeans(Z, K, None,
		                                  criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	    center1 = np.uint8(center1)
	    res1 = center1[label1.flatten()]
	    output1 = res1.reshape((img.shape))
	    K=4
	    ret, label1, center1 = cv2.kmeans(Z, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	    center1 = np.uint8(center1)
	    res1 = center1[label1.flatten()]
	    output2 = res1.reshape((img.shape))
	    K=12
	    ret, label1, center1 = cv2.kmeans(Z, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
	    center1 = np.uint8(center1)
	    res1 = center1[label1.flatten()]
	    output3 = res1.reshape((img.shape))
	    output = [img, output1, output2, output3]
	    titles = ['Original Image', 'K=2', 'K=4', 'K=12']
	    for i in range(4):
	        plt.subplot(2, 2, i+1)
	        plt.imshow(output[i])
	        plt.title(titles[i])
	        plt.xticks([])
	        plt.yticks([])
	    
	    plt.show()

if __name__ == "__main__":
    main()