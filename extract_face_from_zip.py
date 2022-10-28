import os
import cv2
import shutil

ROOT = "../face-recognition-using-siamese-network/dataset/fc"
cascade_path = "./haarcascade_frontalface_default.xml"

cascade_model = cv2.CascadeClassifier(cascade_path)
folders = sorted(os.listdir(ROOT))
extracted = "../face-recognition-using-siamese-network/dataset/fb"

def extract_face(image):
    """ Gets the face from the image passed using Haar-Cascade """
    
    global cascade_model
    
    # Getting co-ordinates of the face
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade_model.detectMultiScale(
        gray,
        scaleFactor=1.4,
        minNeighbors=5,
        minSize=(32, 32)
    )
    
    # Extracts the face from the image and returns it
    if len(faces)>0:
        x,y,w,h = faces[-1]
        image = image[y:y+h,x:x+w]
        return image
    return None

def save_image(path, image):
    """ Saves the Image to the path specified """
    
    # Creating directory
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    # Saving the image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (128, 128))
    cv2.imwrite(path, image)

for folder in folders:
    # Gets list of all files in the folder
    files = os.listdir(os.path.join(ROOT, folder))
    
    num_files = 0
    for file in files:
        # Reads the image and extracts face
        path = os.path.join(ROOT, folder, file)
        image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
        face = extract_face(image)
        
        if not os.path.exists(extracted):
            os.mkdir(extracted)

        # Saves the face
        if not face is None:
            save_path = os.path.join(extracted, folder, folder + "_000" + f"{num_files}.jpg")
            save_image(save_path, face)
            num_files += 1

    print("Now at ", folder)

print("---------------Finished Extracting Faces----------")

# for folder in os.listdir("Extracted Faces"):
#     path = os.path.join("Extracted Faces", folder)
#     files = os.listdir(path)
#     if len(files)<2:
#         shutil.rmtree(path)

print("---------Extraction Complete-------------")