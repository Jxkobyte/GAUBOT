import cv2
import numpy as np
from detect_ship import detect_ship 


img = cv2.imread('game.png', cv2.IMREAD_UNCHANGED)

def get_coin_locations(space_img):
    target_color = np.uint8([[[211, 96, 244]]])  # Update with your coin color
    target_color_hsv = cv2.cvtColor(target_color, cv2.COLOR_BGR2HSV)
    h, s, v = target_color_hsv[0][0]

    lower_bound = np.array([h - 10, max(0, s - 10), max(0, v - 10)])
    upper_bound = np.array([h + 10, min(255, s + 10), min(255, v + 10)])

    space_img_hsv = cv2.cvtColor(space_img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(space_img_hsv, lower_bound, upper_bound)
    # Return None if mask found nothing
    if np.count_nonzero(mask) == 0:
        return []

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    coin_locations = []
    for label in range(1, num_labels):  # Start from 1 to skip background
        coin_mask = np.where(labels == label, 255, 0).astype(np.uint8)
        nonzero_pixels = cv2.findNonZero(coin_mask)
        centroid_x = np.mean(nonzero_pixels[:, 0, 0])
        centroid_y = np.mean(nonzero_pixels[:, 0, 1])
        coin_locations.append((int(centroid_x), int(centroid_y)))

    filtered_coin_locations = []
    for i in range(len(coin_locations)):
        is_unique = True
        for j in range(i + 1, len(coin_locations)):
            x1, y1 = coin_locations[i]
            x2, y2 = coin_locations[j]
            # Check if the distance between the two coin locations is greater than 5 pixels
            if abs(x1 - x2) < 5 and abs(y1 - y2) < 5:
                is_unique = False
                break
        if is_unique:
            filtered_coin_locations.append(coin_locations[i])

    #print("Filtered Coin locations:", filtered_coin_locations)
    

    return filtered_coin_locations



def detect_ship_and_draw_bounding_box(img, going_up):
    

    def draw_boundary(angle, img):
    
        x, y = detect_ship(img)
        angle_radians = np.deg2rad(angle)

        # Calculate the endpoint coordinates
        end_x = int(x + 1000 * np.cos(angle_radians))
        end_y = int(y + 1000 * np.sin(angle_radians))

        # Draw the line
        cv2.line(img, (x, y), (end_x, end_y), (50, 100, 255), 2)

    if (going_up):
        draw_boundary(195 + 180, img) # ------
    else:
        draw_boundary(105 + 180, img) # |


if __name__ == '__main__':

    # x,y = detect_ship(img)
    # cv2.circle(img, (int(x), int(y)), 17, (0, 255, 0), 3)

    detect_ship_and_draw_bounding_box(img, True)
    #print(get_coin_locations(img))

    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
