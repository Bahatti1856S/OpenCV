import cv2 as cv

src = cv.imread("../images/logo.png")

h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)  # X ekseninde (yatay türev / dikey kenarlar) 32-bit float hassasiyetinde Sobel filtresi uygular
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)  # Y ekseninde (dikey türev / yatay kenarlar) 32-bit float hassasiyetinde Sobel filtresi uygular

x_grad = cv.convertScaleAbs(x_grad)  # X gradyanındaki negatif değerlerin mutlak değerini alır ve 8-bit (0-255) görüntü formatına dönüştürür
y_grad = cv.convertScaleAbs(y_grad)  # Y gradyanındaki negatif değerlerin mutlak değerini alır ve 8-bit (0-255) görüntü formatına dönüştürür

cv.imshow("x_grad", x_grad)
cv.waitKey(0)

cv.imshow("y_grad", y_grad)
cv.waitKey(0)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)  # X ve Y gradyanlarını 16-bit işaretli tam sayı (CV_16S) formatında toplar (taşmayı önlemek için)
dst = cv.convertScaleAbs(dst)  # Birleştirilmiş gradyanın mutlak değerini alır ve 8-bit (0-255) görüntü formatına dönüştürür
cv.imshow("gradient", dst)
cv.waitKey(0)