import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(x):
    global hueLow
    hueLow = x
    print('Hue Low : ', hueLow)
def onTrack2(x):
    global hueHigh
    hueHigh = x
    print('Hue High : ', hueHigh)
def onTrack3(x):
    global satLow
    satLow = x
    print('Sat Low : ', satLow)
def onTrack4(x):
    global satHigh
    satHigh = x
    print('Sat High : ', satHigh)
def onTrack5(x):
    global valLow
    valLow = x
    print('Val Low : ', valLow)
def onTrack6(x):
    global valHigh
    #if(valHigh >= valLow):
    valHigh = x
    print('Val High : ', valHigh)

width=640
height=360
cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

hueLow = 10
hueHigh = 20
satLow = 10
satHigh = 250
valLow = 10
valHigh = 100

cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker', width, 0)
cv2.createTrackbar('Hue Low', 'myTracker', 10, 179, onTrack1)
cv2.createTrackbar('Hue High', 'myTracker', 20, 179, onTrack2)
cv2.createTrackbar('Sature Low', 'myTracker', 10, 255, onTrack3)
cv2.createTrackbar('Sature High', 'myTracker', 250, 255, onTrack4)
cv2.createTrackbar('Value Low', 'myTracker', 10, 255, onTrack5)
cv2.createTrackbar('Value High', 'myTracker', 100, 255, onTrack6)

while True:
    ignore,  frame = cam.read()
    frame = cv2.flip(frame,1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    #"myMask = cv2.bitwise_not(myMask)
    myObj = cv2.bitwise_and(frame, frame, mask = myMask)
    cv2.imshow('myMask', myMask)
    #cv2.imshow('myObj', myObj)
    #cv2.moveWindow('myObj', width, height)
    cv2.moveWindow('myMask', 0, height)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()