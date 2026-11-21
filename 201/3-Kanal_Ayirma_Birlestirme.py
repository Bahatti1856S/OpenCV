import cv2 as cv
import numpy as np

path= "../images/"
src= cv.imread(path+"logo.png")

#mavi kanal 0
mv= cv.split(src)
mv[0][:,:] = 0
dst1=cv.merge(mv)
cv.imshow("src",dst1)
cv.waitKey(0)

#yeşil kanal 0
mv= cv.split(src)
mv[1][:,:] = 0
dst2=cv.merge(mv)
cv.imshow("src",dst2)
cv.waitKey(0)

#kırmızı kanal 0
mv= cv.split(src)
mv[2][:,:] = 0
dst3=cv.merge(mv)
cv.imshow("src",dst3)
cv.waitKey(0)

cv.destroyAllWindows()