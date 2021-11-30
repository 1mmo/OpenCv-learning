import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Green', blank)

# 2. Draw a Rectangle
#cv.rectangle(blank, (0, 0), (250, 300), (0, 250, 0), thickness=cv.FILLED) #thickness= -n ... +n
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2),
            (255, 0, 0), thickness=cv.FILLED)

cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=1) # 40- radius
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (250, 250), (250, 250), (255, 255, 255), thickness=1)
cv.imshow("Line", blank)

# 5. Write text
cv.putText(blank, 'Hello, Im Vladislav!!!!!!!', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 2.0, (0, 255, 0), 1)
cv.imshow("Hello", blank)

cv.waitKey(0)
