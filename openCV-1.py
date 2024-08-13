import cv2
print(cv2.__version__)
cam = cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('my WEBcam1', frame)
    cv2.imshow('my WEBcam2', grayFrame)
    cv2.imshow('my WEBcam3', grayFrame)
    cv2.imshow('my WEBcam4', frame)
    cv2.moveWindow('my WEBcam1', 10, 10)
    cv2.moveWindow('my WEBcam2', 750, 10)
    cv2.moveWindow('my WEBcam3', 10, 500)
    cv2.moveWindow('my WEBcam4', 750, 500)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()