import cv2 as cv
import numpy as np

src = cv.imread("../images/kadin.jpg")

r = cv.selectROI("input", src, False)  # Kullanıcının fare ile bir ilgi alanı seçmesini sağlar; seçilen alanın (x, y, w, h) değerlerini döndürür

roi = src[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]  # Seçilen dikdörtgen alanı orijinal görüntüden kırpar
img = src.copy()

cv.rectangle(img,
             (int(r[0]), int(r[1])),  # Dikdörtgenin sol üst köşe koordinatı
             (int(r[0] + r[2]), int(r[1] + r[3])),  # Dikdörtgenin sağ alt köşe koordinatı
             (0, 0, 255), 2)  # Kopya görüntü üzerine seçilen alanı çerçeveleyen dikdörtgen çizer

mask = np.zeros(src.shape[:2], dtype=np.uint8)

rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))  # Seçilen ROI koordinatlarını tam sayı demetine dönüştürür

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

# GrabCut segmentasyonunu dikdörtgen modunda 11 iterasyon boyunca çalıştırarak ön planı arka plandan ayırır
cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv.GC_INIT_WITH_RECT)

# Maskede kesin ön plan (1) veya muhtemel ön plan (3) olarak etiketlenen pikselleri beyaza, arka planı siyaha çevirir
mask2 = np.where((mask == 1) + (mask == 3), 255, 0).astype("uint8")

result = cv.bitwise_and(src, src, mask=mask2)
cv.imshow("roi", roi)
cv.imshow("result", result)
cv.waitKey(0)