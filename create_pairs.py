from itertools import combinations
import os
import shutil
import cv2

root = "lfw"
extracted_path = "Extracted Faces"
cascade_path = "./haarcascade_frontalface_default.xml"

cascade_model = cv2.CascadeClassifier(cascade_path)

def create_pairs():
    num_folders = len(os.listdir(root))
    folders = os.listdir(root)

    similar_data = []
    dissimilar_data = []
    i = 0

    # for i in range(num_folders - 1):
    for folder in folders:
        # files = os.listdir(os.path.join(root, root[i]))
        files = os.listdir(os.path.join(root, folder))

        # Creating similar dataset
        for pair in list(combinations(files, 2)):
            similar_data.append(((folder, pair[0]), (folder, pair[1]), 1))
        
        # Creating different dataset
        for j in range(i, min(i+40, num_folders)):
            dissimilar_data.append(((folder, "0.jpg"), (str(j), "0.jpg"), 0))

        i+=1

    return similar_data+dissimilar_data

# data = create_pairs()
# print(data)

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
    # Creating directory
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (128, 128))
    cv2.imwrite(path, image)

def save_extracted_faces(root):
    folders = os.listdir(root)

    if not os.path.exists(extracted_path):
        os.mkdir(extracted_path)

    for folder in folders:
        num_files = 0
        files = os.listdir(os.path.join(root, folder))

        # print(folder)
        if len(files) < 2:
            continue
        
        for file in files:
            # print(file)
            path = os.path.join(root, folder, file)
            # image = cv2.imread(file)
            image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

            # print(image)
            # break
            face = extract_face(image)

            if not face is None:
                save_path= os.path.join(extracted_path, folder, folder + "_00" + f"{num_files}.jpg")
                save_image(save_path, face)
                num_files += 1

        print("Now at ", folder)

    print("-----------------Finished Extracting Faces---------------------")    
        
def remove_less_than_two_images(root):
    folders = os.listdir(root)
    for folder in folders:
        path = os.path.join(root, folder)
        files = os.listdir(path)
        if len(files) < 2:
            shutil.rmtree(path)
            print("Removing ", folder)
        
        print("Now at ", folder)

    
    print("----------------Extraction Complete----------------")

# save_extracted_faces(root)
# remove_less_than_two_images(extracted_path)