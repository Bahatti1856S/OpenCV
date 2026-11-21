import cv2 as cv
import numpy as np

path= "../images/"
img1= cv.imread(path+"spiderman1.png")
img2= cv.imread(path+"spiderman2.png")
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))#resimlerin boyu eşitlendi

horizontal=np.hstack((img1,img2))# 2 Resmi yatay sekilde yan yana koy
cv.imshow('horizontal',horizontal)
cv.waitKey(0)

cv.destroyAllWindows()