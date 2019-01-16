"""
Parser for collecting data from QC files
"""
import sys
import os
#import pandas as pd
import re

sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/WTDL_20120404v20001.txt')


with open(my_file) as file:
    file_contents = file.read()
    print(file_contents)

data_types = []
