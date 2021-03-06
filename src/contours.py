import cv2 as cv
import numpy as np


img = cv.imread("photos/me.jpg")
print(img.shape)
cv.imshow('Frog', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Frog', gray)

#blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#ret, thresh =cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = cv.resize(blank, (1000, 1000), interpolation=cv.INTER_CUBIC)
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)
cv.imwrite("Contours.jpg", blank)

cv.waitKey(0)
