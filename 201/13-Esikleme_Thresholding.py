import numpy as np
import cv2 as cv

path="../Images/"
img=cv.imread(path+"spiderman1.png")

T=127

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

for i in range(5):
    ret,binary=cv.threshold(gray,T,255,i)
    cv.imshow("binary "+str(i),binary)

cv.waitKey(0)
cv.destroyAllWindows()