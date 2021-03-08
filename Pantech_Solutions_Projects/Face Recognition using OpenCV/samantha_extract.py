# -*- coding: utf-8 -*-
"""
import cv2
import imutils
import os

dataset="dataset"
name_des="samantha"
name_sou="sam"

algo="haarcascade_frontalface_default.xml"

haar_cascade=cv2.CascadeClassifier(algo)


pathd=os.path.join(dataset,name_des)
paths=os.path.join(dataset,name_sou)
#check availability and create
if not os.path.isdir(pathd):
    os.mkdir(pathd)
if not os.path.isdir(paths):
    os.mkdir(paths)
    
(width,height)=(130,100)

pathss="/Users/sindh/My_projects/Pantech_Solutions_Projects/Face Recognition using OpenCV/dataset/sam"

pathsss=os.fsencode(pathss)
    
count=1    
for file in os.listdir(pathsss):
    filee=str(file)
    img=cv2.imread(os.path.join(pathss,filee))
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Face Detected"
        #crop face
        faceOnly=grayimg[y:y+h,x:x+w]
        resizeimg=cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg"%(pathd,count),resizeimg)
        count+=1
"""       
        
import cv2
import os

dataset="dataset"
name_des="samantha"
name_sou="sam"

algo="haarcascade_frontalface_default.xml"

haar_cascade=cv2.CascadeClassifier(algo)

pathd="/Users/sindh/My_projects/Pantech_Solutions_Projects/Face Recognition using OpenCV/dataset/rakul"


(width,height)=(130,100)

def load_images_from_folder(folder):
    count=1
    images=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        
        
        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        
        
        
        
        
        
        resizeimg=cv2.resize(grayimg,(width,height))
        cv2.imwrite("%s/%s.jpg"%(pathd,count),resizeimg)
        count+=1
            
    

folder="/Users/sindh/My_projects/Pantech_Solutions_Projects/Face Recognition using OpenCV/dataset/rak"

imges=load_images_from_folder(folder)
    