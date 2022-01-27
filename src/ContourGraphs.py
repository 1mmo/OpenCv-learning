import cv2
import numpy as np
from matplotlib import pyplot as plt


img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255
print(f' Img matrix: \n {img[0]}')
print(f' Len of img: {len(img[0])}')
print(f' Type of img: {type(img[0])}')

ret, thresh = cv2.threshold(img, 127, 255, 0)
countours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

print(f' Contours matrix: \n {countours}')
print(f' Len of countours: {len(countours)}')
print(f' Type of countours: {type(countours)}')
found_countours = []
time_list = []
time = 0
for countour in countours:
    for i in countour:
        time += 1
        time_list.append(time)
        countour_list = i.tolist()
        for countour_list_i in countour_list:
            found_countours.append(sum(countour_list_i))
print(sum(found_countours))
print(time_list)

plt.plot(time_list, found_countours)
plt.show()

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, countours, -1, (0,255,0), 2)
cv2.imshow("Square", img)
cv2.waitKey(0)
