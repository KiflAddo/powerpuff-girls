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
import pandas as pd

def experiments(number_of_experiments):
    results = []
    for experiment in range(number_of_experiments):
        grid = Grid(houses, batteries)
        algorithm = Greedy_Random(10, 10, 10, 10, grid)
        algorithm.smallest_distance()
        algorithm.step()
        grid.calculate_costs()
        results.append(grid.costs)

    df = pd.DataFrame(results)
    df.index += 1
    df.columns = ['Cost']
    df.to_csv('Results1.csv')

def experiments2(number_of_experiments, algorithm):
    results = []
    for experiment in range(number_of_experiments):
        grid = Grid(houses, batteries)
        algorithm.smallest_distance()
        algorithm.step()
        grid.calculate_costs()
        results.append(grid.costs)

    df = pd.DataFrame(results)
    df.index += 1
    df.columns = ['Cost']
    df.to_csv('Results2.csv')

if __name__ == "__main__":
    batteries = access_data('huizen_batterijen/district_2/district-2_batteries.csv')

    houses = access_data('huizen_batterijen/district_2/district-2_houses.csv')
    # grid = Grid(houses, batteries)
    algorithm = Greedy_Random(10, 10, 10, 10, grid)

    # experiments(10)
    experiments2(10, algorithm)


    # grid1.setup_plot()
    # grid1.visualize()
    # grid1.output()
