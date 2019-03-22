from __future__ import print_function
import os
import sys
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop
from load_dataset import load_data, load_all_data
from display_data import display_data
from sklearn.model_selection import train_test_split
import tensorflow as tf

config = tf.ConfigProto(intra_op_parallelism_threads=0, 
                        inter_op_parallelism_threads=0, 
                        allow_soft_placement=True)

session = tf.Session(config=config)

batch_size = 4
num_classes = 4
epochs = 15

#loading data
flags, atmospheric_pressure = load_data()
pressure_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 10]

#label encoding
le = LabelEncoder()
int_encoding = le.fit_transform(pressure_flags)
print(le.classes_, "\n")

#one hot encoding
hot_encoding = keras.utils.to_categorical(int_encoding, num_classes)
print(hot_encoding.shape[1])

#split training and testing data
x_train, x_test, y_train, y_test = train_test_split(atmospheric_pressure, 
hot_encoding, test_size=0.25, shuffle=False)

x_test = np.array(x_test)
x_train = np.array(x_train)

#reshaping to single feature matrix aka vector
x_train = x_train.reshape(-1,1)
x_test = x_test.reshape(-1,1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

#Normalization
#Feature scaling with StandardScaler
scale_features_std = StandardScaler()
x_train = scale_features_std.fit_transform(x_train)
x_test = scale_features_std.fit_transform(x_test)

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical(y_train, num_classes)
#y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(1,)))
model.add(Dropout(0.2))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
"""
"""
#display_data()







