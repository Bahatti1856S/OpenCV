import cv2 as cv
import numpy as np

def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("../images/sudoku.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

binary = canny_demo(src)

# Doğru parçalarının başlangıç ve bitiş noktalarını tespit eder
# Parametreler: 1 (rho piksel çözünürlüğü), np.pi/180 (1 derece açı çözünürlüğü), 55 (eşik değeri), None (çıkış dizisi), 50 (minimum çizgi uzunluğu), 10 (parçalar arası izin verilen maksimum boşluk)
linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10)

if linesP is not None:
    for x1, y1, x2, y2 in linesP.reshape(-1, 4):# Koordinatları 4'lü gruplar halinde al
        cv.line(src, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1, cv.LINE_AA) # Mavi çizgi çiz

cv.imshow("hough line demo", src)
cv.waitKey(0)
