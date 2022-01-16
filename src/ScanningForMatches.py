import os
import numpy as np
import cv2


# Read the query image.
folder = 'tattoos'
query = cv2.imread(os.path.join(folder, 'query.png'), cv2.IMREAD_GRAYSCALE)

# create files, images, descriptors globals
files = []
images = []
descriptors = []
for (dirpath, dirname, filenames) in os.walk(folder):
    print(filenames)
    files.extend(filenames)
    print(files)
    for f in files:
        if f.endswith('npy') and f != 'query.npy':
            descriptors.append(f)


# Create the SIFT detector.
sift = cv2.xfeatures2d.SIFT_create()

# Perform SIFT feature detection and description on the
# query image.
query_kp, query_ds = sift.detectAndCompute(query, None)

# Define FLANN-base matching
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Create the FLANN matcher.
flann = cv2.FlannBasedMatcher(index_params, search_params)
# Define the minimum number of good matches for a suspect.
MIN_NUM_GOOD_MATCHES = 10

greatest_num_good_matches = 0
prime_suspect = None

print('>> Initiating picture scan...')
for d in descriptors:
    print(f'-------- analyzing {d} for matches --------')
    matches = flann.knnMatch(query_ds, np.load(os.path.join(folder, d)), k=2)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)
    num_good_matches = len(good_matches)
    name = d.replace('.npy', '').upper()
    if num_good_matches >= MIN_NUM_GOOD_MATCHES:
        print('%s is a suspect! (%d matches)' % \
            (name, num_good_matches))
        name_img_suspect = d.replace('.npy', '.png')
        print(f'NAME IMG SUSPECT \t {name_img_suspect}')
        print(type(name_img_suspect))
        img_suspect = cv2.imread(os.path.join(folder, name_img_suspect),
                                 cv2.IMREAD_GRAYSCALE)
        print(f'IMG {img_suspect}')
        kp_suspect, des_suspect = sift.detectAndCompute(img_suspect, None)
        kp_suspect_new, des_suspect_new = sift.detectAndCompute(img_suspect, None)
        if kp_suspect == kp_suspect_new:
            print("YES")
        else:
            print("NO")
        img_matches = cv2.drawMatchesKnn(
                query, query_kp, img_suspect, kp_suspect,
                good_matches, None)
        plt.imshow(img_matches)
        plt.show()
        if num_good_matches > greatest_num_good_matches:
            greatest_num_good_matches = num_good_matches
            prime_suspect = name

    else:
        print('%s is NOT a suspect. (%d matches)' % \
            (name, num_good_matches))

if prime_suspect is not None:
    print('Prime suspect is %s.' % prime_suspect)
else:
    print('There is no suspect.')
