import io
from itertools import count
import os
import stat
from urllib.request import urlopen
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

import pandas as pd


def getData(dirname="Images", img_shape=(100, 100)):
    # data = pd.read_csv(url,sep="\t",skiprows=2,header=None,names=['Name','imagenum','url','rect','md5'])
    # print(data.shape)
    # totalrows=data.shape[0]
    # total_personalities = data.Name.nunique()
    current = 0
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    j = 0
    for i in range(data.shape[0]):
        if not os.path.exists(os.path.join(dirname, data.iloc[i].Name)):
            os.mkdir(os.path.join(dirname, data.iloc[i].Name))
            current += 1
            print("{} : {}/{} {:.2f}% done".format(dirname,
                  current, total_personalities, i*100/totalrows))
            j = 0
        try:
            resp = urlopen(data.iloc[i].url, timeout=1)
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.COLOR_BGR2GRAY)
            p1, p2, p3, p4 = tuple(map(int, data.iloc[i].rect.split(',')))
            image = image[p2:p4, p1:p3]
            image = cv2.resize(image, img_shape, interpolation=cv2.INTER_AREA)
            plt.imsave(os.path.join(
                dirname, data.iloc[i].Name, str(j)+'.jpg'), image)
            j += 1
        except:
            pass


def transfer(dirname, img_shape=(100, 100)):
    j = 0

    folders = os.listdir(dirname)

    path = "train"

    if not os.path.exists(path):
        os.mkdir(path, 0o777)

    for folder in folders:
        entries = os.listdir(os.path.join(dirname, folder))

        for entry in entries:
            print(os.path.join(dirname, folder, entry))
            img = open(os.path.join(dirname, folder, entry), 'rb')

            image = np.asarray(bytearray(img.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.COLOR_BGR2GRAY)
            image = cv2.resize(image, img_shape, interpolation=cv2.INTER_AREA)

            img.close()

            if not os.path.exists(os.path.join(path, folder)):
                os.mkdir(os.path.join(path, folder))

           
            plt.imsave(os.path.join(path, folder, entry), image)

            print(image)


if __name__ == '__main__':
    # getData("Images")
    transfer("lfw")
