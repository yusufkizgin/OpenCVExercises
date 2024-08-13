import cv2
print(cv2.__version__)
width = 720
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 60)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('my WEBcam1', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()