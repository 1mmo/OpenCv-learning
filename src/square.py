

import cv2

img = cv2.imread('photos/frog.jpg')
img[170:630, 100:500, 1] = 0



