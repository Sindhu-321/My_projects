# -*- coding: utf-8 -*-
import urllib.request
import cv2
import numpy as np
import imutils

url='http://192.168.0.176:8000/shot.jpg'

while True:
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(img.path.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img.resize(img,width=450)
    cv2.imshow("Camerafeed",img)
    if ord('q')==cv2.waitKey(1):
        exit(0)
    
