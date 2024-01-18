import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid
from classes.greedy_random import Greedy_Random
from representatie import access_data
import sys
import csv

if __name__ == "__main__":
    batteries = access_data('huizen_batterijen/district_2/district-2_batteries.csv')

    houses = access_data('huizen_batterijen/district_2/district-2_houses.csv')
    number_experiments = 10
    results = []
    for experiment in range(1, number_experiments + 1):
        single_experiment = {}
        grid = Grid(houses, batteries)
        algo = Greedy_Random(10, 10, 10, 10, grid)
        algo.smallest_distance()
        algo.step()
        grid.calculate_costs()
        single_experiment[experiment] = grid.costs
        results.append(single_experiment)

    print(results)

    # grid1.setup_plot()
    # grid1.visualize()
    # grid1.output()
