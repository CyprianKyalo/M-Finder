import numpy as np
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten,MaxPooling2D
from tensorflow.keras.layers import Lambda, Subtract
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.regularizers import l2
from tensorflow.keras import backend as K
from tensorflow.keras.optimizers import SGD,Adam
from tensorflow.keras.losses import binary_crossentropy
from loss import L1Dist
import tensorflow as tf

input_shape = (100, 100, 3)
left_input = Input(input_shape, name="Captured Image")
right_input = Input(input_shape, name="Comparison Image")

#build convnet to use in each siamese 'leg'
convnet = Sequential()
convnet.add(Conv2D(64,(10,10),activation='relu',input_shape=input_shape,kernel_regularizer=l2(2e-4)))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(128,(7,7),activation='relu',
                  kernel_regularizer=l2(2e-4)))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(128,(4,4),activation='relu',kernel_regularizer=l2(2e-4)))
convnet.add(MaxPooling2D())
convnet.add(Conv2D(256,(4,4),activation='relu',kernel_regularizer=l2(2e-4)))
convnet.add(Flatten())
convnet.add(Dense(4096,activation="sigmoid",kernel_regularizer=l2(1e-3)))

#encode each of the two inputs into a vector with the convnet
encoded_l = convnet(left_input)
encoded_r = convnet(right_input)

l1 = L1Dist()
distances = l1.call(encoded_l, encoded_r)
prediction = Dense(1,activation='sigmoid', name="Dense")(distances)
SiameseNet = Model(inputs=[left_input,right_input],outputs=prediction, name="Siamese Network")

optimizer = Adam(0.00006)
#//TODO: get layerwise learning rates and momentum annealing scheme described in paperworking
SiameseNet.compile(loss="binary_crossentropy",optimizer=optimizer)

model = SiameseNet
model.summary()

# tf.keras.utils.plot_model(
#     model,
#     to_file="model.png",
#     show_shapes=True,
#     show_layer_names=True,
#     rankdir="TB",
#     expand_nested=True,
#     dpi=96,
# )