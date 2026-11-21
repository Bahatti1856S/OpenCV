import cv2 as cv
import numpy as np
from numpy.ma.extras import column_stack

img=cv.imread("../images/miuul.png")

rows=img.shape[0]
cols=img.shape[1]

M=np.float32([[1,0,300],[0,1,90]])

shifted=cv.warpAffine(img,M,(cols,rows))
cv.imshow("Shifted",shifted)
cv.waitKey(0)

M=cv.getRotationMatrix2D((cols/2,rows/2),90,1)
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow("Rotation",dst)
cv.waitKey(0)

res=cv.resize(img,None,fx=0.2,fy=0.2,interpolation=cv.INTER_CUBIC)
cv.imshow("Resize",res)
cv.waitKey(0)

cv.destroyAllWindows()