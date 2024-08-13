import cv2
print(cv2.__version__)
width=960
height=540
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def mouseClick(event, x, y, flags, param):
    global fpnt
    global lpnt
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        fpnt = (x, y)
        evt = event
        print('mouse event was : ',event)
    if event == cv2.EVENT_LBUTTONUP:
        print('mouse event was : ',event)
        lpnt = (x, y)
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN:
        print('mouse event was : ',event)
        fpnt = (x, y)
        lpnt = (x, y)
        evt = event
fpnt = (0, 0)
lpnt = (0, 0)
evt = 0
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore,  frame = cam.read()
    frame = cv2.flip(frame, 1)
    if evt == 4:
        frameROI = frame[fpnt[1]:lpnt[1], fpnt[0]:lpnt[0]]
        frameROI = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
        cv2.imshow('my ROI', frameROI)
        cv2.moveWindow('my ROI', width + 10, 0)
    if evt == 2:
        cv2.destroyWindow('my ROI')
        evt = 0
    cv2.imshow('my WEBcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()