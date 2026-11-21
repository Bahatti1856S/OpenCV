import cv2 as cv

path= "../images/"
img= cv.imread(path+"manzara2.jpg")
cv.namedWindow("test",cv.WINDOW_AUTOSIZE)
cv.imshow("test",img)
cv.waitKey(0)


#COLORMAP RENK IYILESTIRME
dst=cv.applyColorMap(img,cv.COLORMAP_SUMMER)
cv.imshow("renk degisim",dst)
cv.waitKey(0)

#cvtColor GRIYE CEVIRME
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gri",gray)
cv.waitKey(0)

#imwrite YAPILAN RESMI KADETME
cv.imwrite(path+"gri_hal.jpg",gray)

cv.destroyAllWindows()