from load_dataset import load_data, load_all_data, load_data_custom, load_data_custom_path
from display_data import display_data_flag_spread
import glob
import os
import sys
 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/research/2012/*.nc')
paths = glob.glob(my_file)

for count, item in enumerate(paths):
    flag = load_data_custom_path('flag', count)
    flag_count = display_data_flag_spread(flag, 'dict')
    if b'K' not in flag_count:
        print(item)
        print(flag_count)