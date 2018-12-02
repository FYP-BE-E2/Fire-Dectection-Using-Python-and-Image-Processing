import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image

def main():
    X_data = []
    firstImg = "E:/FYP/Fire Dataset/FireImageSample/Image1/1.png"
    img1 = cv2.imread(firstImg, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    cv2.imshow('img',img1)
    cv2.waitKey(0)
    files = glob.glob("E:/FYP/Fire Dataset/FireImageSample/Image1/*.png")
    for myFile in files:
        print(myFile)
        img = cv2.imread(myFile, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        X_data = np.hstack((img1, img))
        #test = cv2.imread(X_data, 1)
        cv2.imshow('img', X_data)
        cv2.waitKey(0)
    #X_data = X_data.reshape((-1, 3))
    copied_slice = X_data.astype(np.float32)
    print(copied_slice)
    #img1 = np.float(copied_slice)
    img1 = copied_slice
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K=2
    ret, label1, center1 = cv2.kmeans(img1, K, None,
		                                  criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img1.shape))
    K=4
    ret, label1, center1 = cv2.kmeans(img1, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output2 = res1.reshape((img1.shape))
    K=12
    ret, label1, center1 = cv2.kmeans(img1, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img1.shape))
    output = [X_data, output1, output2, output3]
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