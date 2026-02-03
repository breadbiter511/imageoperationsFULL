import cv2
image2 = cv2.imread("imageoperations/pug.jpg",0)
cv2.imshow("pug in grey scale",image2)
cv2.waitKey(0)
(rows,columns) = image2.shape[:2]
r = cv2.getRotationMatrix2D((columns/2,rows/2),45,1)
results = cv2.warpAffine(image2,r,(columns,rows))
cv2.imshow("rotatedimageby45",results)
cv2.waitKey(0)
r1 = cv2.getRotationMatrix2D((columns/2,rows/2),180,1)
results = cv2.warpAffine(image2,r1,(columns,rows))
cv2.imshow("rotatedimageby45",results)
cv2.waitKey(0)