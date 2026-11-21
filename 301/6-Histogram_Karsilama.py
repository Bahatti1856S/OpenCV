import cv2 as cv


src1 = cv.imread("../images/logo.png")
src2 = cv.imread("../images/miuul.png")
src3 = cv.imread("../images/manzara.jpg")


hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist: Görüntülerin 2 boyutlu renk histogramını hesaplar
# Parametreler: [görüntü], [0, 1] (Hue ve Saturation kanalları), None (maske yok), [60, 64] (kutu/bin sayıları), [0, 180, 0, 256] (değer aralıkları)
hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

# normalize: Histogram değerlerini karşılaştırma yapabilmek için 0 ile 1.0 aralığına ölçekler (Min-Max normalizasyonu)
cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist: İki farklı görüntünün histogramlarını karşılaştırarak benzerlik skoru üretir

# HISTCMP_CORREL: Korelasyon yöntemini kullanır (Sonuç 1'e ne kadar yakınsa görüntüler o kadar benzerdir)
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)  # 1. ve 2.'yi karşılaştırır
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)  # 1. ve 3.'yü karşılaştırır
cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)  # 2. ve 3.'yü karşılaştırır
