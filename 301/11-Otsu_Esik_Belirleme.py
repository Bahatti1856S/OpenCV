import cv2 as cv

src = cv.imread("../images/xantares.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

# Otsu yöntemiyle en uygun eşik değerini (ret) otomatik hesaplar ve görüntüyü siyah-beyaza (binary) dönüştürür
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

h, w = src.shape[:2]

cv.imshow("binary", binary)
cv.waitKey(0)