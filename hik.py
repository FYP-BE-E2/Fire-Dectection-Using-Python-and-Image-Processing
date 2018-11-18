


import numpy as np
import cv2

cap = cv2.VideoCapture('rtsp://admin:Raoabrehman12!%40@192.168.1.64/Streaming/Channels/101')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, ret)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()