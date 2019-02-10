import os
import sys
import numpy as np
from netCDF4 import Dataset
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import glob

sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')

flags = []
bad_counter = 0 
counter = 0

for file in glob.glob(my_file):
    
    my_file = file
    dataset = Dataset(my_file, 'r', format="NETCDF4")

    #checking flag dimension
    flag_array = (dataset.variables['flag'][0])
    
    if len(flag_array) == 15:
        counter += 1
        #print(len(flag_array))
        #flags.extend((dataset.variables['flag'][:]))
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
        #atmospheric_pressure = dataset.variables['P'][:]
        air_temperature = dataset.variables['T'][:]
        relative_humidity = dataset.variables['RH'][:]
        #sea_temperature = dataset.variables['TS'][:]
        #salinity = dataset.variables['SSPS'][:]
        calendar_date = dataset.variables['date'][:]
        time_of_day = dataset.variables['time_of_day'][:]
    else:
        bad_counter += 1

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
'''

pressure_flags = [value for sublist in flags for counter,value in 
enumerate(sublist) if counter == 10]

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
print((counter))
print(bad_counter)