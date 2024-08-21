#2 farklı pencere açılacak
#soldan sağa doğru renk değişecek ( hue 0-180 )
#birinde yukarıdan aşağı doğru doygunluk değişecek ( saturation 0-255 )
#diğerinde yukarıdan aşağı doğru parlaklık değişecek ( value 0-255 )
#images içerisindeki opencv15.png dosyasının aynısı olucak

import cv2
import numpy as np
x = np.zeros([256, 180, 3], dtype=np.uint8)
y = np.zeros([256, 180, 3], dtype=np.uint8)

for row in range(0, 256, 1):
    for col in range(0, 180, 1):
        x[row, col] = (col, row, 255)

for row in range(0, 256, 1):
    for col in range(0, 180, 1):
        y[row, col] = (col, 255, row)

x = cv2.cvtColor(x, cv2.COLOR_HSV2BGR)
y = cv2.cvtColor(y, cv2.COLOR_HSV2BGR)

while True:
    cv2.imshow('My frame1', x)
    cv2.imshow('My frame2', y)
    cv2.moveWindow('My frame1', 0, 0)
    cv2.moveWindow('My frame2', 190, 0)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()