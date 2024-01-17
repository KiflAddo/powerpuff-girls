import matplotlib.pyplot as plt
from pprint import pprint
import re
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid



class Greedy_Random():
    '''Random greedy algorithm'''

    def __init__(self, x_house, y_house, x_battery, y_battery, grid):
        self.coordinates_list = []
        # pos_x_y = x, y
        self.x_house = x_house
        self.y_house = y_house
        self.x_battery = x_battery
        self.y_battery = y_battery

        # self.coordinates.append(pos_x_y)
        self.connected = False
        self.grid = grid

    def step(self):
        # Determine how many steps we have to take on each axis. Negative means to
        # the left, positive means to the right
        x_steps = self.x_battery - self.x_house
        y_steps = self.y_battery - self.y_house

        # The starting positions that will be updated
        cable_x = self.x_house
        cable_y = self.y_house

        # Counting steps for x and y
        count_x = 0
        count_y = 0

        steps_needed = abs(x_steps)+abs(y_steps)

        # Take the right amount of steps
        while steps_needed > steps_taken:

            # Pick a random direction: 1=along x axis, 2=along y axis
            direction = random.randint(1, 2)

            if direction == 1 and count_x < abs(x_steps):
                # Check if the value is negative or positive
                if x_steps > 0:
                    cable_x += 1
                elif x_steps < 0:
                    cable_x -= 1

                steps_taken += 1
                count_x += 1

            if direction == 2 and count_y < abs(y_steps):
                # Check if the value is negative or positive
                if y_steps > 0:
                    cable_y += 1
                elif y_steps < 0:
                    cable_y -= 1

                steps_taken += 1
                count_y += 1

            # Save coordinate to list
            self.coordinates.append((pos_h_x, pos_h_y))

        print(self.coordinates)

    def manhattan_distance(self, x1, y1, x2, y2):

        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)

        total_distance = x_distance + y_distance

        return total_distance


    def smallest_distance(self):
        smallest_dict = {}
        for house in self.grid.houses_and_cables:
            distance_dict = {}
            cum_cap = 0
            for battery in self.grid.batteries:
                distance = self.manhattan_distance(battery.pos_x, battery.pos_y, house.pos_x, house.pos_y)
                distance_dict[house] = distance
            while cum_cap < battery.capacity:
                min_dist_house = min(distance_dict, key=distance_dict.get)
                cum_cap = cum_cap + min_dist_house.capacity

                if battery not in smallest_dict:
                    smallest_dict[battery] = []

                else:
                    smallest_dict[battery].append(min_dist_house)

                del distance_dict[min_dist_house]
        print(smallest_dict)
