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


class Hill_Climber():
    '''improving steps'''

    def __init__(self, grid):
        self.grid = grid

    def improve_steps(self):
        ''' Takes coordinates from cables
            takes random step
            if cost lower save step in coordinates list
        '''
        bruh = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]
        print(bruh)
        print(bruh[3])
        # move in x direction
        if bruh[3][0] == bruh[3 + 1][0] and bruh[3][0] == bruh[3 - 1][0]:

            bruh.insert(3 - 1, (bruh[3][0] + 1, bruh[3][1] - 1))
            bruh[3] = (bruh[3][0] + 1, bruh[3][1])
            bruh.insert(3 + 1, (bruh[3][0] + 1, bruh[3][1] + 1))
        print(bruh)

        # for house, cable in self.grid.houses_and_cables.items():
        #     random_index = random.randint(0, (len(cable.coordinates_list )- 1))
        #     # print(random_index)
        #     break
        #     print(cable.coordinates_list[random_index])
        #
        #
        #     # move in x direction
        #     if cable.coordinates_list[random_index][0] != cable.coordinates_list[random_index + 1][0]
        #     and cable.coordinates_list[random_index][0] != cable.coordinates_list[random_index - 1][0]:
        #         random.randint(1,2)
        #         if direction == 1:
        #             cable.coordinates_list.insert(5 - 1, ?)
        #             cable.coordinates_list[5] = (cable.coordinates_list[random_index][0] + 1, cable.coordinates_list[random_index][1])
        #             cable.coordinates_list.insert(5 + 1, ?)
        #
        #
        #     # adapt the coordinate and add coordinate before and after it
        #     cable.coordinates_list.insert(random_index - 1, ?)
        #     cable.coordinates_list[random_index] = ?
        #     cable.coordinates_list.insert(random_index + 1, ?)
        #
        #     print(cable.coordinates_list)
        #     break


                # choose random x or y direction
                # direction = random.randint(1,2)
                #
                # # x direction
                # if direction == 1 and cable.coordinates_list[i+1][0]


        # count = 0
        # for house, battery in self.smallest_dict.items():
        #
        #     #Negative means go  left, positive means go right
        #     x_steps = battery.pos_x - house.pos_x
        #     y_steps = battery.pos_y - house.pos_y
        #
        #     # The starting positions that will be updated
        #     cable_x = house.pos_x
        #     cable_y = house.pos_y
        #
        #     # Counting steps for x and y
        #     count_x = 0
        #     count_y = 0
        #
        #     steps_needed = abs(x_steps)+abs(y_steps)
        #
        #
        #     cable = self.grid.houses_and_cables.get(house)
        #     cable.coordinates_list.append((cable_x, cable_y))
        #
        #     # Keep taking steps untill the battery is reached
        #     while cable_x != battery.pos_x or cable_y != battery.pos_y:
        #
        #         # Pick a random direction: 1=along x axis, 2=along y axis
        #         direction = random.randint(1, 2)
        #
        #
        #         if direction == 1 and count_x < abs(x_steps):
        #
        #             # Check if the value is positive and if the possible
        #             if x_steps > 0:
        #                 cable_x += 1
        #                 count_x += 1
        #                 cable_coordinate = (cable_x, cable_y)
        #                 cable.coordinates_list.append(cable_coordinate)
        #
        #             else:
        #                 cable_x -= 1
        #                 count_x += 1
        #                 cable_coordinate = (cable_x, cable_y)
        #                 cable.coordinates_list.append(cable_coordinate)
        #
        #             # If the cable segment is placed on an already existing cable segment you add +1 to the shared segments
        #             if cable_coordinate in self.grid.all_cable_locations:
        #                 self.grid.shared_segments += 1
        #             self.grid.all_cable_locations.add(cable_coordinate)
        #
        #         if direction == 2 and count_y < abs(y_steps):
        #
        #             # Check if the value is negative or positive
        #             if y_steps > 0:
        #                 cable_y += 1
        #                 count_y += 1
        #                 cable_coordinate = (cable_x, cable_y)
        #                 cable.coordinates_list.append(cable_coordinate)
        #
        #             else:
        #                 cable_y -= 1
        #                 count_y += 1
        #                 cable_coordinate = (cable_x, cable_y)
        #                 cable.coordinates_list.append(cable_coordinate)
        #
        #             # If the cable segment is placed on an already existing cable segment you add +1 to the shared segments
        #             if cable_coordinate in self.grid.all_cable_locations:
        #                 self.grid.shared_segments += 1
        #             self.grid.all_cable_locations.add(cable_coordinate)
