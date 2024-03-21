import cv2
import numpy as np

def mask_circles(image):
    edge_buffer=2
    min_radius = 10
    max_radius = 50

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect circles using HoughCircles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=min_radius, maxRadius=max_radius)

    # If circles are detected
    if circles is not None:
        # Convert the circles to integer coordinates
        circles = np.round(circles[0, :]).astype("int")

        # Create an empty mask
        mask = np.zeros(gray.shape, dtype=np.uint8)

        # Loop over all detected circles
        for (x, y, r) in circles:
            # Increase the radius slightly to account for edges
            r += edge_buffer

            # Create a mask for the current circle
            circle_mask = np.zeros(gray.shape, dtype=np.uint8)
            cv2.circle(circle_mask, (x, y), r, 255, -1)

            # Add the current circle mask to the overall mask
            mask = cv2.bitwise_or(mask, circle_mask)

        # Invert the mask (areas to avoid become white)
        mask = cv2.bitwise_not(mask)

        # Apply the mask to the input image
        masked_image = cv2.bitwise_and(image, image, mask=mask)

        return masked_image

    return image


if __name__ == "__main__":
    # Example usage:
    masked_image = mask_circles('game.png')

    if masked_image is not None:
        # Display the masked image
        cv2.imshow("Masked Image", masked_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No circles detected.")
