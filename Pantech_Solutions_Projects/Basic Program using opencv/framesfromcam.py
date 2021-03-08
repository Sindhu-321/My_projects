# -*- coding: utf-8 -*-

import cv2
import time#to give delays
#initialise camera
cam=cv2.VideoCapture(0)
#0->webcam
#1->external camera
time.sleep(1)

while True:
    _,img=cam.read()
    cv2.imshow("Cameraimg",img)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()