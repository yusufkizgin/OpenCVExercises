import cv2
import time
width = 640
height = 360
myFont = cv2.FONT_HERSHEY_COMPLEX
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

start = 1
finish = 1
text = ''
fps = 0
while True:
    start = time.time()
    _,frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame, (0,0), (120,50), (150,0,150), -1)
    cv2.putText(frame, text, (20,30), myFont, 0.7, (0,255,0), 1)
    cv2.imshow('hi', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    finish = time.time()
    fps = int(1/(finish-start))
    text = str(fps) + ' fps'
cam.release()