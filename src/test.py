import cv2 as cv


img = cv.imread("photos/frog.jpg")
cv.imshow("frog", img)
face = img[186:515, 200:500]
cv.imshow("face", face)
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
cv.imshow('Face gray', gray)
face[:, :, 0] = gray
cv.imshow("face_lose_channgel_B", face)
#img[186:515, 200:500, :] = face
#cv.imshow("Changed face", img)

cv.waitKey(0)
cv.destroyAllWindows()
