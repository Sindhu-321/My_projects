# -*- coding: utf-8 -*-

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import winsound
import speech_recognition as sr
import pyttsx3


# Initializing required functionalities like speech recognizer and audio to text converter.
listener = sr.Recognizer()
engine = pyttsx3.init()


#Defining a function which plays audio message for text that is passed to it
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Defining a function to detect face and predict mask
def detect_and_predict_mask(frame, faceNet, maskNet):
   
# Accept the dimensions of the frame and then construct a blob from it
#Now frame.shape is array 
#The shape of an image is accessed by img.shape. It returns a tuple of the number of rows, columns, and channels (if the image is color):
#>>> print( img.shape )
#(342, 548, 3)
#To print elements from beginning to a range use [:Index]

	(h, w) = frame.shape[:2]


	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections

	faceNet.setInput(blob)
	detections = faceNet.forward()
	print(detections.shape)

	# initialize our list of faces and the locations and the list of predictions from our face mask network

	faces = []
	locs = []
	preds = []

	# loop the detections

	for i in range(0, detections.shape[2]):
		# extract the probability associated with the detection

		probability = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the Probability is greater than the minimum Probability

		if probability > 0.5:
			# compute the (x, y)-coordinates of the bounding box for the object

			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of  the frame

			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# convert it from BGR to RGB and resize it to 224x224

			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# add the face and bounding boxes to their respective
			# lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# only make a predictions if at least one face was detected

	if len(faces) > 0:
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

	# return a 2-tuple of the face locations and their corresponding locations

	return (locs, preds)

# load our serialized face detector model from disk. These is giving input to deep learning neural networks so that it can learn and detect if mask is worn by a person or not
prototxtPath = r"deploy.prototxt"
weightsPath = r"res10_300x300_ssd_iter_140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk 

maskNet = load_model("mask_detector.model")

# initialize the video stream
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# detect the frame and check they wear mask or not

	(locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

	# loop over the detected face locations and their corresponding locations

	for (box, pred) in zip(locs, preds):
		# unpack

		(startX, startY, endX, endY) = box
		(mask, withoutMask) = pred


		#Based on mask or no mask creating label and colouring it
		label = "Mask" if mask > withoutMask else "No Mask"
		color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

#Based on mask or no mask, sending audio clip

		if label == "No Mask":
			winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
			talk("Please wear mask")


		# include the probability in the label

		label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

		# display the label and bounding box rectangle on the output
		# frame
		cv2.putText(frame, label, (startX, startY - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
		cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

	# show the output frame

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` or 'Q' key was pressed, break from the loop
	if key == ord("q") or key == ord("Q"):
		break

cv2.destroyAllWindows()
vs.stop()
