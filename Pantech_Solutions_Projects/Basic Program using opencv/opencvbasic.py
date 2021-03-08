# -*- coding: utf-8 -*-

import cv2

img=cv2.imread("/Users/sindh/My_projects/Pantech_Solutions_Projects/Basic Program using opencv/opencv.png")
cv2.imshow("OpenCV",img)
cv2.imwrite("OpenCcV.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)
print(img.size)
print(img.dtype)

grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow("Original",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

