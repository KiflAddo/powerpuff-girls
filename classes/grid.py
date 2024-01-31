from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from pprint import pprint
import random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


class Grid():
    '''
    This class takes two data files, one containing information about houses
    and one containing information about batteries, and makes each item an
    object. It visualizes these objects in a grid. This class keeps track of the
    grid and all the changes made in the grid with the use of the algorithms.
    '''

    def __init__(self, house_data, battery_data, district, add_batteries=True):
        self.house_data = house_data
        self.battery_data = battery_data
        self.district = district

        self.house_locations = set()

        self.houses_and_cables = {}
        self.batteries = []
        self.costs = 0
        self.shared_segments = {}
        self.smallest_dict = {}
        self.add_houses_and_cables()
        if add_batteries:
            self.add_batteries()




    def add_houses_and_cables(self):
        '''
        get the coordinate and capacity of the houses
        save the houses with it's cable in a the houses_and_cables dict
        '''
        for house in self.house_data:
            split_data = house.split(',')
            pos_x = int(split_data[0])
            pos_y = int(split_data[1])

            # make it one coordinate
            pos_x_y = (pos_x, pos_y)
            capacity = float(split_data[2])

            # make a set of all house locations to prevent crossing house with cable
            self.house_locations.add(pos_x_y)

            # make a dict with cables as value for the house as key
            self.houses_and_cables[House(pos_x, pos_y, capacity)] = Cables()


    def add_batteries(self):
        '''
        Get the coordinate and capacity of the battery
        '''
        for battery in self.battery_data:

            split_data = battery.split(',')
            true_data = [data.strip('"') for data in split_data]
            pos_x = int(true_data[0])
            pos_y = int(true_data[1])

            # make it one coordinate
            pos_x_y = (pos_x, pos_y)
            capacity = float(true_data[2])
            self.batteries.append(Battery(pos_x, pos_y, capacity))
        for battery in self.batteries:
            self.shared_segments[battery] = []



    def calculate_costs(self):
        '''
        function to calculate the costs
        '''
        total_shared_cables = 0
        for battery in self.shared_segments:
            flatten = sum(self.shared_segments[battery], [])
            duplicate_dict = Counter(flatten)
            total_duplicates = sum(duplicate_dict.values())
            unique_values = set(flatten)
            shared_cables = total_duplicates - len(unique_values)
            total_shared_cables += shared_cables

        total_length = 0
        cable_cost = 0
        battery_cost = 0


        # loop through cables and add the total length, use that the calculate cable cost
        for house, cable in self.houses_and_cables.items():

            # length without shared cables
            total_length += len(cable.coordinates_list)
        cable_cost = (total_length - total_shared_cables) * 9

        # loop through the batteries and use that to calculate battery costs
        for battery in self.batteries:
            battery_cost += 5000

        # add the costs together
        self.costs = cable_cost + battery_cost

    def visualize(self):
        '''
        Plots the houses as blue squares, the batteries as red circles and
        the cables connecting the two as green lines
        '''
        # Plot houses and batteries
        self.plot_houses()
        self.plot_batteries()

        # Loop over the batteries
        for battery_kind in self.batteries:

            # Loop over the houses and batteries in 'smallest_dict'
            for house, battery in self.smallest_dict.items():
                # Determine if 'battery' is the same as 'battery_kind' so only
                # the cables connecting the houses assigned to one specific
                # battery are plotted
                if battery == battery_kind:
                    cable = self.houses_and_cables.get(house)

                    x_coord_cable = []
                    y_coord_cable = []

                    for coord in cable.coordinates_list:
                        # Save the x_coordinate of one cable section to the list
                        # x_coord_cable
                        x_coord_cable.append(coord[0])

                        # Save the y_coordinate of one cable section to the list
                        # y_coord_cable
                        y_coord_cable.append(coord[1])

                    # Plot the cables in the right colour based on which battery
                    # they are connected to
                    if battery == self.batteries[0]:
                        plt.plot(x_coord_cable, y_coord_cable, 'g-')

                    elif battery == self.batteries[1]:
                        plt.plot(x_coord_cable, y_coord_cable, 'm-')

                    elif battery == self.batteries[2]:
                        plt.plot(x_coord_cable, y_coord_cable, 'c-')

                    elif battery == self.batteries[3]:
                        plt.plot(x_coord_cable, y_coord_cable, 'y-')

                    elif battery == self.batteries[4]:
                        plt.plot(x_coord_cable, y_coord_cable, 'k-')

        plt.title("Grid")
        plt.show()

    def plot_houses(self):
        '''
        Plots the houses
        '''
        x_pos_list = []
        y_pos_list = []

        # Append x-coordinates and y-coordinates of houses to a list
        for house in self.houses_and_cables:
            x_pos_list.append(int(house.pos_x))
            y_pos_list.append(int(house.pos_y))

        self.ax1.scatter(x_pos_list, y_pos_list, marker='s')

    def plot_batteries(self):
        '''
        Plots the batteries
        '''
        x_pos_list_bat = []
        y_pos_list_bat = []
        colour_bat = []

        # Append x-coordinates and y-coordinates of batteries to a list
        for battery in self.batteries:
            x_pos_list_bat.append(int(battery.pos_x))
            y_pos_list_bat.append(int(battery.pos_y))
            colour_bat.append('r')

        # Plot batteries
        self.ax1.scatter(x_pos_list_bat, y_pos_list_bat, c=colour_bat)


    def setup_plot(self):
        '''
        Sets up the plot
        '''
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal', adjustable='box')

        # Initialize xticks and yticks for the grid
        plt.xticks(list(range(0,51)))
        plt.yticks(list(range(0,51)))

        # Set grid
        self.ax1.grid()

    def output(self):
        '''
        Prints the output of the grid in the correct format
        '''
        true_data = []
        dict = {"district": self.district, "costs-shared": self.costs}

        true_data.append(dict)
        data = {}

        # Loop over batteries
        for battery in self.batteries:
            coord = []
            pos_x_battery = str(battery.pos_x)
            pos_y_battery = str(battery.pos_y)

            coord.append(pos_x_battery)
            coord.append(pos_y_battery)

            # Save the coordinate of the battery, seperated by a comma
            pos_battery = ','.join(coord)

            # Save the coordinate of the battery to the key 'location' (string)
            data['location'] = pos_battery

            # Save the capacity of the battery to the key 'capacity' (float)
            data['capacity'] = battery.capacity

            # Create a key 'houses' with an exmpty string as value
            data['houses'] = []

            # Loop over houses and cables
            for house, cable in self.houses_and_cables.items():
                house_data = {}

                coord_house = []
                pos_x_house = str(house.pos_x)
                pos_y_house = str(house.pos_y)

                coord_house.append(pos_x_house)
                coord_house.append(pos_y_house)

                # Save the coordinate of the house, seperated by a comma
                pos_house = ','.join(coord_house)

                # Save the coordinate of the house to the key 'location' (string)
                house_data['location'] = pos_house

                # Save the capacity of the battery to the key 'output' (float)
                house_data['output'] = house.capacity

                # Save the list containing the coordinates of the cables to the
                # key 'cables' (list)
                house_data['cables'] = cable.coordinates_list

                # Save the dictionary containing the information on the houses
                # to the 'houses' key in the dictionary containing all the data
                data['houses'].append(house_data)


            true_data.append(data)
            pprint(true_data)

    def clear_objects(self):
        '''
        Clears battery objects when the houses need to be connected to different
        batteries
        '''
        for battery in self.batteries:
            battery.used_capacity = 0
