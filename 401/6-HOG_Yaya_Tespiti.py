import cv2 as cv

src = cv.imread("../images/yayalar.jpg")

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())  # Burada insan tespiti yapılır

# Görüntüde farklı ölçeklerde yaya tespiti yapar
rects, weights = hog.detectMultiScale(
    src,
    winStride=(8, 8),   # Tarama penceresinin x ve y eksenlerinde kaydırılma adım aralığı (piksel)
    padding=(32, 32),   # Tarama penceresinin kenarlarına eklenen dolgu (boşluk) miktarı
    scale=1.05          # Görüntü piramidinde her katmanda uygulanacak ölçek küçültme oranı
)

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Yayalar", src)
cv.waitKey(0)