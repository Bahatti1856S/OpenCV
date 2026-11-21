import cv2 as cv
import numpy as np

src = cv.imread("../images/qr.png")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
qrcoder = cv.QRCodeDetector() # QR Kodu bu aşamada tespit ediliyor

data, points, straight_qrcode = qrcoder.detectAndDecode(gray) # QR Kodu decode edilipi içindeki ver vs. oknuyor

print(points)

result = np.copy(src)

cv.drawContours(result,[np.int32(points)], 0,(0,0, 255), 2) # QR Kodun etrafına kare çizildi

print("qrcode information is :\n%s" % data)
cv.imshow("qrcode", result)
cv.waitKey(0)
cv.destroyAllWindows()