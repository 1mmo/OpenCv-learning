import cv2
from matplotlib import pyplot as plt

bg_subtractor = cv2.createBackgroundSubtractorKNN(detectShadows=True)


OPENCV_MAJOR_VERSION = int(cv2.__version__.split('.')[0])

BLUR_RADIUS = 21
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 11))

cap = cv2.VideoCapture("photos/chapter08_traffic.flv")

# Capture several frame to allow the camera's autoexposure to adjust.
for i in range(10):
    success, frame = cap.read()
if not success:
    exit(1)

gray_background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_background = cv2.GaussianBlur(gray_background, 
                                  (BLUR_RADIUS, BLUR_RADIUS), 0)

success, frame = cap.read()
found_countours = []
time_list = []
time = 0
while success:

    fg_mask = bg_subtractor.apply(frame)

    _, thresh = cv2.threshold(fg_mask, 244, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thres test", thresh)
    cv2.erode(thresh, erode_kernel, thresh, iterations=2)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=2)

    if OPENCV_MAJOR_VERSION >= 4:
        # OpenCV 4 or a later version is being used.
        contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) > 1000:
            x, y, w, h = cv2.boundingRect(c)
            P_rectangle = x + y + w + h
            found_countours.append(P_rectangle)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    #plt.plot(time_list, found_countours)
    #plt.show()
    cv2.imshow('knn', fg_mask)
    cv2.imshow('thresh', thresh)
    cv2.imshow('detection', frame)

    k = cv2.waitKey(1)
    if k == 27: # Escape
        break

    success, frame = cap.read()

print(len(time_list))
print(len(found_countours))
plt.plot(time_list[:len(found_countours)], found_countours)
plt.show()
