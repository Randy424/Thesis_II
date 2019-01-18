import os
import sys
from netCDF4 import Dataset

sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/WTDL_20120404v20001.nc')

dataset = Dataset(my_file)
