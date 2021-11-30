import cv2 as cv

img = cv.imread("frog.jpg")
capture = cv.VideoCapture("videos/leo.mp4")

def rescaleFrame(frame, scale=0.2):
    """ Images, Videos and Live Video """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    frame = frame[600:1080, 0:1920]
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
