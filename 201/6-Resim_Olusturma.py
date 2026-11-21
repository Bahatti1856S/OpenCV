import cv2 as cv
import numpy as np

path= "../images/"
img= cv.imread(path+"manzara2.jpg")

#RESMIN BELLI KISMINI BOYAMA
m1=np.copy(img)
m2=img
img[100:200,200:300,:]=0
cv.imshow("boyama",m2)
cv.waitKey(0)

#RESIM OLUSTURMA
m3=np.zeros(img.shape,img.dtype)
cv.imshow("m3",m3)
cv.waitKey(0)

m4=np.zeros([300,500],np.uint8)
cv.imshow("m4",m4)
cv.waitKey(0)

m5=np.zeros([500,500],np.uint8)
cv.imshow("m5",m5)
m5[:,:]=127
cv.imshow("m5",m5)
cv.waitKey(0)

cv.destroyAllWindows()