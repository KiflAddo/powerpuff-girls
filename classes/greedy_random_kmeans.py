from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid_k_means import Grid_kmeans
import random
from sklearn.cluster import KMeans
import numpy as np
from classes.greedy_random import *



class Greedy_Random_kmeans(Greedy_Random):
    '''
    This class takes a grid and applies the Greedy Random algorithm to it. It
    computes and saves the coordinates for the cables connecting the houses
    to their respective batteries, keeping in mind the capacity of the batteries
    and finding the shortest route to these batteries.
    '''

    def __init__(self, grid):
        super().__init__(grid)

    def kmeans(self):
        '''
        Partitions the houses into 5 clusters where each datapoint belongs
        to the cluster with the nearest mean
        '''
        data = self.grid.numpy_houses()

        # Use the sklearn package KMeans to assign the batteries the optimal
        # positions in the grid
        kmeans = KMeans(n_clusters=5, n_init="auto").fit(data)
        kmeans.predict(data)

        # Save the optimal battery coordinates rounded to the nearest number
        # as an integer
        battery_coords = (np.round(kmeans.cluster_centers_)).astype(int)
        self.grid.batt_loc.append(battery_coords)

    def run(self, visualize=False, output=False):
        '''
        Function that calls on each function needed for a single succesfull
        run of the algorithm
        '''
        self.kmeans()
        self.grid.add_batteries()
        self.smallest_distance()
        self.step()
        self.grid.calculate_costs()


        if visualize == True:
            self.grid.setup_plot()
            self.grid.visualize()

        if output == True:
            self.grid.output()

        return self.grid
