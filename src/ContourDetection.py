import cv2
import numpy as np


img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
cont = list(contours)
print(type(cont))
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow('Cont', color)
cv2.waitKey()
#cv2.destroyAllWindows()

img = cv2.pyrDown(cv2.imread("photos/katya.jpg", cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127,
                            255, cv2.THRESH_BINARY)
contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_cont = cv2.drawContours(img, contours, -1, (132, 112, 0), 3)
cv2.imshow("contours1", img_cont)

black = np.zeros_like(img)

for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    hull = cv2.convexHull(cnt)
    cv2.drawContours(black, [cnt], -1, (0, 255, 0), 2)
    cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
    cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)
    # find bounding box coordinates
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow("box", img)


    # find minimum area
    rect = cv2.minAreaRect(cnt)
    print(rect, '---rect')
    # calculate coordinates of the minimum area rectangle
    box = cv2.boxPoints(rect)
    print(box, '---box')
    # normalize coordinates to integers
    box = np.int0(box)
    print(box)
    # draw contours
    cv2.drawContours(img, [box], 0, (0,0,255), 3)
    cv2.imshow("box2", img)

    # calculate center and radius of minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    # cast to integers
    center = (int(x), int(y))
    radius = int(radius)
    # draw the circle
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)
    cv2.imshow("Circle", img)

cv2.imshow("hull", black)

cv2.drawContours(img, contours, -1, (255,0,0), 1)
cv2.imshow("contours", img)

cv2.waitKey()
cv2.destroyAllWindows()
