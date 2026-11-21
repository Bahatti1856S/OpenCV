import cv2 as cv
import numpy as np

path = "../images"

def templat_demo():
    src = cv.imread(path + "/opencv.png")
    tpl = cv.imread(path + "/template.png")

    if src is None:
        print("Error: opencv.png not found!")
        return
    if tpl is None:
        print("Error: template.png not found!")
        return

    cv.imshow("input", src)
    cv.imshow("template", tpl)

    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    tpl_gray = cv.cvtColor(tpl, cv.COLOR_BGR2GRAY)

    th, tw = tpl_gray.shape[:2]

    if th > src_gray.shape[0] or tw > src_gray.shape[1]:
        print("Error: Template is larger than source image!")
        print("SRC:", src_gray.shape)
        print("TPL:", tpl_gray.shape)
        return

    # Şablon eşleştirme
    # Şablonu ana görüntü üzerinde tarar ve benzerlik haritası çıkarır
    result = cv.matchTemplate(src_gray, tpl_gray, cv.TM_CCOEFF_NORMED)

    t = 0.8
    loc = np.where(result >= t)  # Benzerlik skoru 0.8 ve üzerinde olan tüm konumların indekslerini bulur

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, (pt[0], pt[1]), (pt[0] + tw, pt[1] + th), (255, 0, 0), 3)

    cv.imshow("Eşleştirme", src)

templat_demo()
cv.waitKey(0)
