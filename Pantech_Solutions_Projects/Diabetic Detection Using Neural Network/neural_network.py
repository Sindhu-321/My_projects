# -*- coding: utf-8 -*-

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

dataset=loadtxt('pima-indians-diabetes.csv',delimiter=',')
x=dataset[:,0:8]
y=dataset[:,8]

model=Sequential()

model.add(Dense(12,input_dim=8,activation='relu'))

model.add(Dense(8,activation='relu'))

model.add(Dense(1,activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2)


model.fit(x_train,y_train,epochs=2000,batch_size=10)

_,accuracy=model.evaluate(x_test,y_test)

predictions=model.predict_classes(x_test)


print("Accuracy = {}".format((accuracy)*100))

model_json=model.to_json()
with open("model.json","w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")

