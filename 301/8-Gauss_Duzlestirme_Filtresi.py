import cv2 as cv
import numpy as np

src = cv.imread("../images/surat.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

h, w = src.shape[:2]

# Bilateral (çift taraflı) filtre uygular: 0 (d: piksel komşuluk çapı, 0 ise sigmaSpace'den hesaplanır), 100 (sigmaColor: renk uzayı filtresi), 20 (sigmaSpace: koordinat uzayı filtresi)
dst = cv.bilateralFilter(src, 0, 100, 20)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

cv.imshow("result", result)
cv.waitKey(0)