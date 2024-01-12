import random

import matplotlib.pyplot as plt
from pprint import pprint

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

class Battery():
    def __init__(self, pos_x, pos_y, pos_x_y capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_y = pos_x_y
        self.capacity = capacity


class House():
    def __init__(self, pos_x, pos_y, pos_x_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_y = pos_x_y
        self.capacity = capacity


class Cables():
    '''class for cables'''
    def __init__(self):
        self.coordinates_list = []
        self.connected = False

class Grid():
    '''Grid with houses and cables as dict. Batteries will be put in a list'''

    def __init__(self, house_data, battery_data):
        self.house_data = house_data
        self.battery_data = battery_data

        # house = key, cables = value as list of coordinates
        self.houses_and_cables = {}
        self.batteries = []
        self.cables_list = []
        self.add_houses_and_cables()
        self.add_batteries()


    def add_houses_and_cables(self):
        '''get the coordinate and capacity of the house
        save the house with it's cable in a the houses_and_cables dict'''

        for house in self.house_data:
            split_data = house.split(',')
            pos_x = split_data[0]
            pos_y = split_data[1]

            # make it one coordinate
            pos_x_y = (pos_x, pos_y)
            capacity = split_data[2]

            # cables as value for the house as key in dict
            self.houses_and_cables[House(pos_x, pos_y, pos_x_y, capacity)] = Cables()


    def add_batteries(self):
        '''get the coordinate and capacity of the battery'''

        for battery in self.battery_data:
            split_data = battery.split(',')
            pos_x = split_data[0]
            pos_y = split_data[1]

            # make it one coordinate
            pos_x_y = (pos_x, pos_y)
            capacity = split_data[2]
            self.batteries.append(Battery(pos_x, pos_y, pos_x_y, capacity))


    def cable_coordinates(self):
        '''generates random coordinates as a cable'''

        for house, cable in self.houses_and_cables.items():
            for x in range(10):
                coordinate = (random.randint(0, 10), random.randint(0, 10))
                cable.coordinates_list.append(coordinate)
            print(cable.coordinates_list)


    def count_objects(self):
        houses = len(self.houses_and_cables)
        batteries = len(self.batteries)
        count = (houses, batteries)

        return count

    def connected(self):
        '''check if the cable is connected'''
        pass



if __name__ == "__main__":
    batteries = access_data('test_batteries.csv')

    houses = access_data('test_houses.csv')

    true_grid = Grid(houses, batteries)

    print(true_grid.count_objects())
    true_grid.cable_coordinates()
