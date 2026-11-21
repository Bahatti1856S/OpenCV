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

# Doğruları tespit eder: 1 (rho piksel çözünürlüğü), np.pi/180 (1 derece açı çözünürlüğü), 150 (doğru sayılması için minimum kesişim eşiği)
lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:  # Eğer görüntüde en az bir doğru tespit edildiyse döngüye girer
    for i in range(0, len(lines)):  # Tespit edilen tüm doğrular üzerinde tek tek döner
        rho = lines[i][0][0]  # Doğrunun orijine (sol üst köşeye) olan dik uzaklığını (rho) alır
        theta = lines[i][0][1]  # Doğrunun açısını (radyan cinsinden theta) alır
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)  # Orijinal görüntü üzerine kırmızı doğru çizer

cv.imshow("Hoffman",src)
cv.waitKey(0)