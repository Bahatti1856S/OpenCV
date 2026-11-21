import cv2 as cv
import numpy as np

image=np.zeros((512,512,3),np.uint8)

cv.rectangle(image,
             (100,100),#X
             (300,300),#Y
             (255,0,0),#Renk
             2,#Kalinlik
             cv.LINE_8,#Cizgi Tipi
             0#Kayma(shift)
             )
cv.circle(image,
          (256,256),#Merkez X
          50,#Yaricap
          (0,255,0),#Renk
          2,#Kalinlik
          cv.LINE_8,#Cizgi Tipi
          0#Kayma(Shift)
          )
cv.ellipse(image,
           (256,256),#Merkez X
           (150,50),#Eksenleri
           360,#Durus Acisi
           180,#Baslangic Acisi
           360,#Bitis Acisi
           (0,0,255),#Renk
           2,#Kalinlik
           cv.LINE_8,#Cizgi Tipi
           0#Kayma(Shift)
           )
cv.imshow('image',image)
cv.waitKey(0)

cv.destroyAllWindows()