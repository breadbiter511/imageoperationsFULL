import cv2
camera = cv2.VideoCapture(0)
while True:
    index,frame = camera.read()
    if not index:
        break
    upsidedown = cv2.rotate(frame,cv2.ROTATE_180)
    cv2.imshow("upside down camera",upsidedown)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release(cv2.destroyAllWindows)