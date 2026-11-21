import cv2 as cv
import numpy as np

path= "../images/"

#PYTHONDA RENK KODLAR BGR DİYE GİDER!!!!
#0=B
#1=G
#2=R

#resim1
src1=np.zeros((400,400,3),np.uint8)
src1[100:200,100:200,1]=255
src1[100:200,100:200,2]=255
cv.imshow("src1",src1)
cv.waitKey(0)

#resim2
src2 = np.zeros((400,400,3),np.uint8)
src2[150:250,150:250,2]=255
cv.imshow("src2",src2)
cv.waitKey(0)


#and
dst1=cv.bitwise_and(src1,src2)
cv.imshow("and",dst1)
cv.waitKey(0)

#or
dst2=cv.bitwise_or(src2,src1)
cv.imshow("or",dst2)
cv.waitKey(0)

#xor
dst3=cv.bitwise_xor(src2,src1)
cv.imshow("xor",dst3)
cv.waitKey(0)

#pikesl degerlerini tersine cevir
src=cv.imread(path+"logo.png")
cv.namedWindow("src",cv.WINDOW_AUTOSIZE)
cv.imshow("src",src)
cv.waitKey(0)

dst=cv.bitwise_not(src)
cv.imshow("dst",dst)
cv.waitKey(0)

cv.destroyAllWindows()