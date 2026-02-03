import cv2

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b,g,r = img[y,x]
        print("BGR:",b,g,r)

img = cv2.imread("Chocolate_Bar.jpg")
cv2.imshow("Image",img)
cv2.setMouseCallback("Image", pick_color)

cv2.waitKey(0)
cv2.destroyAllWindows()