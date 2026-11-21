import cv2 as cv
import numpy as np

src = cv.imread("../images/para.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

# dp=1 (çözünürlük oranı), minDist=10 (daire merkezleri arası min mesafe), param1=100 (Canny üst eşiği), param2=50 (merkez tespit eşiği), minRadius/maxRadius (aranacak min-max yarıçap)
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp=1, minDist=10, param1=100, param2=50, minRadius=20, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for (cx, cy, r) in circles[0, :]:
        cv.circle(src, (cx, cy), r, (0, 0, 255), 3) # Yarıçap ile kırmızı daire çizer
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 3) # Dairenin merkezine yeşil nokta çizer
cv.imshow("hough line demo", src)
cv.waitKey(0)