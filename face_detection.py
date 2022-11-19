# import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # Read the input image
# #img = cv2.imread('test.png')
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     _, img = cap.read()

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 6)

#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

#     # Display the output
#     cv2.imshow('img', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
from model import SiameseModel
from utils import verify_predict
from tensorflow.keras.models import load_model

images_path = "./static/uploads"
model_path = "./my_encoder"
# model = 1
model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})


import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        # for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

        cv2.imwrite("my_image.jpg", img)
        print("The results is ", verify_predict(model))


            # break

    # Display the output
    cv2.imshow('img', img)


    # if cv2.waitKey(1) & 0xFF == ord('v'):
    #     print("Saving Image") 
    #     cv2.imwrite("my_image.jpg", img)
    #     # print("The index is ", os.listdir(images_path)[verify_predict(model)])
    #     print("The results is ", verify_predict(model))

    # cv2.imshow("Faces found", faces)

    # for i in range(0, len(faces)):
    #     (x, y, w, h) = faces[i]
    #     cv2.imwrite("Image number {}.jpg".format(i), gray[y:y+w, x:x+h])


	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

# program to capture single image from webcam in python

# importing OpenCV library
from cv2 import *

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
# cam_port = 0
# cam = cv2.VideoCapture(cam_port)

# # reading the input using the camera
# result, image = cam.read()

# # If image will detected without any error,
# # show result
# if result:

# 	# showing result, it take frame name and image
# 	# output
# 	cv2.imshow("GeeksForGeeks", image)

# 	# saving image in local storage
# 	cv2.imwrite("GeeksForGeeks.png", image)

# 	# If keyboard interrupt occurs, destroy image
# 	# window
# 	cv2.waitKey(0)
# 	cv2.destroyWindow("GeeksForGeeks")

# # If captured image is corrupted, moving to else part
# else:
# 	print("No image detected. Please! try again")

