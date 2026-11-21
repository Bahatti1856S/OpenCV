import numpy as np
import cv2 as cv


path = "../../images/"

# Caffe modelinin mimari ve ağırlık dosyaları
protxt = "deploy.prototxt"
bin_model = "bvlc_googlenet.caffemodel"

# Önceden eğitilmiş DNN modelini yükle
net = cv.dnn.readNetFromCaffe(protxt, bin_model)

# Modeldeki tüm katman isimlerini al
layer_names = net.getLayerNames()

# Her katmanın ID, tür ve isim bilgisini konsola yazdır
for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name: %s" %
          (id, layer.type, layer.name))

# ImageNet sınıf isimlerini dosyadan okuyup listeye aktar
with open("classification_classes_ILSVRC2012.txt", "r") as f:
    classes = f.read().split("\n")

# Modeli yeniden yükle
net = cv.dnn.readNetFromCaffe(protxt, bin_model)

image2 = cv.imread(path + "dog2.jpg")

# Görüntüyü modelin beklediği formata dönüştür
blob = cv.dnn.blobFromImage(image2, 1.0, (224,224), (104,117,123), False, crop=False)

result = np.copy(image2)

# Girdiyi modele ver ve ileri besleme işlemini çalıştır
net.setInput(blob)
out = net.forward()

# Çıktı matrisini tek boyutlu diziye çevir
out = out.flatten()

# En yüksek olasılığa sahip sınıfın indeksini bul
classId = np.argmax(out)
print(classId)

# En yüksek olasılık skorunu al
confidence = out[classId]
print(confidence)

# Tahmin süresini milisaniye cinsinden hesapla ve görüntüye yazdır
t, _ = net.getPerfProfile()
label = "cost time: %.2f ms" % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0,20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

# Tahmin edilen sınıf adını ve güven skorunu görüntüye yazdır
label = "%s: %.4f" % (classes[classId] if classes else "Class #%d" % classId, confidence)
cv.putText(result, label, (0,60), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

result = cv.resize(result, (image2.shape[1], image2.shape[0]))

show_img = np.hstack((image2, result))
cv.namedWindow("demo", cv.WINDOW_NORMAL)
cv.imshow("demo", show_img)

cv.waitKey(0)