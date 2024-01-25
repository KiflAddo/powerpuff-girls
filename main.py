import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid_stage5 import Grid
from classes.greedy_random_stage5 import Greedy_Random
from access_data import access_data
from experiment import experiments
from visualize_cost import visualize_cost
import sys
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np


if __name__ == "__main__":
    batteries = access_data('huizen_batterijen/district_3/district-3_batteries.csv')

    houses = access_data('huizen_batterijen/district_3/district-3_houses.csv')

    # experiments(100)
    grid = Grid(houses, batteries)
    algorithm = Greedy_Random(grid)
    # algorithm.run(visualize=True)

    experiments(10000, Greedy_Random, houses, batteries)
    visualize_cost('results.csv', 'figures/greedy_random3.png')
    #
    # grid.add_batteries()
    # grid.experiments(10)
    # # experiments2(10, algorithm)
    #
    # algorithm.smallest_distance()
    # algorithm.step()
    # grid.calculate_costs()
    # print(grid.costs)
    # grid.setup_plot()
    # grid.visualize()
    # grid.output()
    # print(grid.shared_segments)



    # print(grid.batt_loc)
