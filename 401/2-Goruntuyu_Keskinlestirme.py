import cv2 as cv
import numpy as np

src = cv.imread("../images/logo.png")

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)  # Merkez pikseli güçlendirip komşu pikselleri çıkaran 3x3 keskinleştirme filtresi matrisi oluşturur

sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)  # filter2D burda 32bit hassasiyetinde birleştime için kullanıldı

sharpen_image = cv.convertScaleAbs(sharpen_image)

cv.imshow("sharpen_image", sharpen_image)
# Daha keskin fakat daha düşük kalitede resim elde ettik
cv.waitKey(0)