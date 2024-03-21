import cv2
import numpy as np
import mss
sct = mss.mss()



def detect_ship(space_img):

    # space_img = cv2.imread('game.png', cv2.IMREAD_UNCHANGED)

    target_color = np.uint8([[[165, 102, 93]]])
    target_color_hsv = cv2.cvtColor(target_color, cv2.COLOR_BGR2HSV)
    h, s, v = target_color_hsv[0][0]

    lower_bound = np.array([h - 10, max(0, s - 10), max(0, v - 10)])
    upper_bound = np.array([h + 10, min(255, s + 10), min(255, v + 10)])

    space_img_hsv = cv2.cvtColor(space_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(space_img_hsv, lower_bound, upper_bound)
    # return if mask found nothing
    if np.count_nonzero(mask) == 0:
        return None

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    largest_label = np.argmax(stats[1:, cv2.CC_STAT_AREA]) + 1
    largest_mask = np.where(labels == largest_label, 255, 0).astype(np.uint8)
    nonzero_pixels = cv2.findNonZero(largest_mask)
    centroid_x = np.mean(nonzero_pixels[:, 0, 0])
    centroid_y = np.mean(nonzero_pixels[:, 0, 1])
    #cv2.rectangle(space_img, (int(centroid_x) - 5, int(centroid_y) - 5), (int(centroid_x) + 5, int(centroid_y) + 5), (0, 0, 255), 2)

    return (int(centroid_x), int(centroid_y))

if __name__ == '__main__':
    # space_img = cv2.imread('game.png', cv2.IMREAD_UNCHANGED)
    monitor = {'left': 800, 'top': 450, 'width': 350, 'height': 350}

    while 1:
        sct_img = sct.grab(monitor)
        space_img = np.array(sct_img)
        detect_ship(space_img)
        cv2.imshow('Game', space_img)
        cv2.waitKey(1)