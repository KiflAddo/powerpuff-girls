import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid
from classes.greedy_random import Greedy_Random
import sys
import pandas as pd


def experiments(number_of_experiments):
    results = []
    for experiment in range(number_of_experiments):
        grid = Grid(houses, batteries)
        algorithm = Greedy_Random(grid)
        algorithm.smallest_distance()
        algorithm.step()
        grid.calculate_costs()
        results.append(grid.costs)

    df = pd.DataFrame(results)
    df.index += 1
    df.columns = ['Cost']
    df.to_csv('Results1.csv')

def experiments2(number_of_experiments, algorithm):
    '''Unfinshed version of experiments that takes an algorithm as input'''

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
