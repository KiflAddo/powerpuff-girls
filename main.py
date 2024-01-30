import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid_k_means import Grid
from classes.greedy_random_algorithm import Greedy_Random
from access_data import access_data
from experiment import experiments
from visualize_cost import visualize_cost
import sys
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from classes.hill_climber import Hill_Climber


if __name__ == "__main__":
    batteries = access_data('huizen_batterijen/district_1/district-1_batteries.csv')

    houses = access_data('huizen_batterijen/district_1/district-1_houses.csv')

    # experiments(100)
    grid = Grid(houses, batteries)
    algorithm = Greedy_Random(grid)
    greedy_random_grid = algorithm.run()

    hill = Hill_Climber(greedy_random_grid)
    hill.run()
    hill.visualize('figures/hill_climber-1')
