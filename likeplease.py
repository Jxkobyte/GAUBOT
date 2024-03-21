import cv2
import mss
sct = mss.mss()
import numpy as np


monitor = {'left': 840, 'top': 600, 'width': 150, 'height': 150}

sct_img = sct.grab(monitor)
img = np.array(sct_img)

cv2.imshow('Game', img)
cv2.waitKey(0)