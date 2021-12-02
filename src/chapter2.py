import cv2 as cv
import numpy as np
import os


# Make an array of 120,000 random bytes
#randomByteArray = bytearray(os.urandom(120000))
#flatNumpyArray = np.array(randomByteArray)
#print(randomByteArray)
#print(flatNumpyArray)


# Convert the array to make a 400x300 grayscale image
#grayImage = flatNumpyArray.reshape(300, 400)
#cv.imshow("RandomGray", grayImage)

# Convert the array to make a 400x100 color image
#bgrImage = flatNumpyArray.reshape(100, 400, 3)
#cv.imshow('RandomColor', bgrImage)

#cv.waitKey(0)

""" Accessing image data with numpy.array """
img = cv.imread('photos/frog.jpg')
#img[287, 362] = [255, 255, 255] # White point
#img.itemset((287, 362, 0), 255) # itemset better than img[287, 362]
#cv.imshow("Ya dodik", img)
#print(img.item(150, 120, 0))


#img[:, :, 1] = 0
#cv.imshow('Not green', img)


""" Regions of interests """

#my_roi = img[0:100, 0:100]
#img[300:400, 300:400] = my_roi
#cv.imshow('Copy', img)

#print(img.shape)
#print(img.size)
#print(img.dtype)


#cv.waitKey(0)



""" Reading/writing a video file """

#videoCapture = cv.VideoCapture("videos/leo.mp4")
#fps = videoCapture.get(cv.CAP_PROP_FPS)
#size = (int(videoCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
#        int(videoCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
#videoWriter = cv.VideoWriter(
#        "MyOutputVid.mp4", 0x7634706d,
#        fps, size)

#success, frame = videoCapture.read()
#while success:
#    videoWriter.write(frame)
#    succes, frame = videoCapture.read()


""" Capturing camera frames """

#cameraCapture = cv.VideoCapture(0)
#fps = 30 # An assumption
#size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),
#        int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
#videoWriter = cv.VideoWriter(
#        "MyOutpuVid.avi", cv.VideoWriter_fourcc('I', '4', '2', '0'),
#        fps, size)
#
#success, frame = cameraCapture.read()
#numFramesRemaining = 10 * fps - 1 # 10 seconds of frames
#while success and numFramesRemaining > 0:
#    videoWriter.write(frame)
#    succes, frame = cameraCapture.read()
#    numFramesRemaining -= 1
