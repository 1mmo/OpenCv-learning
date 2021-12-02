import cv2 as cv


img = cv.imread('photos/frog.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
inv_gray = 255 - img_gray
blurred_image = cv.GaussianBlur(inv_gray, (21, 21), 0, 0)
gray_sketch = cv.divide(img_gray, 255 - blurred_image, scale=256)
cv.imshow("Gray Sketch", gray_sketch)

cv.waitKey(0)
