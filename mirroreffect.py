import cv2
camera = cv2.VideoCapture(0)
while True:
    frame1,frame2 = camera.read()
    mirror = cv2.flip(frame2,1)
    cv2.imshow("mirroreffectimage",mirror)
    if cv2.waitKey(1) == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()