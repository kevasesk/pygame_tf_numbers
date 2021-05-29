# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import hickle as hkl

digits_mnist = keras.datasets.mnist  # load dataset
(train_images, train_labels), (test_images, test_labels) = digits_mnist.load_data(path="mnist.npz")  # split into tetsing and training

data = {'train_images': train_images, 'train_labels': train_labels,'test_images': test_images,'test_labels':test_labels}
hkl.dump(data, 'data.hkl')

class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

train_images = train_images / 255.0  #format data for 0-1
test_images = test_images / 255.0 #format data for 0-1


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # input layer (1)
    keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
    keras.layers.Dense(10, activation='softmax') # output layer (3)
]) #network configuration

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=1)
print('Test accuracy:', test_acc)
predictions = model.predict(test_images)
model.save('keras_memory')
