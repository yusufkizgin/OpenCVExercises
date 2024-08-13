import cv2
import cv2.cv2
print(cv2.__version__)
width=640
height=360
snipw = 120
sniph = 60

boxCC = int(width/2)
boxCR = int(height/2)

deltaRow = 2
deltaColumn = 2

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameROI = frame[boxCR-int(sniph/2) : boxCR+int(sniph/2), boxCC-int(snipw/2) : boxCC+int(snipw/2)]
    frameROI = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    frameROI = cv2.cvtColor(frameROI, cv2.COLOR_GRAY2BGR)
    frameROI = (0, 0, 0)
    frame[boxCR-int(sniph/2) : boxCR+int(sniph/2), boxCC-int(snipw/2) : boxCC+int(snipw/2)] = frameROI
    
    if boxCR - sniph/2 <= 0 or boxCR + sniph/2 >= height:
        deltaRow = deltaRow * (-1)
    if boxCC - snipw/2 <= 0 or boxCC + snipw/2 >= width:
        deltaColumn = deltaColumn * (-1)

    boxCR = boxCR + deltaRow
    boxCC = boxCC + deltaColumn
    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()