import cv2

def pickcoulor(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = image[y,x]
        print("bgr colour code is:",b,g,r)

image = cv2.imread("Chocolate_Bar.jpg")
cv2.imshow("colourpicker",image)
cv2.setMouseCallback("image",pickcoulor)
cv2.waitKey(0)
cv2.destroyAllWindows()