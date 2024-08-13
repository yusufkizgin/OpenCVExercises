import numpy as np
import cv2
print(cv2.__version__)

xVal = 0
yVal = 0
evt = 0

def mouseClick(event, x, y, flags, param):
    global xVal
    global yVal
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse event was : ',event)
        xVal = x
        yVal = y
        evt = event

width = 1280
height = 720
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    if evt == 1:
        x = np.zeros([250, 250, 3], dtype=np.uint8)
        color = frame[yVal][xVal]
        print(color)
        x[:, :] = color
        cv2.putText(x, str(color), (5, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255))
        cv2.imshow('Color Picker', x)
        cv2.moveWindow('Color Picker', width + 8, 0)
        evt = 0
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()