from __future__ import print_function
import os
import sys
import numpy as np
import pandas as pd
from load_dataset import load_data, load_all_data

def display_data():

  flags, atmospheric_pressure = load_data()

  pressure_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == 10]

  side_by_side = list(zip(atmospheric_pressure, pressure_flags))

  """
  df_flags = pd.DataFrame(flags, columns=['time', 'lat', 'lon', 'PL_HD', 'PL_CRS', 'DIR', 'PL_WDIR', 'PL_SPD',
  'SPD', 'PL_WSPD', 'P', 'T', 'RH', 'TS', 'SSPS',])
  """

  df_flag_and_obs = pd.DataFrame(side_by_side, columns=['pressure observation', 'flag'])

  print(df_flag_and_obs)
  return df_flag_and_obs


if __name__ == "__main__":
  G = display_data()
  print(G.shape[1])