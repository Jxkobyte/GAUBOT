import cv2 

img = cv2.imread('girl-original.jpeg')

# print(img)
# print(img.shape)

small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#small[0:10,0:100] = (0,0,255)

gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Original", img)
#cv2.imshow("Small", small)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)

cv2.imwrite('girl-gray.jpeg', gray)