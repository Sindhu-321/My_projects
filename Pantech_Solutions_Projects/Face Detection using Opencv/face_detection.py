# -*- coding: utf-8 -*-

import cv2
import os

dataset="dataset"
name="sindhu"


path=os.path.join(dataset,name)
#check availability and create
if not os.path.isdir(path):
    os.mkdir(path)
    
(width,height)=(130,100)




algo="haarcascade_frontalface_default.xml"

haar_cascade=cv2.CascadeClassifier(algo)

cam=cv2.VideoCapture(0)

count=1
i=1



while i<21:
    print(count)
    
    _,img=cam.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.3,4)
    text="No Face Detected"
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Face Detected"
        #crop face
        faceOnly=grayimg[y:y+h,x:x+w]
        resizeimg=cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeimg)
        count+=1
        i+=1
        
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
    cv2.imshow("Face_Detection",img)
    
    key=cv2.waitKey(10)
    if key==27:
        break
print("Images captured!")
cam.release()
cv2.destroyAllWindows()




