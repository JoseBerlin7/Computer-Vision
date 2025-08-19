import numpy as np
import cv2

def get_hsv_color_range(color_name):
    col = np.uint8([[color_name]])
    hsv_col = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)[0][0]

    lower_bound = np.array([hsv_col[0] - 10, 100, 100])
    upper_bound = np.array([hsv_col[0] + 10, 255, 255])

    return lower_bound, upper_bound