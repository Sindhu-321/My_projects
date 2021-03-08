from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
json_file=open("model.json","r")
loaded_model_json=json_file.read()
json_file.close()

model=model_from_json(loaded_model_json)
model.load_weights("model.h5")

import cv2
import imutils
from time import sleep
import urllib

classes=['NONE','ONE','TWO','THREE','FOUR','FIVE']

cam=cv2.VideoCapture(0)

while True:
    _,img=cam.read()

    img = cv2.imdecode(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res=model.predict(gray)
    pred = np.where(res[0] == 1)
    if(len(pred)==0):
        cv2.putText(img,"Not identified",(10,10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        print("Not identified")
    else:
        cv2.putText(img, classes[pred[0][0]], (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print(classes[pred[0][0]])
    cv2.imshow("Gesture",img)
    key=cv2.waitKey(10)
    if key==27:
        break

cam.release()
cv2.destroyAllWindows()

