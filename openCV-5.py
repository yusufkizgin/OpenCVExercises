import cv2
print(cv2.__version__)
width = 640
height = 360
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
    #frame[140:220, 250:390] = (255,0,0)
    cv2.rectangle(frame, (250,140), (390,220), (0,255,0), 2)
    cv2.circle(frame, (int(width/2), int(height/2)), myRadius, myColor, 2)
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, myText, (120,60), myFont, 0.5, (255, 0, 0), 1)
    cv2.imshow('my WEBcam1', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()