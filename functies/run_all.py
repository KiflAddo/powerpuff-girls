import matplotlib.pyplot as plt
from pprint import pprint
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.greedy_random_kmeans import Greedy_Random_kmeans
from classes.grid_k_means import Grid_kmeans
from classes.grid import Grid
from classes.greedy_random import Greedy_Random
from functies.access_data import access_data
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from classes.hill_climber import Hill_Climber

def run_algorithm(algorithm, district, visualize=False, output=False, experiment=False):
    '''
    This function runs an algorithm specified in the input
    '''

    # acces the data from a specified district
    batteries = access_data(f'huizen_batterijen/district_{district}/district-{district}_batteries.csv')

    houses = access_data(f'huizen_batterijen/district_{district}/district-{district}_houses.csv')

    # initialize the start grid for Hill_Climber
    if algorithm == Hill_Climber:
        start_grid = Grid_kmeans(houses, batteries, district)
        start_algorithm = Greedy_Random_kmeans(start_grid)
        grid = start_algorithm.run()

    #  initialize the start grid for kmeans
    elif algorithm == Greedy_Random_kmeans:

        grid = Grid_kmeans(houses, batteries, district)

    # initialize the start grid for Greedy_Random
    else:
        grid = Grid(houses, batteries, district)

    # Initialize the algorithm
    test_algorithm = algorithm(grid)

    # run the algorithm
    if algorithm == Hill_Climber:
        new_grid = test_algorithm.run(visualize, output)

    else:
        new_grid = test_algorithm.run(visualize, output)


    # returns the grid in case this function is used for experiments
    if experiment == True:
        return new_grid
