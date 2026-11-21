import cv2 as cv
import numpy as np

path= "../images/"
src1=cv.imread(path+"spiderman1.png")
src2=cv.imread(path+"spiderman2.png")

#resize RESIM BOYUTLARINI ESITLEME
src2 = cv.resize(src2, (src1.shape[1], src1.shape[0]))

#add TOPLAMA
add_result=np.zeros(src1.shape, src1.dtype)
cv.add(src1,src2,add_result)
cv.imshow("add",add_result)
cv.waitKey(0)

#subtract CIKARMA
subtract_result=np.zeros(src1.shape, src1.dtype)
cv.subtract(src1,src2,subtract_result)
cv.imshow("subtract",subtract_result)
cv.waitKey(0)

#multiply CARPMA
multiply_result=np.zeros(src1.shape, src1.dtype)
cv.multiply(src1,src2,multiply_result)
cv.imshow("multiply",multiply_result)
cv.waitKey(0)

#divide BOLME
divide_result=np.zeros(src1.shape, src1.dtype)
cv.divide(src1,src2,divide_result)
cv.imshow("divide",divide_result)
cv.waitKey(0)

cv.destroyAllWindows()