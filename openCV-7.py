import cv2
print(cv2.__version__)
width = 1280
height = 720
myRadius = 82
myColor = (0,0,255)
myText = 'Hello Guys'
myFont = cv2.FONT_HERSHEY_COMPLEX
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameROI = frame[330:390, 440:840]
    frameROIgray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROIbgr = cv2.cvtColor(frameROIgray, cv2.COLOR_GRAY2BGR)
    frame[330:390, 440:840] = frameROIbgr
    cv2.imshow('my WEBcam1', frame)
    #cv2.imshow('gray', frameROIgray)
    #cv2.moveWindow('gray', 660,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()