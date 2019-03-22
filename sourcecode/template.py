from __future__ import print_function
import os
import sys
import numpy as np
from netCDF4 import Dataset
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import glob
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import RMSprop
import tensorflow as tf



sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')


flags = []
flag_classes = np.array([b'A', b'B', b'C', b'D', b'E', b'F',
b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'S', b'Z'])
bad_counter = 0 
counter = 0

"""
#label encoding
le = LabelEncoder()
int_encoding = le.fit_transform(flag_classes)
print(int_encoding)
print(le.classes_, "\n")

#one hot encoding, initializes encoder object, reshapes list of flags...
#transforms flags 
oh_encoding = OneHotEncoder(sparse=False, categories="auto")
reshaped_flag_classes = flag_classes.reshape(len(flag_classes), 1)
oh_encoding = oh_encoding.fit_transform(reshaped_flag_classes)
print(oh_encoding, "\n")


#revert encoding
reverted_flags = [le.inverse_transform([np.argmax(oh_encoding[i,:])])[0] for i,
j in enumerate(oh_encoding)]
print(reverted_flags, "\n")

"""

#Collecting data from NetCDF files
#Will start with pressure variable
atmospheric_pressure = []
for file in glob.glob(my_file):
    
    my_file = file
    dataset = Dataset(my_file, 'r', format="NETCDF4")

    #checking flag dimension
    flag_array = (dataset.variables['flag'][0])
    
    #creating pressure flag
    
    if len(flag_array) == 15:
        counter += 1
        #print(len(flag_array))
        flags.extend((dataset.variables['flag'][:]))
        """
        time = dataset.variables['time'][:]
        lat = dataset.variables['lat'][:]
        lon = dataset.variables['lon'][:]
        platform_heading = dataset.variables['PL_HD'][:]
        platform_course = dataset.variables['PL_CRS'][:]
        earth_relative_wind_direction = dataset.variables['DIR'][:]
        platform_relative_wind_direction = dataset.variables['PL_WDIR'][:]
        platform_speed_over_ground = dataset.variables['PL_SPD'][:]
        earth_relative_wind_speed = dataset.variables['SPD'][:]
        platform_relative_wind_speed = dataset.variables['PL_WSPD'][:]
        """
        atmospheric_pressure.extend(dataset.variables['P'][:])
        """
        air_temperature = dataset.variables['T'][:]
        relative_humidity = dataset.variables['RH'][:]
        #sea_temperature = dataset.variables['TS'][:]
        #salinity = dataset.variables['SSPS'][:]
        """

    else:
        bad_counter += 1
      
#print(len(atmospheric_pressure))
#print(len(flags))

'''
['time', 'lat', 'lon', 'PL_HD', 'PL_CRS', 'DIR', 'PL_WDIR', 'PL_SPD',
 'SPD', 'PL_WSPD', 'P', 'T', 'RH', 'TS', 'SSPS', 'date', 'time_of_day', 'flag',
  'history']
'''

'''
df = pd.DataFrame(data = flags, columns = ['time', 'lat', 'lon', 'PL_HD', 
'PL_CRS', 'DIR', 'PL_WDIR', 'PL_SPD','SPD', 'PL_WSPD', 'P', 'T', 'RH', 'TS',
 'SSPS'])
'''
#flatten flag array & create new array of pressure & relative wind speed
# data from flag[*][10] & flag[*][9]


pressure_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 10]

"""
"""

'''
platform_wind_speed_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 9]
'''
#Attempting to encode labels

#print(flags[0], "variables: ",dataset.variables)

#label_encoder = preprocessing.LabelEncoder()
#label_encoder.fit(flags)
#print("label classes: ",list(label_encoder.classes_))

#encoded_flags = label_encoder.transform(flags)
#print("encoded flags: ",encoded_flags)
#print (dataset.variables.keys())
#print (time_of_day)

#print(pressure_flags)
#print(len(pressure_flags))
#print(platform_wind_speed_flags)
print("counter:",counter)
#print(bad_counter)
print(len(atmospheric_pressure))
#print(atmospheric_pressure)
print(len(pressure_flags))

"""
"""

#Normalizing Data
#lets test without standardizing first...

#Neural Net Structure

batch_size = 1
num_classes = 4
epochs = 20


#label encoding
le = LabelEncoder()
int_encoding = le.fit_transform(pressure_flags)
#print(int_encoding)
print(le.classes_, "\n")

#one hot encoding, initializes encoder object, reshapes list of flags...
#transforms flags 
oh_encoding = OneHotEncoder(sparse=False, categories="auto")
pressure_flags = np.array(pressure_flags)
reshaped_flag_classes = pressure_flags.reshape(len(pressure_flags), 1)
pressure_flags = oh_encoding.fit_transform(reshaped_flag_classes)
print(len(pressure_flags))

# the data, split between train and test sets
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = np.array(atmospheric_pressure[:185292])
x_test = np.array(atmospheric_pressure[185292:])

y_train = np.array(pressure_flags[:185292])
y_test = np.array(pressure_flags[185292:])

pressure_flag_train = y_train
pressure_flag_test = y_test

#pressure_flag_train = pressure_flag_train.reshape(185292, 1)
#pressure_flag_test = pressure_flag_test.reshape(46400, 1)

#Normalize
#x_train = tf.keras.utils.normalize(x_train, axis = 0 - 1)
#y_train = tf.keras.utils.normalize(y_train, axis = 0 - 1)

print("length x_train", len(x_train))
print(x_train)
print("length y_train", len(y_train))
print(y_train)

#Why M x 784?
x_train = x_train.reshape(185292, 1)
x_test = x_test.reshape(46400, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

#y_train = y_train.reshape()
#y_test = y_test.reshape()

#x_train /= 255
#x_test /= 255

print(y_train, 'train samples')
print(y_test.shape[1], 'test samples')

# convert class vectors to binary class matrices
pressure_flag_train = keras.utils.to_categorical(pressure_flag_train, num_classes)
pressure_flag_train = keras.utils.to_categorical(pressure_flag_train, num_classes)

#pressure_flag_train = pressure_flag_train.reshape(185292, 4)
#pressure_flag_train = pressure_flag_test.reshape(46400, 4)

model = Sequential()
model.add(Dense(20, activation='relu', input_dim = 1))
model.add(Dropout(0.2))
model.add(Dense(20, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(4, activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(x_train, pressure_flag_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, pressure_flag_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])

"""
"""
