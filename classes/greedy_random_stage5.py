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



class Greedy_Random():
    '''Random greedy algorithm'''

    def __init__(self, grid):
        self.coordinates_list = []
        # self.smallest_dict = {}

        self.grid = grid


    def step(self):
        '''Lies the cable in random steps of 1, starting from a house
            untill the cable is connected to a battery'''

        count = 0
        for house, battery in self.grid.smallest_dict.items():

            #Negative means go  left, positive means go right
            x_steps = battery.pos_x - house.pos_x
            y_steps = battery.pos_y - house.pos_y

            # The starting positions that will be updated
            cable_x = house.pos_x
            cable_y = house.pos_y

            # Counting steps for x and y
            count_x = 0
            count_y = 0

            steps_needed = abs(x_steps)+abs(y_steps)


            cable = self.grid.houses_and_cables.get(house)
            cable.coordinates_list.append((cable_x, cable_y))

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
                        cable.coordinates_list.append(cable_coordinate)

                    else:
                        cable_x -= 1
                        count_x += 1
                        cable_coordinate = (cable_x, cable_y)
                        cable.coordinates_list.append(cable_coordinate)

                    # If the cable segment is placed on an already existing cable segment you add +1 to the shared segments

                if direction == 2 and count_y < abs(y_steps):

                    # Check if the value is negative or positive
                    if y_steps > 0:
                        cable_y += 1
                        count_y += 1
                        cable_coordinate = (cable_x, cable_y)
                        cable.coordinates_list.append(cable_coordinate)

                    else:
                        cable_y -= 1
                        count_y += 1
                        cable_coordinate = (cable_x, cable_y)
                        cable.coordinates_list.append(cable_coordinate)

                    # If the cable segment is placed on an already existing cable segment you add +1 to the shared segments
            self.grid.shared_segments[battery].append(cable.coordinates_list)



    def manhattan_distance(self, x1, y1, x2, y2):
        '''function that calculates the manhatten distance'''
        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)

        total_distance = x_distance + y_distance

        return total_distance


    def smallest_distance(self):
        ''''Calculates the battery with the smallest distance from a house'''
        while len(self.grid.smallest_dict) < 150:

            # Shuffle keys
            keys = list(self.grid.houses_and_cables.keys())
            random.shuffle(keys)

            for house in keys:
                count = 0

                # dict with house as key and closest battery as value
                distance_dict = {}

                for battery in self.grid.batteries:

                    # connect house with different battery if the battery capacity is fully used
                    if (battery.used_capacity + house.capacity) <= battery.capacity:
                        # print(battery.used_capacity)
                        distance = self.manhattan_distance(battery.pos_x, battery.pos_y, house.pos_x, house.pos_y)
                        distance_dict[battery] = distance
                        count += 1

                if count == 0:
                    self.grid.smallest_dict.clear()
                    self.grid.clear_objects()
                    break

                # print(len(self.grid.smallest_dict))
                min_dist_battery = min(distance_dict, key=distance_dict.get)
                self.grid.smallest_dict[house] = min_dist_battery
                min_dist_battery.used_capacity += house.capacity


    def kmeans(self):
        '''Partitions the houses into 5 clusters where each datapoint belongs
        to the cluster with the nearest mean'''
        data = self.grid.numpy_houses()

        # Use the sklearn package KMeans to assign the batteries the optimal
        # positions in the grid
        kmeans = KMeans(n_clusters=5, n_init="auto").fit(data)
        kmeans.predict(data)

        # Save the optimal battery coordinates rounded to the nearest number
        # as an integer
        battery_coords = (np.round(kmeans.cluster_centers_)).astype(int)
        self.grid.batt_loc.append(battery_coords)

    def run(self, visualize=False, output=False):
        '''Function that calls on each function needed for a single succesfull
        run of the algorithm'''
        self.kmeans()
        self.grid.add_batteries()
        self.smallest_distance()
        self.step()
        self.grid.calculate_costs()

        print(self.grid.costs)

        if visualize == True:
            self.grid.setup_plot()
            self.grid.visualize()

        if output == True:
            self.grid.output()

        return self.grid
