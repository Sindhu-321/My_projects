# -*- coding: utf-8 -*-
import cv2,numpy,os

haar_file='haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)

dataset="dataset"
print('Training...')

(images,labels,names,id)=([],[],{},0)

for(subdirs,dirs,files) in os.walk(dataset):
    for subdir in dirs:
        names[id]=subdir
        subjectpath=os.path.join(dataset,subdir)
        for filename in os.listdir(subjectpath):
            path=subjectpath+'/'+filename
            label=id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id=id+1
      
(images,labels)=[numpy.array(lis) for lis in [images,labels]]

url='http://192.168.0.176:8000/shot.jpg'
        
(width,height)=(130,100)

#recognition

model=cv2.face.LBPHFaceRecognizer_create()
#model=cv2.face.FisherFaceRecogniser_create()

model.train(images,labels)

#webcam=cv2.VideoCapture(0)

cnt=0

while True:
    #_,im=webcam.read()
    imgpath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(img.path.read()),dtype=np.uint8)
    im=cv2.imdecode(imgNp,-1)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,225,0),2)
        face=gray[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(width,height))
        
        prediction=model.predict(face_resize)
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,255))
        if prediction[1]<800:
            cv2.putText(im,'%s-%.0f' % (names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,255,255),2)
            print(names[prediction[0]])
            cnt=0
        else:
            cnt+=1
            cv2.putText(im,"Unknown",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)
            if(cnt>100):
                print("Unknown person!!")
                cv2,imwrite("unknown.jpg",im)
                cnt=0
    cv2.imshow("face_Recognition",im)
    key=cv2.waitKey(10)
    if key==27:
        break
    
#webcam.release()
cv2.destroyAllWindows()
