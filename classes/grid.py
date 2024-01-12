from classes.house_class import House
from classes.battery_class import Battery
from classes.cables_class import Cables
from pprint import pprint
import random

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
            # print(cable.coordinates_list)


    def count_objects(self):
        houses = len(self.houses_and_cables)
        batteries = len(self.batteries)
        count = (houses, batteries)

        return count

    def connected(self):
        '''check if the cable is connected'''
        pass

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

                #
                house_data['cables'] = cable.coordinates_list

                data['houses'].append(house_data)

            # pprint(data)
            true_data.append(data)
            pprint(true_data)

            break
