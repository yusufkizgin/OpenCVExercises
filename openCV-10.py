import cv2
print(cv2.__version__)
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global pnt
    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse event was : ',event)
        print('at position ', xPos, yPos)
        evt = event
        pnt = (xPos, yPos)
    if event == cv2.EVENT_LBUTTONUP:
        print('mouse event was : ',event)
        print('at position ', xPos, yPos)
        evt = event
        pnt = (xPos, yPos)
    if event == cv2.EVENT_RBUTTONDOWN:
        print('mouse event was : ',event)
        evt = event
        pnt = (xPos, yPos)
width=980
height=480
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
evt = 0
while True:
    ignore,  frame = cam.read()
    frame = cv2.flip(frame,1)
    if evt == 1 or evt == 4:
        cv2.circle(frame, pnt, 25, (255, 0, 0), 2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()