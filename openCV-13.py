import cv2
print(cv2.__version__)

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

def adjustSize1(x):
    global width
    width = int(x)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720*width/1280)

def adjustSize2(y):
    global height
    height = int(y)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280*height/720)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def adjustLocation1(_xPos):
    global xPos
    xPos = int(_xPos)

def adjustLocation2(_yPos):
    global yPos
    yPos = int(_yPos)

xPos = 0
yPos = 0
width=640
height=360
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cv2.namedWindow('location')
cv2.namedWindow('size')
cv2.namedWindow('my WEBcam')
cv2.resizeWindow('size', 400, 90)
cv2.resizeWindow('location', 400, 90)
cv2.createTrackbar('x', 'size', width, 1280, adjustSize1)
cv2.createTrackbar('y', 'size', height, 720, adjustSize2)
cv2.moveWindow('size', width, 0)
cv2.moveWindow('location', width, 100)

cv2.createTrackbar('x position', 'location', 0, 1280, adjustLocation1)
cv2.createTrackbar('y position', 'location', 0, 1280, adjustLocation2)
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', xPos, yPos)
    if cv2.waitKey(2) == ord('q'):
        break
cam.release()