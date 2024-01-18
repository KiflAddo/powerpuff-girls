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

if __name__ == "__main__":
    batteries = access_data('huizen_batterijen\district_3\district-3_batteries.csv')

    houses = access_data('huizen_batterijen\district_3\district-3_houses.csv')

    grid1 = Grid(houses, batteries)

    algo1 = Greedy_Random(10, 10, 10, 10, grid1)

    algo1.smallest_distance()

    algo1.step()
    grid1.calculate_costs()
    grid1.setup_plot()
    grid1.visualize()
    # grid1.output()
