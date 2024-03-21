import random
import cv2
import numpy as np
import pyautogui
import time
import mss
import keyboard
from detect_ship import detect_ship
from coinmask import mask_circles
from edge_detection import detect_ship_and_draw_bounding_box, get_coin_locations
import threading
import math

sct = mss.mss()


monitor = {'left': 800, 'top': 450, 'width': 350, 'height': 350}

detection_range = 100 #80
going_up = True

def is_q_pressed():
    if keyboard.is_pressed('q'):
        time.sleep(0.5)
        return True
    return False

# Function for circle detection
def detect_custom_color_circle(image):
    global going_up, detection_range
    
    
    
    ship = detect_ship(image)
    
    
    if ship is not None:

        detect_ship_and_draw_bounding_box(image, going_up)

        x,y = ship
        yellow_pixel_count = 0

        if not going_up:
            xloc = x + detection_range

            # adjust height
            y = y + 15

            z = 15 # detection radius
            roi = image[y - z: y + z, xloc - z: xloc + z]
            if roi.size > 0:
                
                roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                lower_yellow = np.array([24, 164, 255])
                upper_yellow = np.array([26, 166, 255])
                mask_yellow = cv2.inRange(roi_hsv, lower_yellow, upper_yellow)
                yellow_pixel_count = np.count_nonzero(mask_yellow)
                cv2.circle(image, (xloc, y), z, (0, 0, 255), 1)

        elif going_up:
            yloc = y - detection_range

            # adjust x
            x = x + 20

            z = 15 # detection radius
            roi = image[yloc - z: yloc + z, x - z: x + z]
            if roi.size > 0:
                
                roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                lower_yellow = np.array([24, 164, 255])
                upper_yellow = np.array([26, 166, 255])
                mask_yellow = cv2.inRange(roi_hsv, lower_yellow, upper_yellow)
                yellow_pixel_count = np.count_nonzero(mask_yellow)
                cv2.circle(image, (x, yloc), z, (0, 0, 255), 1)

        # detect coin
        coin_detected = False
        # coin_locations = get_coin_locations(image)

        # for c in coin_locations:
        #     x,y = c
        #     z = 17 # detection radius
        #     roi = image[y - z: y + z, x - z: x + z]
        #     if roi.size > 0:
        #         roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        #         lower_bounds = np.array([6, 204, 255])
        #         upper_bounds = np.array([8, 206, 255])
        #         mask = cv2.inRange(roi_hsv, lower_bounds, upper_bounds)
        #         if np.count_nonzero(mask) > 0:
        #             coin_detected = True
        #             break


        if yellow_pixel_count > 1:# or coin_detected:
            
            pyautogui.click(clicks=7, interval=0.001)
            
            
                
            
            #print(yellow_pixel_count)
            going_up = not going_up
            
           
            

    time.sleep(0.001)
    return image

# # Read the input image
# image = cv2.imread('game.png')

print("Press 'q' to enter the game loop...")
    
while not is_q_pressed():
    pass

print("Starting...")

def start_game():
    global going_up
    while True:
        try:
            image_center = pyautogui.locateCenterOnScreen("ranked3.png", confidence=0.9)
            pyautogui.click(image_center.x, image_center.y)
            break
            
        except Exception as e:
            pass

        try:
            image_center2 = pyautogui.locateCenterOnScreen("new_match.png", confidence=0.9)
            pyautogui.click(image_center2.x, image_center2.y)
            break

        except Exception as e:
            pass

    # wait to detect spaceship
    while 1:
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        ship = detect_ship(img)
        if ship is not None:
            time.sleep(5)
            break
        time.sleep(1)

    # click once
    pyautogui.click()

    # set going up = true
    going_up = True

timer_completed = False
def timer():
    print("Timer started.")
    time.sleep(125 + random.randint(0, 10))  # Sleep for 2 minutes
    print("Timer completed.")
    # Set the flag to True after the timer completes
    global timer_completed
    timer_completed = True




while True:
    

    start_game()
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()
    pyautogui.click()

    while not timer_completed:
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)

        custom_color_circles_detected = detect_custom_color_circle(img)

        cv2.imshow('Ship Detected', custom_color_circles_detected)
        cv2.waitKey(1)
    
        if is_q_pressed():
            print("Exiting...")
            break
    timer_completed = False
    if is_q_pressed():
            print("Exiting...")
            break
    
    
    

# cv2.imshow('Ship Detected', custom_color_circles_detected)
# cv2.waitKey(0)
cv2.destroyAllWindows()