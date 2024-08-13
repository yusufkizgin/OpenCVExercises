import cv2
import numpy as np

while True:
    frame = np.zeros([250, 250, 3], dtype=np.uint8)
    frame[100:150, 100:150] = (250,0,0)
    cv2.imshow('My window', frame)
    if cv2.waitKey(1) == ord('q'):
        break