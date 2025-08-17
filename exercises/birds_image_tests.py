import cv2
import numpy as np
import os
from exercises.dogs_image_tests import show_image, save_image

img = os.path.join('imgs', 'birds.jpg')
img = cv2.imread(img)
img = cv2.resize(img, (640, 480))

# edge detection
img_edges = cv2.Canny(img, 80, 210)
# show_image(img_edges)
# save_image(img_edges, 'birds_canny.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show_image(img_gray, 'Grayscale Image')

img_edges = cv2.cornerHarris(np.float32(img_gray), 2, 1, 0.04)
# show_image(img_edges, 'Harris Corners')
# save_image(img_edges, 'birds_HarrisCorner.jpg')


# Thresholding
_, img_thres = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
# show_image(img_thres, 'Thresholded Image')


# Finding contours
img_cont, hierarchy = cv2.findContours(img_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cont in img_cont:
    if cv2.contourArea(cont) >20:
        # cv2.drawContours(img, [cont], -1, (0, 255, 0), 5)

        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show_image(img, 'Contours on Image')



