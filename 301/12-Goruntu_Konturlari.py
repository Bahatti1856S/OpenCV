import cv2 as cv

def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)  # Gürültüyü azaltmak için 3x3 çekirdek boyutuyla Gauss bulanıklaştırması uygular
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)  # Otsu yöntemiyle otomatik eşik değeri bulup görüntüyü siyah-beyaza (binary) çevirir
    cv.imshow("binary", binary)
    return binary

def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t * 2)  # 100 ve 200 değerleriyle kenar tespiti uygular
    cv.imshow("canny_output", canny_output)
    return canny_output

src = cv.imread("../images/karakter.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

binary = threshold_demo(src)

canny = canny_demo(src)

# Kenar görüntüsündeki tüm konturları ve iç içe hiyerarşilerini (RETR_TREE) bulur
contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):  # Bulunan tüm konturlar üzerinde tek tek döner
    # Her bir konturu orijinal görüntünün üzerine kırmızı renkte, 2 piksel kalınlığında ve 8-bağlantılı çizgi tipiyle çizer
    cv.drawContours(src, contours, c, (0, 0, 255), 2, 8)

cv.imshow("contours-demo", src)
cv.waitKey(0)