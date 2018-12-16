import cv2
import matplotlib.pyplot as plt
import numpy as np

vidcap = cv2.VideoCapture('E:/FYP/Fire Dataset/FireVideo/Fire Ball in Slow Motion HD with Slow Mo Video Views of Flames Burning out from Core of Fireball.mp4')
success,image = vidcap.read()
count = 0
success = True
fps = vidcap.get(cv2.CAP_PROP_FPS)
fps = int(fps)

while success:
    success,image = vidcap.read()
    print('read a new frame:',success)
    if count % (2 * fps) == 0 :
         cv2.imwrite('1.jpg',image)
    if count % (2+1 * fps) == 0:
        cv2.imwrite('2.jpg',image)
    count+=1
    img1 = cv2.imread('1.jpg', 0)
    img2 = cv2.imread('2.jpg', 0)
    DifImage = abs(img1.astype(np.float64) - img2.astype(np.float64))
    DifImage = DifImage.astype(np.uint8)
    cv2.imshow('Difference Image', DifImage)
    cv2.waitKey(0)


    #DifImage = abs(img1.astype(np.float64) - img2.astype(np.float64))
    #DifImage = DifImage.astype(np.uint8)
    #frame = plt.figure()
    #plt.imshow(DifImage, cmap="gray")
    #plt.axis('off')
    #plt.title('Difference Image')



