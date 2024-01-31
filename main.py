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
from functies.access_data import access_data
from functies.experiment import experiments
from functies.visualize_cost import visualize_cost
import sys
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from classes.hill_climber import Hill_Climber
from functies.run_all import run_algorithm


if __name__ == "__main__":
    # batteries = access_data(f'huizen_batterijen/district_{1}/district-{1}_batteries.csv')
    #
    # houses = access_data(f'huizen_batterijen/district_{1}/district-{1}_houses.csv')

    # grid = Grid_kmeans(houses, batteries)
    # algorithm = Greedy_Random_kmeans(grid)
    # greedy_random_grid = algorithm.run()
    # experiments(10, Greedy_Random_kmeans, 1, 'results.csv')
    # visualize_cost('results.csv', 'test_hill')

    # hill = Hill_Climber(greedy_random_grid)
    # hill.run(visualize=True, output=True)
    # print(hill.all_costs)
    # hill.visualize('figures/hill_climber-1')

    # run_algorithm(Hill_Climber, 1, visualize=True)
