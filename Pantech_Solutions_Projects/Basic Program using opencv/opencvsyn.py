# -*- coding: utf-8 -*-

import cv2
import imutils

img=cv2.imread("opencv.png")
#resizing
resizeImg=imutils.resize(img,width=400)
cv2.imwrite("opencvrsiz.png",resizeImg)
#gaussian blur blurs the image
gaussianBlurImg=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("gausianblur.png",gaussianBlurImg)

#Thresholding
#image needs to be grayscale
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresimg=cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("Threshold.png",thresimg)
#drawing rectangle

