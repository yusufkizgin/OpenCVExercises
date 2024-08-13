import cv2
print(cv2.__version__)
import numpy as np

while True:
    frame = np.zeros([400, 400], dtype = np.uint8)
    for i in range(8):
        for j in range(8):
            # Satır ve sütunun toplamı çift ise kareyi beyaz (255), tek ise siyah (0) yap
            if (i + j) % 2 == 0:
                frame[i * 50:(i + 1) * 50, j * 50:(j + 1) * 50] = 255
    cv2.imshow('My frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break