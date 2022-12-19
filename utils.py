from model import SiameseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import preprocess_input

import cv2
import numpy as np
import os

# siamese_model.load_weights("./weights/encoder.data-00000-of-00001")
model_path = "./my_encoder"
path1 = "./Extracted_Faces/Fabian_Kyalo/Fabian_Kyalo_0001.jpg"
path2 = "./Extracted_Faces/Suzanne_Gaudet/Suzanne_Gaudet_001.jpg"
# ROOT = "./Extracted_Faces"
images_path = "./static/uploads"

cascade_path = "./haarcascade_frontalface_default.xml"
cascade_model = cv2.CascadeClassifier(cascade_path)

def extract_face(image):
    """ Gets the face from the image passed using Haar-Cascade """
    
    global cascade_model
    # ROOT = "./"
    # path = os.path.join(ROOT, image)

    # image = cv2.imread(image)
    
    # Getting co-ordinates of the face
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # faces = cascade_model.detectMultiScale(
    #     gray,
    #     scaleFactor=1.4,
    #     minNeighbors=5,
    #     minSize=(32, 32)
    # )
    faces = cascade_model.detectMultiScale(gray, 1.1, 4)
    
    # Extracts the face from the image and returns it
    if len(faces)>0:
        x,y,w,h = faces[-1]
        image = image[y:y+h,x:x+w]
        return image
    return None

def read_image(path):
    # path = os.path.join(ROOT, index[0], index[1])
    image = cv2.imread(path)
    # 
    # if image is None:
    #     print("No image found")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # image = extract_face(image)
    image = cv2.resize(image, (128, 128))

    
    # cv2.imwrite("Read_image.jpg", image)
    # if image is None:
    #     print("Nothing")
    # print("image")
    return image
    
def classify(model, face_list1, face_list2, threshold=1.35):
    # Getting the encodings for the passed faces
    tensor1 = model.predict(face_list1)
    tensor2 = model.predict(face_list2)
    
    distance = np.sum(np.square(tensor1-tensor2), axis=-1)
    # print("The distance is ", distance)
    prediction = np.where(distance<=threshold, 0, 1)

    return distance, prediction

def verify_predict(model):
    results = []
    captured_image = "my_taken_image.jpg"
    captured_image = preprocess_input(read_image(captured_image))

    for img in os.listdir(images_path):
        print("Now at image ", img)
        validation_image = preprocess_input(read_image(os.path.join(images_path, img)))

        dist, pred = classify(model, np.expand_dims(captured_image, axis=0), np.expand_dims(validation_image, axis=0))

        results.append(dist)

    index = np.argmin(results)

    if index and results[index] < 1.5:
        return index
    return None
    

# model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})

# print("The predicted output is ", classify_images(model, read_image(path1), read_image(path2)))
# print("The output is ", classify(model, np.expand_dims(preprocess_input(read_image(path1)), axis=0), np.expand_dims(preprocess_input(read_image(path2)), axis=0)))
# model.summary()