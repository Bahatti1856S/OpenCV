import cv2 as cv

#HSV (Hue Saturation Value) renk formatı nesne takibini kolaylaştırır.

#RGB renk formati
img=cv.imread("../images/logo.png")
cv.namedWindow('RGB',cv.WINDOW_AUTOSIZE)
cv.imshow('RGB',img)
cv.waitKey(0)

#Gri renk formati
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

#HSV renk formati
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
cv.waitKey(0)

cv.destroyAllWindows()