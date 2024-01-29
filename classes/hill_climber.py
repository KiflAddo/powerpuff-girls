import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid
import random
from sklearn.cluster import KMeans
import numpy as np
import copy


class Hill_Climber():
    '''improving steps'''

    def __init__(self, grid):
        self.grid = grid

    def run(self):
        ''' Takes the step function multiple times untill improvement '''

        house_keys = list(self.grid.houses_and_cables.keys())

        # list and counter to plot costs with iterations
        all_costs = []
        iterations = 0

        while iterations < 10000:

            # calculate the old cost before taking a different path
            self.grid.calculate_costs()
            old_cost = self.grid.costs

            iterations += 1
            print(iterations)

            # get a random house from the dictionary
            house, battery, cable = self.choose_house(house_keys)

            # remove all coordinates to lay a new cable
            self.grid.shared_segments[battery].remove(cable.coordinates_list)

            # save the old coordinates in case the cost doesn't decrease
            old_coordinates_list = copy.deepcopy(cable.coordinates_list)

            # Keep taking steps untill the battery is reached
            new_coordinates_list = self.step(battery, cable, house)

            # put the new coordinates in the dictionary
            cable.coordinates_list = new_coordinates_list
            self.grid.shared_segments[battery].append(new_coordinates_list)

            # calculate the new cost after adapting the cable
            self.grid.calculate_costs()
            new_cost = self.grid.costs

            # If the costs did not decrease remove the changes made
            if old_cost < new_cost:
                self.grid.shared_segments[battery].remove(new_coordinates_list)

                cable.coordinates_list.clear()

                cable.coordinates_list = old_coordinates_list

                self.grid.shared_segments[battery].append(cable.coordinates_list)

                all_costs.append(old_cost)

            # else keep the changes made
            else:
                all_costs.append(new_cost)

        print(all_costs)


    def step(self, battery, cable, house):

        new_coordinates_list = []

        # Negative means go left, positive means go right
        x_steps = battery.pos_x - house.pos_x
        y_steps = battery.pos_y - house.pos_y
        steps_needed = abs(x_steps)+abs(y_steps)

        # The starting positions that will be updated
        cable_x = house.pos_x
        cable_y = house.pos_y
        new_coordinates_list.append((cable_x, cable_y))

        # Counting steps for x and y
        count_x = 0
        count_y = 0


        # Keep taking steps untill the battery is reached
        while cable_x != battery.pos_x or cable_y != battery.pos_y:

            # Pick a random direction: 1=along x axis, 2=along y axis
            direction = random.randint(1, 2)

            if direction == 1 and count_x < abs(x_steps):

                # Check if the value is positive and if the possible
                if x_steps > 0:
                    cable_x += 1
                    count_x += 1
                    cable_coordinate = (cable_x, cable_y)
                    new_coordinates_list.append(cable_coordinate)

                else:
                    cable_x -= 1
                    count_x += 1
                    cable_coordinate = (cable_x, cable_y)
                    new_coordinates_list.append(cable_coordinate)

            if direction == 2 and count_y < abs(y_steps):

                # Check if the value is negative or positive
                if y_steps > 0:
                    cable_y += 1
                    count_y += 1
                    cable_coordinate = (cable_x, cable_y)
                    new_coordinates_list.append(cable_coordinate)

                else:
                    cable_y -= 1
                    count_y +=1
                    cable_coordinate = (cable_x, cable_y)
                    new_coordinates_list.append(cable_coordinate)
        return new_coordinates_list

    def choose_house(self, house_keys):

        # get a random house from the dictionary
        house = random.choice(house_keys)

        # get the battery that belongs to this random house
        battery = self.grid.smallest_dict[house]

        # Get the cable that belongs to the house
        cable = self.grid.houses_and_cables[house]

        return house, battery, cable
