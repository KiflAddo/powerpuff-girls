import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid
import random



class Greedy_Random():
    '''Random greedy algorithm'''

    def __init__(self, x_house, y_house, x_battery, y_battery, grid):
        self.coordinates_list = []
        self.smallest_dict = {}
        # pos_x_y = x, y
        self.x_house = x_house
        self.y_house = y_house
        self.x_battery = x_battery
        self.y_battery = y_battery

        # self.coordinates.append(pos_x_y)
        self.connected = False
        self.grid = grid


    def step(self):
        for house, battery in self.smallest_dict.items():

            # Determine how many steps we have to take on each axis. Negative means to
            # the left, positive means to the right
            x_steps = battery.pos_x - house.pos_x
            y_steps = battery.pos_y - house.pos_y

            # The starting positions that will be updated
            cable_x = house.pos_x
            cable_y = house.pos_y

            # Counting steps for x and y
            count_x = 0
            count_y = 0

            steps_needed = abs(x_steps)+abs(y_steps)

            # Keep taking steps untill the battery is reached
            while cable_x != battery.pos_x or cable_y != battery.pos_y:

                # Pick a random direction: 1=along x axis, 2=along y axis
                direction = random.randint(1, 2)

                if direction == 1 and count_x < abs(x_steps):
                    # Check if the value is positive and if the possible
                    # coordinate is not in the set of house coordinates
                    if x_steps > 0 and (cable_x + 1, cable_y) not in self.grid.house_locations:
                        cable_x += 1
                        count_x += 1
                        self.grid.houses_and_cables.get(house).coordinates_list.append((cable_x, cable_y))

                    # Check if the value is negative and if the possible
                    # coordinate is not in the set of house coordinates
                    elif x_steps < 0 and (cable_x - 1, cable_y) not in self.grid.house_locations:
                        cable_x -= 1
                        count_x += 1
                        self.grid.houses_and_cables.get(house).coordinates_list.append((cable_x, cable_y))

                    # If there is a house in the way, change direction
                    else:
                        direction = 2
                        # If we cannot take anymore steps in the y direction, restart
                        # by resetting count_x and count_y and clear the list with
                        # coordinates
                        if count_y == abs(y_steps):
                            count_x = 0
                            count_y = 0
                            self.grid.houses_and_cables.get(house).coordinates_list.clear()



                if direction == 2 and count_y < abs(y_steps):
                    # Check if the value is negative or positive
                    if y_steps > 0 and cable_y + 1 not in self.grid.house_locations:
                        cable_y += 1
                        count_y += 1
                        self.grid.houses_and_cables.get(house).coordinates_list.append((cable_x, cable_y))

                    elif y_steps < 0 and cable_y - 1 not in self.grid.house_locations:
                        cable_y -= 1
                        count_y += 1
                        self.grid.houses_and_cables.get(house).coordinates_list.append((cable_x, cable_y))

                    else:
                        direction = 1
                        if count_x == abs(x_steps):
                            count_x = 0
                            count_y = 0
                            self.grid.houses_and_cables.get(house).coordinates_list.clear()



    def manhattan_distance(self, x1, y1, x2, y2):

        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)

        total_distance = x_distance + y_distance

        return total_distance


    def smallest_distance(self):
        ''''Calculates the battery with the smallest distance from a house'''
        count = 0
        for house in self.grid.houses_and_cables:

            # dict with house as key and closest battery as value
            distance_dict = {}

            for battery in self.grid.batteries:

                # connect house with different battery if the battery capacity is fully used
                if battery.used_capacity <= battery.capacity:
                    # print(battery.used_capacity)
                    distance = self.manhattan_distance(battery.pos_x, battery.pos_y, house.pos_x, house.pos_y)
                    distance_dict[battery] = distance
            min_dist_battery = min(distance_dict, key=distance_dict.get)
            self.smallest_dict[house] = min_dist_battery
            min_dist_battery.used_capacity += house.capacity
