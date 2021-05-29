# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import hickle as hkl

#digits_mnist = keras.datasets.mnist  # load dataset
#(train_images, train_labels), (test_images, test_labels) = digits_mnist.load_data(path="mnist.npz")  # split into tetsing and training
#train_images = train_images / 255.0  #format data for 0-1
#test_images = test_images / 255.0 #format data for 0-1



def predict(input):
    input = tf.reshape(input, [28, 28])
    input = input.numpy()
    inputNetwork = input / 255.0
    inputNetwork = np.expand_dims(inputNetwork, 0)

    data = hkl.load('network/data.hkl')
    # train_images = data['train_images']
    # train_labels = data['train_labels']
    # test_images = data['test_images']
    # test_labels = data['test_labels']

    model = keras.models.load_model('network/keras_memory')
    predictions = model.predict([inputNetwork])

    print(predictions)
    print(np.argmax(predictions))
    return predictions

    #test_index = 65
    # print(np.argmax(predictions[test_index]))
    # print(test_labels[test_index])

    # plt.figure()
    # plt.imshow(input)
    # plt.colorbar()
    # plt.grid(False)
    # plt.show()

