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
from classes.hill_climber import Hill_Climber
from functies.run_all import run_algorithm
import pandas as pd
from pprint import pprint
import csv
from tqdm import tqdm
import numpy as np



def experiments(number_of_experiments, algorithm, district, file_name, N=3000):
    '''Function that takes an algorithm as input, runs it N times and save the results to a csv '''

    results = {}
    last_cost = np.inf

    # Do the experiment N times
    for experiment in tqdm(range(1, number_of_experiments + 1)):
        experiment_dict = {}
        battery_locations = set()

        # runs a specified algorithm
        new_grid = run_algorithm(algorithm, district, experiment=True)

        # loop through all battery locations and add them to the dictionary
        for battery in new_grid.batteries:
            battery_locations.add(battery.pos_x_y)
        experiment_dict[new_grid.costs] = battery_locations

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
