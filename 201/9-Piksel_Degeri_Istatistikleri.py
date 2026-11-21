import cv2 as cv
import numpy as np

path= "../images/"
src= cv.imread(path+"logo.png",cv.IMREAD_GRAYSCALE)

min_value,max_value,min_loc,max_loc= cv.minMaxLoc(src)
print('min_value:',min_value)
print('max_value:',max_value)
print('min_loc:',min_loc)
print('max_loc:',max_loc)

means,stddev= cv.meanStdDev(src)
print('ortalama(means)',means,'standart sapma(stddev)',stddev)

#renk degeri ortalamanın altıdna olanları beyaz ustunde olanları sıyah yaptık
src[np.where(src<means)]=0
src[np.where(src>means)]=255
#boylece resmi sadece siyah beyaza cevirdik gri tonlardan kurtulduk

cv.imshow("src",src)
cv.waitKey(0)

cv.destroyAllWindows()