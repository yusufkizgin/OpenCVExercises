import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(x):
    global hueLow1
    hueLow1 = x
    print('Hue Low : ', hueLow1)
def onTrack2(x):
    global hueHigh1
    hueHigh1 = x
    print('Hue High : ', hueHigh1)
def onTrack3(x):
    global satLow1
    satLow1 = x
    print('Sat Low : ', satLow1)
def onTrack4(x):
    global satHigh1
    satHigh1 = x
    print('Sat High : ', satHigh1)
def onTrack5(x):
    global valLow1
    valLow1 = x
    print('Val Low : ', valLow1)
def onTrack6(x):
    global valHigh1
    #if(valHigh >= valLow):
    valHigh1 = x
    print('Val High : ', valHigh1)
def onTrack7(x):
    global hueLow2
    hueLow2 = x
    print('Hue Low : ', hueLow2)
def onTrack8(x):
    global hueHigh2
    hueHigh2 = x
    print('Hue High : ', hueHigh2)
def onTrack9(x):
    global satLow2
    satLow2 = x
    print('Sat Low : ', satLow2)
def onTrack10(x):
    global satHigh2
    satHigh2 = x
    print('Sat High : ', satHigh2)
def onTrack11(x):
    global valLow2
    valLow2 = x
    print('Val Low : ', valLow2)
def onTrack12(x):
    global valHigh2
    #if(valHigh >= valLow):
    valHigh2 = x
    print('Val High : ', valHigh2)

width = 640
height = 360
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTracker1')
cv2.moveWindow('myTracker1', width, 0)
cv2.createTrackbar('Hue Low', 'myTracker1', 10, 179, onTrack1)
cv2.createTrackbar('Hue High', 'myTracker1', 20, 179, onTrack2)
cv2.createTrackbar('Sature Low', 'myTracker1', 10, 255, onTrack3)
cv2.createTrackbar('Sature High', 'myTracker1', 250, 255, onTrack4)
cv2.createTrackbar('Value Low', 'myTracker1', 10, 255, onTrack5)
cv2.createTrackbar('Value High', 'myTracker1', 100, 255, onTrack6)

cv2.namedWindow('myTracker2')
cv2.moveWindow('myTracker2', width + 310, 0)
cv2.createTrackbar('Hue Low', 'myTracker2', 85, 179, onTrack7)
cv2.createTrackbar('Hue High', 'myTracker2', 255, 179, onTrack8)
cv2.createTrackbar('Sature Low', 'myTracker2', 150, 255, onTrack9)
cv2.createTrackbar('Sature High', 'myTracker2', 255, 255, onTrack10)
cv2.createTrackbar('Value Low', 'myTracker2', 100, 255, onTrack11)
cv2.createTrackbar('Value High', 'myTracker2', 255, 255, onTrack12)

while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound1 = np.array([hueLow1, satLow1, valLow1])
    upperBound1 = np.array([hueHigh1, satHigh1, valHigh1])
    lowerBound2 = np.array([hueLow2, satLow2, valLow2])
    upperBound2 = np.array([hueHigh2, satHigh2, valHigh2])
    mask1 = cv2.inRange(frameHSV, lowerBound1, upperBound1)
    mask2 = cv2.inRange(frameHSV, lowerBound2, upperBound2)
    myMask = cv2.bitwise_or(mask1, mask2)
    cv2.imshow('my WEBcam2', myMask)
    cv2.imshow('my WEBcam1', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()