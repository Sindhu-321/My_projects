# -*- coding: utf-8 -*-
import imutils
import cv2

#color hsv values
redLower=(97,68,62)
redUpper=(176,255,255)


camera=cv2.VideoCapture(0)

while True:
    #read frame
    (grabbed,frame)=camera.read()
    #resize frame
    frame=imutils.resize(frame,width=600)
    #smoothening by gaussian blur
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    #hsv form
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    #mask background-masked for only red
    mask=cv2.inRange(hsv,redLower,redUpper)
    #make thin and remove noise
    mask=cv2.erode(mask,None,iterations=2)
    #contours
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    #center initialise
    center=None
    #enter only if there are contours ie traces of red
    if len(cnts)>0:
        #getting maximum contour area
        c=max(cnts,key=cv2.contourArea)
        #drawing mim encosure circle
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        #calculating moments
        M=cv2.moments(c)
        
        #only if rad>10 draw circle
        if radius>10:
            #calculating center
            center=(int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            #draw circle
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            #plot center
            cv2.circle(frame,center,5,(0,0,255),-1)
            #stop if too far
            if radius>250:
                print("stop")
            else:
                if(center[0]<150):
                    print("left")
                elif(center[0]>450):
                    print("right")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):#on pressing q exit
        break
camera.release()
cv2.destroyAllWindows()

    
            
            