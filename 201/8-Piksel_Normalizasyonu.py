import cv2 as cv
import numpy as np

path= "../images/"
src= cv.imread(path+"logo.png")

gray= cv.cvtColor(src,cv.COLOR_BGR2GRAY)
gray= np.float32(gray)#standarlaştırma işlemlerinde intager yetmedigi için floata cevirdik

#NORM_MINMAX
dst=np.zeros(gray.shape,np.float32)
cv.normalize(gray,dst,1.0,0,cv.NORM_MINMAX)
#floatta 0 ın altındaki degerleri inte cevirince 0'a yuvarlayıp resmi tamamen siyah yapmasın diye 255 ile carpıyoruz
cv.imshow("NORM_MINMAX",np.uint8(dst*255))
cv.waitKey(0)
#gorunurde hicbir degisiklik yok ama artık resim 0-255 aralıgında degil 0-1 aralıgındaki sayılarla olusuyor

#Diger normalizasyon yontemleri(bunlara cogunlukla gerek olmuyo genelde MINMAX yonremı kullanılır)
#NORM_INF
dst=np.zeros(gray.shape,np.float32)
cv.normalize(gray,dst,1.0,0,cv.NORM_INF)
cv.imshow("NORM_INF",np.uint8(dst*255))
cv.waitKey(0)

#NORM_L1
dst=np.zeros(gray.shape,np.float32)
cv.normalize(gray,dst,1.0,0,cv.NORM_L1)
cv.imshow("NORM_L1",np.uint8(dst*10000000))
cv.waitKey(0)

#NORM_L2
dst=np.zeros(gray.shape,np.float32)
cv.normalize(gray,dst,1.0,0,cv.NORM_L2)
cv.imshow("NORM_L2",np.uint8(dst*10000))
cv.waitKey(0)

cv.destroyAllWindows()