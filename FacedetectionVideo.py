import cv2


face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w), (x+2, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
        cv2.imshow('Face Detection', frame)

