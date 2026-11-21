import cv2 as cv
import numpy as np

path= "../images/"
img= cv.imread(path+"logo.png")
cv.namedWindow('img',cv.WINDOW_AUTOSIZE)

h,w,c=img.shape
print(h,w,c)

for row in range(h):
    for col in range(w):
        b,g,r=img[row,col]
        if b==255 and g==255 and r==255:
            b=0
            g=0
            r=0
            img[row,col]=b,g,r

cv.imshow('img',img)
cv.waitKey(0)

cv.destroyAllWindows()