import cv2
import numpy as np
import pyautogui
import time
import mss
import keyboard

sct = mss.mss()

monitor = {'left': 700, 'top': 400, 'width': 500, 'height': 400}

detection_range = 100
going_up = True

def is_q_pressed():
    if keyboard.is_pressed('q'):
        time.sleep(0.5)
        return True
    return False


def detect_custom_color_circle(image):
    

    time.sleep(0.02)
    return image



print("Press 'q' to enter the game loop...")
    
while not is_q_pressed():
    pass

print("Starting...")

while True:

    sct_img = sct.grab(monitor)
    img = np.array(sct_img)

    custom_color_circles_detected = detect_custom_color_circle(img)

    cv2.imshow('Ship Detected', custom_color_circles_detected)
    cv2.waitKey(1)

    if is_q_pressed():
        print("Exiting...")
        break

cv2.destroyAllWindows()