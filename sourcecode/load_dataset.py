from __future__ import print_function
import os
import sys
import numpy as np
from netCDF4 import Dataset
import pandas as pd
import glob


sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


flag_classes = np.array([b'A', b'B', b'C', b'D', b'E', b'F',
b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'S', b'Z'])



def load_data():

  #Collecting data from NetCDF files
  #Will start with pressure variable
  
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')

  flags = []
  atmospheric_pressure = []
  bad_counter = 0 
  counter = 0
  paths = sorted(glob.glob(my_file))
  paths = paths[1:5]
  for file in paths:
      
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

  return flags, atmospheric_pressure

def load_data_custom(variable):

  #Collecting data from NetCDF files
  #Will start with pressure variable
  
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')

  variable_data = []
  flags = []
  atmospheric_pressure = []
  bad_counter = 0 
  counter = 0
  paths = sorted(glob.glob(my_file))
  paths = paths[1:5]
  for file in paths:
      
      my_file = file
      dataset = Dataset(my_file, 'r', format="NETCDF4")

      #checking flag dimension
      flag_array = (dataset.variables['flag'][0])
      
      if len(flag_array) == 15:
          counter += 1
          #print(len(flag_array))
          variable_data.extend((dataset.variables[variable][:]))
          """
          """

      else:
          bad_counter += 1

  return variable_data

def load_data_custom_path(variable, index, path = '../data/WTDL_pisces/research/2012/*.nc'):

  #Collecting data from NetCDF files
  #Will start with pressure variable
  
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(THIS_FOLDER, path)

  variable_data = []
  flags = []
  atmospheric_pressure = []
  bad_counter = 0 
  counter = 0
  paths = sorted(glob.glob(my_file))
  paths = paths[index:index+1]
  #print(paths)
  for file in paths:
      my_file = file
      dataset = Dataset(my_file, 'r', format="NETCDF4")
      print(dataset.variables['P'].qcindex)
      #checking flag dimension
      flag_array = (dataset.variables['flag'][0])
      
      if len(flag_array) == 15:
          counter += 1
          #print(len(flag_array))
          variable_data.extend((dataset.variables[variable][:]))
          """
          """

      else:
          bad_counter += 1

  return variable_data

def load_all_data():

  #Collecting data from NetCDF files
  #Will start with pressure variable
  
  THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
  my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')

  flags = []
  atmospheric_pressure = []
  bad_counter = 0 
  counter = 0
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

  return flags, atmospheric_pressure


