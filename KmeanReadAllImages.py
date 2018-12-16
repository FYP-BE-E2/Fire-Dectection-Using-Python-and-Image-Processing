import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
from PIL import Image

def main():
    X_data = []
    firstImg = "E:/FYP/Fire Dataset/FireImageSample/Image1/1.png"
    img1 = cv2.cvtColor(cv2.imread(firstImg, 1), cv2.COLOR_BGR2RGB)
    files = glob.glob("E:/FYP/Fire Dataset/FireImageSample/Image1/*.png")
    for myFile in files:
        img = cv2.imread(myFile, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img1 = np.hstack((img1, img))
    X_data = img1
    copied_slice = X_data.astype(np.float32)
    img1 = copied_slice
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K=12
    ret, label1, center1 = cv2.kmeans(img1, K, None,criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img1.shape))
    output = [X_data, output3]
    titles = ['Original Image','K=12']
    for i in range(2):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()