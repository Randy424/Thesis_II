from __future__ import print_function
import os
import sys
sys.path.append('../')
import glob
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import pandas as pd
import keras
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, Conv1D, Reshape
from keras.optimizers import RMSprop, Adam
from load_dataset import load_data, load_all_data, load_data_custom_path_single
from display_data import display_data
from sklearn.model_selection import train_test_split
import tensorflow as tf
from graph import Graph
from scipy import signal

config = tf.ConfigProto(intra_op_parallelism_threads=0, 
                        inter_op_parallelism_threads=0, 
                        allow_soft_placement=True)

session = tf.Session(config=config)

batch_size = 4
num_classes = 2
epochs = 3

#array of data paths
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../../data/jump_data_PL/*.nc') 
file_array = glob.glob(my_file)
atmospheric_pressure = []
pressure_flags = []

#loading data
for file in file_array:
    atmospheric_pressure_single, flags_single, index = load_data_custom_path_single('PL_WSPD',file)
    pressure_flags_single = [value for sublist in flags_single for counter,value in 
    enumerate(sublist) if counter == index]
    atmospheric_pressure.extend(atmospheric_pressure_single)
    pressure_flags.extend(pressure_flags_single)

x = list(range(0, len(atmospheric_pressure)))
x = [float(i) for i in x]
#print (y)

x = np.array(x)

y = atmospheric_pressure
y = np.array(y)

mean = y.mean()
std = y.std()
cv = std/mean
vary = y.var()
print("mean: ", mean)
print("standard deviation: ", std)
print("coefficient of variation: ", cv)
print("variance: ", vary)
print(y)

"""
#y = np.sin(0.5 * np.pi * x * (1 + .1 * x))

graph_2 = Graph(x,y)


freq, psd = signal.welch(y)
graph_3 = Graph(x, y)
graph_3.build_powerspectrum_graph()
graph_3.build_frequ_graph()
"""

"""

#label encoding
le = LabelEncoder()
int_encoding = le.fit_transform(pressure_flags)
print("Classes: ",le.classes_, "\n")

#one hot encoding
hot_encoding = keras.utils.to_categorical(int_encoding, num_classes)
#print(hot_encoding.shape[1])

#splitting data into training/testing sets
x_train, x_test, y_train, y_test = train_test_split(atmospheric_pressure, 
hot_encoding, test_size=0.25, shuffle=False)

di = dict()
for x in pressure_flags:
    if x not in di:
        di[x] = 1
    else:
        di[x] += 1

print('total flag dist', di, "\n")

di = dict()
for x in y_train:
    if tuple(x) not in di:
        di[tuple(x)] = 1
    else:
        di[tuple(x)] += 1

print("training set distribution: ",di, "\n")

print("y_train shape:", y_train.shape)

x_test = np.array(x_test)
x_train = np.array(x_train)

x_train = x_train.reshape(10547, 1, 1)
x_test = x_test.reshape(3516, 1, 1)
y_train = y_train.reshape(10547, 1, 2)
y_test = y_test.reshape(3516, 1, 2)
print("Shape", len(x_train.shape))

print("train",len(x_train))
print("test",len(x_test))

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

#Normalization (for 3D data)
scalers = {}
for i in range(x_train.shape[2]):
    scalers[i] = StandardScaler()
    x_train[:, i, :] = scalers[i].fit_transform(x_train[:, i, :]) 

for i in range(x_test.shape[2]):
    x_test[:, i, :] = scalers[i].transform(x_test[:, i, :]) 

#Feature scaling with StandardScaler
#scale_features_std = StandardScaler()
#x_train = scale_features_std.fit_transform(x_train)
#x_test = scale_features_std.transform(x_test)


print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv1D(100, kernel_size=(1), activation='relu', input_shape = (1,1)))
model.add(Dense(10, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(lr= .00001),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# list all data in history
print(history.history.keys())

graph = Graph(None, [history.history['acc'],
history.history['val_acc']],'CNN model accuracy (spike)','accuracy',
'epoch',['train', 'test'])




# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('CNN model accuracy (spike)')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('CNN model loss (spike)')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""



