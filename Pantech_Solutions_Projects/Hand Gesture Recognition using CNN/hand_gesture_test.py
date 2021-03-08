from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
json_file=open("model.json","r")
loaded_model_json=json_file.read()
json_file.close()

model=model_from_json(loaded_model_json)
model.load_weights("model.h5")

def classify(img_file):
    img_name=img_file
    test_image = image.load_img(img_name, target_size=(256, 256), color_mode="grayscale")

    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)


    return result


import os
dir="./HandGestureDataset/test"

files=[]

for r,d,f in os.walk(dir):
    for file in f:
        if '.png' in file:

            files.append(os.path.join(r,file))
import random
classes=['NONE','ONE','TWO','THREE','FOUR','FIVE']
i=1
while i<=10:
    num=random.randint(0,len(files))
    res=classify(files[num]).astype(int)
    pred=np.where(res[0]==1)
    if(len(pred)!=0):
        print("Predicted="+classes[pred[0][0]]+", Actual= "+files[num])
    i=i+1










