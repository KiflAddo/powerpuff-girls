from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from pprint import pprint
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from classes.grid import *

class Grid_kmeans(Grid):
    '''
    This class takes two data files, one containing information about houses
    and one containing information about batteries, and makes each item an
    object. It visualizes these objects in a grid. This class keeps track of the
    grid and all the changes made in the grid with the use of the algorithms.
    '''

    def __init__(self, house_data, battery_data):
        super().__init__(house_data, battery_data)
        self.batt_loc = []

    def numpy_houses(self):
        '''
        Creates a numpy array of the house coordinates which is used for
        the kmeans() function
        '''
        arr = []

        # Loop over houses
        for house in self.houses_and_cables:
            # Save the x and y coordinates of the house to the list 'arr'
            arr.append([house.pos_x, house.pos_y])

        # Convert the list 'arr' to a numpy array
        array = np.array(arr)
        return array
