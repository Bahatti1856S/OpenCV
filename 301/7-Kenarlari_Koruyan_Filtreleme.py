import cv2 as cv
import numpy as np

src = cv.imread("../images/surat.jpg")
cv.imshow("input", src)
cv.waitKey(0)

h, w = src.shape[:2]

# Kenar koruyucu filtre uygular (sigma_s: komşuluk boyutu/yumuşatma yarıçapı, sigma_r: kenar koruma hassasiyeti, RECURS_FILTER: hızlı özyinelemeli filtre)
dst = cv.edgePreservingFilter(src, sigma_s=10, sigma_r=0.9, flags=cv.RECURS_FILTER)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)  # İki görüntüyü yan yana koymak için 2 katı büyüklüğünde yeni tuval
result[0:h, 0:w, :] = src  # Sol yarıya orjinal görüntüyü yerleştirir
result[0:h, w:2 * w, :] = dst  # Sağ yarıya filtrelenmiş görüntüyü yerleştirir

result = cv.resize(result, (w, h // 2))
cv.imshow("result", result)
cv.waitKey(0)