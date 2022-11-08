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

def read_image(path):
    # path = os.path.join(ROOT, index[0], index[1])
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
    
def classify(model, face_list1, face_list2, threshold=1.3):
    # Getting the encodings for the passed faces
    tensor1 = model.predict(face_list1)
    tensor2 = model.predict(face_list2)
    
    distance = np.sum(np.square(tensor1-tensor2), axis=-1)
    # print("The distance is ", distance)
    prediction = np.where(distance<=threshold, 0, 1)

    return distance, prediction

def verify_predict(model):
    results = []
    captured_image = os.path.join('static', 'imgs', 'input_image.jpg')
    captured_image = preprocess_input(read_image(captured_image))

    for img in os.listdir(images_path):
        print("Now at image ", img)
        validation_image = preprocess_input(read_image(img))

        dist, pred = classify(model, np.expand_dims(captured_image, axis=0), np.expand_dims(validation_image, axis=0))

        results.append(dist)

    index = np.argmin(results)

    if index:
        return index
    return 0
    

model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})

# print("The predicted output is ", classify_images(model, read_image(path1), read_image(path2)))
# print("The output is ", classify(model, np.expand_dims(preprocess_input(read_image(path1)), axis=0), np.expand_dims(preprocess_input(read_image(path2)), axis=0)))
# model.summary()