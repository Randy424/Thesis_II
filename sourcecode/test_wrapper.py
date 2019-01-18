from parser import parse_file, _parse_line
import parser
import sys
import os
import pandas as pd
import re


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../data/WTDL_pisces/WTDL_20120404v20001.txt')


if __name__ == '__main__':
    data = parse_file(my_file)
    print(data)