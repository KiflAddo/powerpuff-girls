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
    batteries = access_data('huizen_batterijen\district_1\district-1_batteries.csv')

    houses = access_data('huizen_batterijen\district_1\district-1_houses.csv')

    grid1 = Grid(houses, batteries)

    algo1 = Greedy_Random(10, 10, 10, 10, grid1)

    algo1.smallest_distance()
