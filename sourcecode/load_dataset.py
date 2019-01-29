import os
import sys
from netCDF4 import Dataset

sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/WTDL_20120404v20001.nc')

dataset = Dataset(my_file, 'r', format="NETCDF4")
flags = dataset.variables['flag'][:]
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
atmospheric_pressure = dataset.variables['P'][:]
air_temperature = dataset.variables['T'][:]
relative_humidity = dataset.variables['RH'][:]
sea_temperature = dataset.variables['TS'][:]
salinity = dataset.variables['SSPS'][:]
calendar_date = dataset.variables['date'][:]
time_of_day = dataset.variables['time_of_day'][:]

'''
['time', 'lat', 'lon', 'PL_HD', 'PL_CRS', 'DIR', 'PL_WDIR', 'PL_SPD',
 'SPD', 'PL_WSPD', 'P', 'T', 'RH', 'TS', 'SSPS', 'date', 'time_of_day', 'flag', 'history']
'''



print (dataset.variables.keys())
print (time_of_day)
