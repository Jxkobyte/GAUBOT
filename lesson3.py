import cv2
import numpy as np

farm_img = cv2.imread('farm.png', cv2.IMREAD_UNCHANGED)
needle_img = cv2.imread('needle.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(farm_img, needle_img, cv2.TM_CCOEFF_NORMED)

threshold = 0.6
yloc, xloc = np.where(result >= threshold)

w = needle_img.shape[1]
h = needle_img.shape[0]



rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append((int(x), int(y), int(w), int(h)))
    rectangles.append((int(x), int(y), int(w), int(h)))

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

for (x, y, w, h) in rectangles:
    cv2.rectangle(farm_img, (x, y), (x+w, y+h), (0, 255, 255), 2)

#cv2.imshow("result", result)

cv2.imshow("farm", farm_img)
#cv2.imshow("needle", needle_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

