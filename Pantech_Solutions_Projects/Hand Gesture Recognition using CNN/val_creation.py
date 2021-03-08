import os
import shutil

i=0

src="/Users/sindh/My_projects/Pantech_Solutions_Projects/Hand Gesture Recognition using CNN/HandGestureDataset/train"
dest="/Users/sindh/My_projects/Pantech_Solutions_Projects/Hand Gesture Recognition using CNN/HandGestureDataset/val"

dir="FIVE"

while i<500:
    sor=src+"/"+dir+"/"+dir+"_"+str(i)+".png"
    sr=r'{}'.format(sor)
    des=dest+"/"+dir+"/"+dir+"_"+str(i)+'.png'
    de=r'{}'.format(des)
    shutil.move(sr,de)
    i=i+1



