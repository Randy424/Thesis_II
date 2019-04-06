import glob
import os
import sys
import numpy as np
import pandas as pd
from netCDF4 import Dataset
import pandas as pd
import csv

def find_flags(flag_variable):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, '/Net/samosproc/data/public/research/*')
    ships_paths = glob.glob(my_file)
    ships_paths.sort()
    filename = f"flag_chart_{flag_variable}.csv"
    build_flag_table(filename)
    #print(ships_paths)
    for s_path in ships_paths:
        years_paths = glob.glob(s_path+'/*')
        for y_path in years_paths:
            nc_paths = glob.glob(y_path+'/*.nc')
            for nc in nc_paths:
                flag, index = load_data_custom_path_single(flag_variable, nc)
                flag_count = display_data_flag_spread(flag, index, 'dict')
                if flag_count == None:
                    pass
                else:
                    flag_count['filename'] = nc
                    append_to_flag_table(flag_count, filename)
                if b'S' in flag_count:
                    print(nc)
                    print(flag_count)


def load_data_custom_path_single(variable, path):

    #Collecting data from NetCDF files
    #Will start with pressure variable
    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, path)

    variable_data = []
    my_file = path
    dataset = Dataset(my_file, 'r', format="NETCDF4")

    try:
        #print(dataset.variables[variable].qcindex)
        index = dataset.variables[variable].qcindex
    except:
        print(f"no {variable} variable in: ", path)
        return None, 0

    
    variable_data.extend((dataset.variables['flag'][:]))
    #print(variable_data)
            
    return variable_data, index

def display_data_flag_spread(flags, index, rtype=None):

  if flags == None:
      return None

  variable_flags = [value for sublist in flags for counter,value in 
  enumerate(sublist) if counter == index-1 and value != b'']

  flag_dict = {b'A':0, b'B':0, b'C':0, b'D':0, b'E':0, b'F':0,
    b'G':0, b'H':0, b'I':0, b'J':0, b'K':0, b'L':0, b'M':0, b'N':0,
    b'Q':0, b'S':0, b'Z':0}
  
  for value in variable_flags:
    if value not in flag_dict:
      flag_dict[value] = 1
    else:
      flag_dict[value] += 1
  if rtype == 'dict':
      return flag_dict
  else:
    print(flag_dict)
  

def build_flag_table(filename):
    flag_classes = ['filename', b'A', b'B', b'C', b'D', b'E', b'F',
    b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'Q', b'S', b'Z']
    f = open(filename, "w+")
    writer = csv.DictWriter(f, fieldnames=flag_classes)
    writer.writeheader()
    f.close()

def append_to_flag_table(dictionary, filename):
    flag_classes = ['filename', b'A', b'B', b'C', b'D', b'E', b'F',
    b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'Q', b'S', b'Z']
    f = open(filename, 'a+')
    writer = csv.DictWriter(f, fieldnames=flag_classes)
    print(dictionary)
    writer.writerow(dictionary)


if __name__ == "__main__":
    if(len(sys.argv) == 2):
      find_flags(sys.argv[1])
    else:
      print("Incorrect number of arguments")
    
