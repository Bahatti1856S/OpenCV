import cv2 as cv
import numpy as np

src = cv.imread('../images/bloklar.jpg')

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(gray, 100, 0.05, 10) # Shi-Tomasi algoritması ile köşeleri bulur
    print(len(corners))
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)

    winSize = (3, 3)
    zeroZone = (-1, -1)

    # İyileştirme işleminin durma kriterini belirler
    criteria = (cv.TERM_CRITERIA_EPS + cv.TermCriteria_COUNT, 40, 0.001)
    # Tespit edilen köşe koordinatlarını alt-piksel hassasiyetine getirerek daha kesin hale getirir
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

    for i in range(corners.shape[0]):
        print(" -- Refined Corner [", i, "]  (", corners[i, 0, 0], ",", corners[i, 0, 1], ")")
    return image

result = process(src)
cv.imshow("Subpixel", result)
cv.waitKey(0)
cv.destroyAllWindows()