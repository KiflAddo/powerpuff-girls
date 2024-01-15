import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid

def access_data(file_name):
    data = []

    # open the file
    file = open(f'{file_name}', 'r')

    #remove the \n in every line
    true_file = (line.replace('\n', '') for line in file)

    #skip the first line
    for i in range(1):
        next(true_file)

    for line in true_file:
        data.append(line)

    return data


if __name__ == "__main__":
    batteries = access_data('huizen_batterijen/test_data/test_batteries.csv')

    houses = access_data('huizen_batterijen/test_data/test_houses.csv')

    true_grid = Grid(houses, batteries)

    # print(true_grid.count_objects())
    true_grid.is_connected()
    true_grid.calculate_costs()
    true_grid.output()
