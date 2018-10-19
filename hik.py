import numpy as np
import cv2

cap = cv2.VideoCapture()
cap.open('rtsp://admin:Raoabrehman12!%40@192.168.1.63/1',cv2.CAP_FFMPEG)

while(True):
     # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    

    # Display the resulting frame
    cv2.imshow('frame',ret)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()