import cv2 as cv

cap = cv.VideoCapture('../videos/man_speak.mp4')

# Arka plan çıkarıcı oluşturur (history=250: arka planı öğrenmek için baz alınan kare sayısı, varThreshold=250: pikselin ön plan sayılması için eşik değeri)
fgbg = cv.createBackgroundSubtractorMOG2(history=250, varThreshold=250)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)  # Mevcut kareye arka plan çıkarma işlemini uygular ve hareketli nesneleri gösteren siyah-beyaz maskeyi (fgmask) üretir
    background = fgbg.getBackgroundImage()  # Algoritmanın öğrendiği sabit arka plan görüntüsünü elde eder
    cv.imshow('input', frame)
    cv.imshow('mask', fgmask)
    cv.imshow('background', background)
    k = cv.waitKey(10)&0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()