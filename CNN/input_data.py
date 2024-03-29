import os

import numpy as np

from tensorflow.python.keras._impl.keras import backend as K
from tensorflow.python.keras._impl.keras.datasets.cifar import load_batch
from tensorflow.python.keras._impl.keras.utils.data_utils import get_file


def load_data():
    dirname = 'data/'
    path = dirname

    num_train_samples = 50000

    x_train = np.zeros((num_train_samples, 3, 32, 32), dtype='uint8')
    y_train = np.zeros((num_train_samples,), dtype='uint8')

    for i in range(1, 6):
        fpath = os.path.join(path, 'data_batch_' + str(i))
        data, labels = load_batch(fpath)
        x_train[(i - 1) * 10000:i * 10000, :, :, :] = data
        y_train[(i - 1) * 10000:i * 10000] = labels

    fpath = os.path.join(path, 'test_batch')
    x_test, y_test = load_batch(fpath)

    y_train = np.reshape(y_train, (len(y_train), 1))
    y_test = np.reshape(y_test, (len(y_test), 1))

    if K.image_data_format() == 'channels_last':
        x_train = x_train.transpose(0, 2, 3, 1)
        x_test = x_test.transpose(0, 2, 3, 1)

    x_test = 1.0 - x_test / 255.0
    x_train = 1.0 - x_train / 255.0

    return (x_train, y_train), (x_test, y_test) - x_train / 255.0

    return (x_train, y_train), (x_test, y_test)
