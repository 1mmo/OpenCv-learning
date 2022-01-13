import cv2
from matplotlib import pyplot as plt


# Load the image.
img0 = cv2.imread('photos/nasa_logo.png', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('photos/kennedy_space_center.jpg', cv2.IMREAD_GRAYSCALE)

# Perform ORB feature detection and description.
orb = cv2.ORB_create()
kp0, des0 = orb.detectAndCompute(img0, None)
kp1, des1 = orb.detectAndCompute(img1, None)

# Perform brute-force matching.
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
pairs_of_matches = bf.knnMatch(des0, des1, k=2)

# Sort the pairs of  matches by distance.
pairs_of_matches = sorted(pairs_of_matches, key=lambda x:x[0].distance)



# Show the matches.
img_pairs_of_matches = cv2.drawMatchesKnn(img0, kp0, img1, kp1, 
        pairs_of_matches[:25],  img1, 
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img_pairs_of_matches)
plt.show()
