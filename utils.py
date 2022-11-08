from model import SiameseModel, siamese_model
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import preprocess_input

import cv2
import numpy as np
import os

# siamese_model.load_weights("./weights/encoder.data-00000-of-00001")
model_path = "./my_encoder"
path1 = "./Extracted_Faces/Fabian_Kyalo/Fabian_Kyalo_0001.jpg"
path2 = "./Extracted_Faces/Fabian_Kyalo/Fabian_Kyalo_0000.jpg"
# ROOT = "./Extracted_Faces"

def read_image(path):
    # path = os.path.join(ROOT, index[0], index[1])
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
    
def verify_predict(encoder, face_list1, face_list2, threshold=1.3):
    # Getting the encodings for the passed faces
    tensor1 = encoder.predict(face_list1)
    tensor2 = encoder.predict(face_list2)
    
    distance = np.sum(np.square(tensor1-tensor2), axis=-1)
    prediction = np.where(distance<=threshold, 0, 1)

    return prediction

model = load_model(model_path, custom_objects={"SiameseModel": SiameseModel})

# print("The predicted output is ", classify_images(model, read_image(path1), read_image(path2)))
print("The output is ", verify_predict(model, np.expand_dims(preprocess_input(read_image(path1)), axis=0), np.expand_dims(preprocess_input(read_image(path2)), axis=0)))
# model.summary()