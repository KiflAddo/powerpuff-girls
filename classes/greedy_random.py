
from classes.house import House
from classes.battery import Battery
from classes.cables import Cables
from classes.grid import Grid
import random



class Greedy_Random():
    '''
    This class takes a grid and applies the Greedy Random algorithm to it. It
    computes and saves the coordinates for the cables connecting the houses
    to their respective batteries, keeping in mind the capacity of the batteries
    and finding the shortest route to these batteries.
    '''


    def __init__(self, grid):
        self.coordinates_list = []
        self.smallest_dict = {}

        self.grid = grid


    def step(self):
        '''
        Lies the cable in steps of 1, either first all in x direction or in
        y direction, starting from a house, untill the cable is connected to
        a battery
        '''

        # Loop over houses and batteries in the dictionary 'smallest_dict'
        for house, battery in self.grid.smallest_dict.items():

            # Find out how many steps in which direction need to be set
            self.initialize_steps(house, battery)

            self.cable = self.grid.houses_and_cables.get(house)
            self.cable.coordinates_list.append((self.cable_x, self.cable_y))

            # Pick a random direction: 1=along x axis, 2=along y axis
            direction = random.randint(1, 2)

            # Keep taking steps untill the battery is reached
            while self.cable_x != battery.pos_x or self.cable_y != battery.pos_y:

                if direction == 1:
                    while self.count_x < abs(self.x_steps):
                        self.step_x(battery)
                    while self.count_y < abs(self.y_steps):
                        self.step_y(battery)

                if direction == 2:
                    while self.count_y < abs(self.y_steps):
                        self.step_y(battery)
                    while self.count_x < abs(self.x_steps):
                        self.step_x(battery)

            self.grid.shared_segments[battery].append(self.cable.coordinates_list)

    def initialize_steps(self, house, battery):
        '''
        Initializes how many steps need to be set in both the x and the y
        direction for the house to be connected to the battery
        :Param
            house: house object being looped over
            battery: battery object being looped over
        '''
        # Negative means go  left, positive means go right
        self.x_steps = battery.pos_x - house.pos_x
        self.y_steps = battery.pos_y - house.pos_y

        # The starting positions that will be updated
        self.cable_x = house.pos_x
        self.cable_y = house.pos_y

        # Counting steps for x and y
        self.count_x = 0
        self.count_y = 0


    def step_x(self, battery):
        '''
        Sets a step in the x direction, saves the coordinate to the list of
        cable coordinates
        :Param
            battery: battery object being looped over
        '''
        # Check if the value is positive and if the possible
        if self.x_steps > 0:
            # Change x-coord
            self.cable_x += 1
            self.count_x += 1

            # Save new coordinate to list of cable coordinates
            cable_coordinate = (self.cable_x, self.cable_y)
            self.cable.coordinates_list.append(cable_coordinate)

        else:
            # Change x_coord
            self.cable_x -= 1
            self.count_x += 1

            # Save new coordinate to list of cable coordinates
            cable_coordinate = (self.cable_x, self.cable_y)
            self.cable.coordinates_list.append(cable_coordinate)


    def step_y(self, battery):
        '''
        Sets a step in the y direction, saves the coordinate to the list of
        cable coordinates
        :Param
            battery: battery object being looped over
        '''
        # Check if the value is positive
        if self.y_steps > 0:
            # Change y-coord
            self.cable_y += 1
            self.count_y += 1

            # Save new coordinate to list of cable coordinates
            cable_coordinate = (self.cable_x, self.cable_y)
            self.cable.coordinates_list.append(cable_coordinate)

        else:
            # Change y-coord
            self.cable_y -= 1
            self.count_y += 1

            # Save new coordinate to list of cable coordinates
            cable_coordinate = (self.cable_x, self.cable_y)
            self.cable.coordinates_list.append(cable_coordinate)



    def manhattan_distance(self, x1, y1, x2, y2):
        '''
        Function that calculates the manhatten distance
        '''
        x_distance = abs(x1 - x2)
        y_distance = abs(y1 - y2)

        total_distance = x_distance + y_distance

        return total_distance


    def smallest_distance(self):
        ''''
        Calculates the battery with the smallest distance from a house
        '''
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

    def run(self, visualize=False, output=False):
        '''
        Function that calls on each function needed for a single succesfull
        run of the algorithm
        '''

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
