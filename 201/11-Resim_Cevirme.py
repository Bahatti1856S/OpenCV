import cv2 as cv
import numpy as np

path= "../images/"
img= cv.imread(path+"logo.png")

#X Ekseninde Cevirme
dst1=cv.flip(img,0)#0=X
cv.imshow("X Ekseninde Cevirme",dst1)
cv.waitKey(0)

#Y Ekseninde Cevirme
dst2=cv.flip(img,1)#1=Y
cv.imshow("Y Ekseninde Cevirme",dst2)
cv.waitKey(0)

#XY Ekseninde Cevirme
dst3=cv.flip(img,-1)#-1=XY
cv.imshow("XY Ekseninde Cevirme",dst3)
cv.waitKey(0)

cv.destroyAllWindows()