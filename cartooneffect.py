import cv2
image2 = cv2.imread("face2.jpg")
cv2.imshow("normal face",image2)
cv2.waitKey(0)
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(
    blur, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY, 9, 9
)

color = cv2.bilateralFilter(image2, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()