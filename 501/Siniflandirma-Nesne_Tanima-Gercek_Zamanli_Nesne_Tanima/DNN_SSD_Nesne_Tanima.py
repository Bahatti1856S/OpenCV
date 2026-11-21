import cv2 as cv

model_bin = "MobileNetSSD_deploy.caffemodel"
config_text = "MobileNetSSD_deploy.prototxt"

objName = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"]

# Caffe tabanlı DNN modelini yükle
net = cv.dnn.readNetFromCaffe(config_text, model_bin)

image = cv.imread("../../images/dog.jpg")
h = image.shape[0]
w = image.shape[1]

# Modelin son katman bilgisini al
layerNames = net.getLayerNames()
lastLayerId = net.getLayerId(layerNames[-1])
lastLayer = net.getLayer(lastLayerId)

blobImage = cv.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)

# Girdiyi modele ver ve nesne tespiti yap
net.setInput(blobImage)
cvOut = net.forward()

# Tespit edilen tüm nesneleri döngüyle kontrol et
for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])      # Güven skoru
    objIndex = int(detection[1])     # Nesne sınıf indeksi

    # Güven skoru %50'nin üzerindeyse çizim yap
    if score > 0.5:
        # Normalize koordinatları piksel değerlerine çevir
        left = detection[3] * w
        top = detection[4] * h
        right = detection[5] * w
        bottom = detection[6] * h

        cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), 2)

        # Skor ve sınıf adını kutunun üzerine yazdır
        cv.putText(image, "score:%.2f, %s" % (score, objName[objIndex]),(int(left) - 10, int(top) - 5), cv.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2, 8)

cv.imshow("mobilenet-ssd-demo", image)
cv.imwrite("result.png", image)

cv.waitKey(0)