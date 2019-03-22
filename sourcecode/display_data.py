from __future__ import print_function
import os
import sys
import numpy as np
import pandas as pd
from load_dataset import load_data, load_all_data, load_data_custom, load_data_custom_path

def display_data():

  flags, atmospheric_pressure = load_data()
  sst = load_data_custom('TS')
  at = load_data_custom('T')
  #print(at)
  pressure_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == 10]

  sst_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == 13]

  at_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == 11]


  side_by_side = list(zip(at, atmospheric_pressure, at_flags, pressure_flags))
  print(len(side_by_side))
  """
  df_flags = pd.DataFrame(flags, columns=['time', 'lat', 'lon', 'PL_HD', 'PL_CRS',
  'DIR', 'PL_WDIR', 'PL_SPD', 'SPD', 'PL_WSPD', 'P', 'T', 'RH', 'TS', 'SSPS',])
  """

  df_flag_and_obs = pd.DataFrame(side_by_side, columns=['air temp', 'pressure observation',
  'at flag', 'pressure flag'])

  with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_flag_and_obs)
  #print(df_flag_and_obs)
  return df_flag_and_obs

def show_data_spread():
  flag_classes = np.array([b'A', b'B', b'C', b'D', b'E', b'F',
  b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'S', b'Z'])

def display_data_flag_spread(flags, rtype=None):

  flag_classes = np.array([b'A', b'B', b'C', b'D', b'E', b'F',
  b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'S', b'Z'])

  pressure_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == 10]

  flag_dict = dict()

  for value in pressure_flags:
    if value not in flag_dict:
      flag_dict[value] = 1
    else:
      flag_dict[value] += 1
  if rtype == 'dict':
      return flag_dict
  else:
    print(flag_dict)


if __name__ == "__main__":
  G = display_data()
  print(G.shape[1])