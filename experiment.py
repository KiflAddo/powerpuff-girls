import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.greedy_random_stage5 import Greedy_Random
from classes.grid_stage5 import Grid
import sys
import pandas as pd
from pprint import pprint
import csv


def experiments(number_of_experiments, algorithm_heuristic, houses, batteries):
    '''Function that takes an algorithm as input, runs it N times and save the results to a csv '''

    results = {}

    # Do the experiment N times
    for experiment in range(1, number_of_experiments + 1):
        experiment_dict = {}
        battery_locations = set()

        grid = Grid(houses, batteries)
        algorithm = algorithm_heuristic(grid)
        algorithm.kmeans()
        grid.add_batteries()
        algorithm.smallest_distance()
        algorithm.step()
        grid.calculate_costs()

        # loop through all battery locations and add them to the dictionary
        for battery in grid.batteries:
            battery_locations.add(battery.pos_x_y)
        experiment_dict[grid.costs] = battery_locations

        # add the dictionary as a nested dictionary to the results dictionary
        results[experiment] = experiment_dict

    # Open the CSV file in write mode
    with open('results.csv', 'w', newline='') as csv_results:

        # Create a CSV writer object
        csv_writer = csv.writer(csv_results)

        # # Write the header row
        csv_writer.writerow(['Experiment', 'Costs', 'Coordinates'])

        # Write the data rows
        for experiment, cost_coordinates_dict in results.items():
            for cost, coordinates_set in cost_coordinates_dict.items():

                # Write the row
                csv_writer.writerow([experiment, cost, coordinates_set])
