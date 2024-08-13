import cv2
print(cv2.__version__)
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def myCallbackX(val):
    global xPos
    xPos = val
def myCallbackY(val):
    global yPos
    yPos = val

xPos = int(width/2)
yPos = int(height/2)

cv2.namedWindow('myTrackbar')
cv2.resizeWindow('myTrackbar', 400, 100)
cv2.moveWindow('myTrackbar', width, 0)
cv2.createTrackbar('xPos', 'myTrackbar', xPos, 1920, myCallbackX)
cv2.createTrackbar('yPos', 'myTrackbar', yPos, 1080, myCallbackY)
while True:
    ignore,  frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.circle(frame, (xPos, yPos), 25, (255, 0, 0), 2)
    cv2.imshow('my WEBcam', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()