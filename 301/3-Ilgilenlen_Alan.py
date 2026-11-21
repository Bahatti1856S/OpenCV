# ROI

import cv2 as cv

src = cv.imread("../images/miuul.png")
h, v = src.shape[:2]
img = src.copy()

# Görüntüden belirli bir bölgeyi kırp ve ekranda göster
roi = img[100:250, 250:380, :]
roi.shape[:2]
cv.imshow("roi", roi)
cv.waitKey(0)

# Kırpılan bölgeyi kopya görüntünün sol üst köşesine yapıştır
img[0:150, 0:130, :] = roi
cv.imshow("img", img)
cv.waitKey(0)

# ROI bölgesini %30 oranında küçült ve göster
res = cv.resize(roi, None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(0)

# Küçültülen bölgeyi kopya görüntünün sol üst köşesine yapıştır
res.shape[:2]
img[0:45, 0:39, :] = res
cv.imshow("img", img)
cv.waitKey(0)

# Küçültülen bölgeyi orijinal görüntünün sol üst köşesine yapıştır
src[0:45, 0:39, :] = res
cv.imshow("src", src)
cv.waitKey(0)

# Tüm pencereleri kapat
cv.destroyAllWindows()