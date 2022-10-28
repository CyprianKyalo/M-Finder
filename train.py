import os
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from model import SiameseNet

def train():
    checkpoint_filepath = 'tmp/checkpoint'

    if not os.path.exists(checkpoint_filepath):
        os.mkdir(checkpoint_filepath)

    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_filepath, save_weights_only=False, monitor='loss', mode='min', save_best_only=True)

    callbacks = [
        EarlyStopping(patience=5),
        model_checkpoint_callback,
    ]

train()