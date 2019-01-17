"""
Parser for collecting data from QC files
"""
import sys
import os
import pandas as pd
import re

sys.path.append('../data/WTDL_pisces')
sys.path.append('../data/KAQP_atlantis')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/WTDL_20120404v20001.txt')


with open(my_file) as file:
    file_contents = file.read()
    #print(file_contents)

data_types = []
data_container = []

#regular expressions for parsing data
rx_data = {
    'time': re.compile(r'time = (?P<time>.*);')
}

#the line parser as a function (helper function)
def _parse_line(line):

    """
    regex search for all defined regex's
    returns the key and match result
    """

    for key, rx in rx_data.items():
        match = rx.search(line)
        if match:
            return key, match
        #return None when no matches are made
    return None, None

#file parser
def parse_file(filepath):
    """
    given filepath, parse file

    parmeters:
    filepath (str)

    returns:
    data (pd.DataFrame)
        parsed data
    """
    # for holding data
    data = []

    #open file, read line-by-line
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:
            #search each line for a match with regex
            key, match = _parse_line(line)

            if key == 'time ':
                time = match.group('time')
            while line.strip():
                time = line.strip().split(',')
                
                row = {
                    'time': time
                }

                data.append(row)
                line = file_object.readline()
            line = file_object.readline()
         # create a pandas DataFrame from the list of dicts
        data = pd.DataFrame(data)
        # set the School, Grade, and Student number as the index
        data.set_index(['time'], inplace=True)
        # consolidate df to remove nans
        data = data.groupby(level=data.index.names).first()
        # upgrade Score from float to integer
        data = data.apply(pd.to_numeric, errors='ignore')
    return data

