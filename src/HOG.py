import cv2


def is_inside(i, o):
    print(' Function is_inside... ')
    print(f' I = {i}')
    print(f' o = {o}')
    ix, iy, iw, ih = i
    ox, ox, ow, oh = o
    return (ix > ox and ix + iw < ox + ow and
            iy > oy and iy + ih < oy + oh)

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread('photos/haying.jpg')
#img = cv2.resize(img, (580, 580), interpolation=cv2.INTER_CUBIC)

found_rects, found_weights = hog.detectMultiScale(
        img, winStride=(4, 4), scale=1.02, finalThreshold=.0)
print(found_rects)
print(found_weights)

found_rects_filtered = []
found_weights_filtered = []
for ri, r in enumerate(found_rects):
    for qi, q in enumerate(found_rects): 
        if ri != qi and is_inside(r, q):
            print(f'{ri} != {qi}')
            break
    else:
        found_rects_filtered.append(r)
        found_weights_filtered.append(found_weights[ri])

for ri, r in enumerate(found_rects_filtered):
    x, y, w, h = r
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
    text = f'{found_weights_filtered[ri]}.2f'
    cv2.putText(img, text, (x, y - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2.imshow("Women in Hayfield Datected", img)
cv2.waitKey(0)
