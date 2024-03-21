import cv2
import time
import numpy as np
import mss
sct = mss.mss()

monitor = {'left': 700, 'top': 400, 'width': 500, 'height': 400}

img = np.array(sct)

cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)

while True:

    sct_img = sct.grab(monitor)
    img = np.array(sct_img)

    # Perform object detection on the captured image
    detected_img = detect_objects(img)

    # Display the detected objects in a window
    cv2.imshow('Object Detection', detected_img)

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break