import cv2


img = cv2.imread('sea.jpeg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#                 x1,y1       x2,y2       color    thickness
cv2.rectangle(img, (432,216), (524, 285), (0,255,0), 5)
cv2.rectangle(img, (973,259), (1070, 326), (255,0,255), 5)
cv2.putText(img, "Penguin", (432, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
#                  x1,y1   radius    color  thickness
cv2.circle(img, (252, 252), 50, (100,100,5), 5)

cv2.imshow("Original", img)
cv2.waitKey(0)