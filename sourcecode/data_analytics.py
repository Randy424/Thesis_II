import os
import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
from graph import Graph

class data_analytics:
    """
    Class data_analytics takes a data signal and prints
    mean, standard deviation, coefficient of variation, 
    and variance
    """

    def __init__(self, signal):
        self.signal = np.array(signal)
        self.std = self.signal.std()
        self.cv = self.signal.cv()
        self.mean = self.signal.mean()
        self.variance = self.signal.var()

    def print_analytics(self):

        print("mean: ", self.mean)
        print("standard deviation: ", self.std)
        print("coefficient of variation: ", self.cv)
        print("variance: ", self.variance)
        