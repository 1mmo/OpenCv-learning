import cv2
import numpy as np


img = cv2.imread("photos/frog.jpg", 0)
img_canny = cv2.Canny(img, 200, 300)
cv2.imshow('frog', img)
cv2.imshow("canny", img_canny)
cv2.waitKey()
cv2.destroyAllWindows()
