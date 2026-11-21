import cv2 as cv
import numpy as np

capture=cv.VideoCapture('../videos/walking1.mp4')
height=capture.get(cv.CAP_PROP_FRAME_HEIGHT)#Videonun Yukekligi
width=capture.get(cv.CAP_PROP_FRAME_WIDTH)#Videonun Genisili
count=capture.get(cv.CAP_PROP_FRAME_COUNT)#Videonun Frame Sayisi
fps=capture.get(cv.CAP_PROP_FPS)#Videonun FPS'i
print(height,width,count,fps)

#Videoyu .avi olarak kaydetme
out=cv.VideoWriter('../videos/walking1.avi',
                   cv.VideoWriter_fourcc('D','I','V','X'),
                   np.int8(fps),
                   (np.int16(width),np.int16(height)),True)

while True:
    #goruntuyu al
    ret,frame=capture.read()
    if ret==True:#goruntu basariyla alındıysa gir
        cv.imshow('frame',frame)#videoyu oynat
        out.write(frame)
        key=cv.waitKey(15)#15sn sonra cik
        if key==27:#ESC basilirsa kapat
            break
    else:
        break

capture.release()#hafızadaki videoyu kapat
out.release()#hafızadaki .avi videosunu kapat

