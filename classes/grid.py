from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from pprint import pprint
import random
import matplotlib.pyplot as plt

class Grid():
    '''Grid with houses and cables as dict. Batteries will be put in a list'''

    def __init__(self, house_data, battery_data):
        self.house_data = house_data
        self.battery_data = battery_data

        # house = key, cables = value as list of coordinates
        self.houses_and_cables = {}
        self.batteries = []
        self.cables_list = []
        self.costs = 0
        self.add_houses_and_cables()
        self.add_batteries()
        # self.cable_coordinates()

        self.setup_plot()
        self.visualize()



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
            true_data = [data.strip('"') for data in split_data]
            pos_x = true_data[0]
            pos_y = true_data[1]

            # make it one coordinate
            pos_x_y = (pos_x, pos_y)
            capacity = true_data[2]
            self.batteries.append(Battery(pos_x, pos_y, pos_x_y, capacity))


    # def cable_coordinates(self):
    #     '''generates random coordinates as a cable'''
    #     for house, cable in self.houses_and_cables.items():
    #         for x in range(10):
    #             coordinate = (random.randint(0, 10), random.randint(0, 10))
    #             cable.coordinates_list.append(coordinate)


    def count_objects(self):
        """Counting the number of objects"""
        houses = len(self.houses_and_cables)
        batteries = len(self.batteries)
        count = (houses, batteries)

        return count

    def is_connected(self):
        '''check if the cable is connected'''

        for house, cable in self.houses_and_cables.items():

            while cable.connected == False:
                cable.step(house.pos_x, house.pos_y)

                # chack if in battery coordinates
                if cable.coordinates_list[-1] in self.batteries.battery.pos_x_y:
                    cable.connected = True


    def calculate_costs(self):
        '''function to calculate the costs'''

        total_length = 0
        cable_cost = 0
        battery_cost = 0

        # loop through cables and add the total length, use that the calculate cable cost
        for house, cable in self.houses_and_cables.items():
            total_length += len(cable.coordinates_list)
        cable_cost = total_length * 9

        # loop through the batteries and use that to calculate battery costs
        for battery in self.batteries:
            battery_cost += 5000

        # add the costs together
        self.costs = cable_cost + battery_cost

    def visualize(self):
        '''Plots the houses as blue squares, the batteries as red circles and
        the cables connecting the two as green lines'''
        x_pos_list = []
        y_pos_list = []

        # Append x-coordinates and y-coordinates of houses to a list
        for house in self.houses_and_cables:
            x_pos_list.append(int(house.pos_x))
            y_pos_list.append(int(house.pos_y))


        x_pos_list_bat = []
        y_pos_list_bat = []
        colour_bat = []

        # Append x-coordinates and y-coordinates of batteries to a list
        for battery in self.batteries:
            x_pos_list_bat.append(int(battery.pos_x))
            y_pos_list_bat.append(int(battery.pos_y))
            colour_bat.append('r')

        # Plot houses and batteries
        self.ax1.scatter(x_pos_list, y_pos_list, marker='s')
        self.ax1.scatter(x_pos_list_bat, y_pos_list_bat, c=colour_bat)

        # Initialize xticks and yticks for the grid
        plt.xticks(list(range(0,51)))
        plt.yticks(list(range(0,51)))

        # Set grid
        self.ax1.grid()

        # Loop over houses and cables
        for house, cable in self.houses_and_cables.items():
            x_coord_cable = []
            y_coord_cable = []

            # Loop over coordinates of the cables of one house
            for coord in cable.coordinates_list:

                # Save the x_coordinate of one cable section to the list
                # x_coord_cable
                x_coord_cable.append(coord[0])

                # Save the y_coordinate of one cable section to the list
                # y_coord_cable
                y_coord_cable.append(coord[1])

            # Plot the cable connection the house to a battery
            plt.plot(x_coord_cable, y_coord_cable, 'g-')

        plt.show()


    def setup_plot(self):
        '''Sets up the plot'''
        self.fig, self.ax1 = plt.subplots(1)


    def output(self):
        true_data = []
        dict = {"district": 1, "costs-shared": self.costs}

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
