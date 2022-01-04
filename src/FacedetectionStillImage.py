import cv2


face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')
img = cv2.imread('photos/boys.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.08, 20)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
cv2.namedWindow('Woodctutters Detected!')
cv2.imshow('Woodcutters Detected!', img)
cv2.waitKey(0)
