import cv2 as cv

src = cv.imread("../images/xantares.jpg")
cv.imshow("xantares", src)
cv.waitKey(0)

# Canny kenar tespiti uygular: 100 (alt eşik değeri), 300 (üst eşik değeri)
edge = cv.Canny(src, 100, 300)  # Belirlenen eşik değerlerine göre kenarları çıkarır (siyah-beyaz maske görüntüsü oluşturur)
cv.imshow("mask image", edge)
cv.waitKey(0)