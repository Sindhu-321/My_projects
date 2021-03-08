# -*- coding: utf-8 -*-
import cv2
import time#to give delays
import imutils
#initialise camera
cam=cv2.VideoCapture(0)
#0->webcam
#1->external camera
time.sleep(1)

firstFrame=None
area=500

while True:
    _,img=cam.read()
    text="Normal"
    img=imutils.resize(img,width=300)
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussimg=cv2.GaussianBlur(grayImg,(21,21),0)
    movobjcnt=0
    
    if firstFrame is None:
        firstFrame=gaussimg
        continue
    imgdiff=cv2.absdiff(firstFrame,gaussimg)
    threshImg=cv2.threshold(imgdiff,25,255,cv2.THRESH_BINARY)[1]
    threshImg=cv2.dilate(threshImg,None,iterations=2)
    contours=cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours)
    for c in contours:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Moving Object Detected"
        movobjcnt=movobjcnt+1
        print(text)
    cv2.putText(img,text+" {}".format(movobjcnt),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    
    cv2.imshow("Cameraimg",img)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

