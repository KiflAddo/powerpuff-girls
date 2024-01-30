import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.greedy_random_kmeans import Greedy_Random_kmeans
from classes.grid_k_means import Grid_kmeans
from classes.grid import Grid
from classes.greedy_random import Greedy_Random
import sys
import pandas as pd
from pprint import pprint
import csv
from tqdm import tqdm



def experiments(number_of_experiments, algorithm, houses, batteries, file_name):
    '''Function that takes an algorithm as input, runs it N times and save the results to a csv '''

    results = {}

    # Do the experiment N times
    for experiment in tqdm(range(1, number_of_experiments + 1)):
        experiment_dict = {}
        battery_locations = set()

        # choose which grid you want to initialize
        if algorithm == Greedy_Random_kmeans:
            # Initialize the grid
            grid = Grid_kmeans(houses, batteries)
        else:
            grid = Grid(houses, batteries)

        # Initialzie the algorithm
        test_algorithm = algorithm(grid)

        # run the algorithm
        new_grid = test_algorithm.run()


        # loop through all battery locations and add them to the dictionary
        for battery in grid.batteries:
            battery_locations.add(battery.pos_x_y)
        experiment_dict[grid.costs] = battery_locations

        # add the dictionary as a nested dictionary to the results dictionary
        results[experiment] = experiment_dict

    # Open the CSV file in write mode
    with open(file_name, 'w', newline='') as csv_results:

        # Create a CSV writer object
        csv_writer = csv.writer(csv_results)

        # # Write the header row
        csv_writer.writerow(['Experiment', 'Costs', 'Coordinates'])

        # Write the data rows
        for experiment, cost_coordinates_dict in results.items():
            for cost, coordinates_set in cost_coordinates_dict.items():

                # Write the row
                csv_writer.writerow([experiment, cost, coordinates_set])
