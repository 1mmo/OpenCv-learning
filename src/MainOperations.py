import cv2


image = cv2.imread("matrix.jpg")
#cv2.imshow("Original image", image)
#cv2.waitKey(0) # Чтобы картинка сразу не закрывалась
#print(image.shape) # Размер картинки


# Нам надо сохранить соотношение сторон
# чтобы изображение не исказилось при уменьшении
# для этого считаем коэф. уменьшения стороны
final_wide = 200
r = float(final_wide) / image.shape[1]
dim = (final_wide, int(image.shape[0] * r))
# уменьшаем изображение до подготовленных размеров
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#cv2.imshow("Resize image", resized)
#cv2.waitKey(0)

# Вырежем участок изображения используя срезы
cropped = image[30:130, 150:300]
#cv2.imshow("Cropped image", cropped)
#cv2.waitKey(0)

# Получим размеры изображения для поворота
# и вычислим центр изображения
h, w = image.shape[:2]
center = (w / 2, h / 2)
# повернем изображение на 180 градусов
M = cv2.getRotationMatrix2D(center, 180, 1.0) # Считаем матрицу преобразования
rotated = cv2.warpAffine(image, M, (w, h)) # Поворачиваем изображение
#cv2.imshow("Rotated image", rotated)
#cv2.waitKey(0)

# отразим изображение по горизонтали
flip_image = cv2.flip(image, 1)
cv2.imshow("Flip image", flip_image)
cv2.waitKey(0)

# Сохранение изображения на диск
cv2.imwrite("flip.png", flip_image)
