import cv2 as cv


img = cv.imread('photos/frog.jpg')
cv.imshow('FROG', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilating", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)
cv.imshow("Eroding", eroded)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
