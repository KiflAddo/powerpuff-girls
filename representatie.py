import matplotlib.pyplot as plt
from pprint import pprint
import re
import classes.house_class

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
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity


class House():
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity


class Grid():
    def __init__(self, house_data, battery_data):
        self.house_data = house_data
        self.battery_data = battery_data
        self.houses = []
        self.batteries = []
        self.add_houses()
        self.add_batteries()

        # self.setup_plot()
        # self.visualize()

        self.output()

    def add_houses(self):
        for house in self.house_data:
            split_data = house.split(',')
            pos_x = split_data[0]
            pos_y = split_data[1]
            capacity = split_data[2]
            self.houses.append(House(pos_x, pos_y, capacity))

    def add_batteries(self):
        for battery in self.battery_data:
            true_battery_data = battery.replace('"', '')
            split_data = true_battery_data.split(',')
            pos_x = split_data[0]
            pos_y = split_data[1]
            capacity = split_data[2]
            self.batteries.append(Battery(pos_x, pos_y, capacity))


    def count_objects(self):
        houses = len(self.houses)
        batteries = len(self.batteries)
        count = (houses, batteries)
        return count

    def visualize(self):
        """
        Plotting the batteries and houses in a grid
        """
        x_pos_list = []
        y_pos_list = []

        # Append x-coordinates and y-coordinates of houses to a list
        for house in self.houses:
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
        self.ax1.scatter(x_pos_list, y_pos_list)
        self.ax1.scatter(x_pos_list_bat, y_pos_list_bat, c=colour_bat)

        # Initialize xticks and yticks for the grid
        plt.xticks(list(range(0,51)))
        plt.yticks(list(range(0,51)))

        # Set grid
        self.ax1.grid()
        plt.show()


    def setup_plot(self):
        """
        Sets up the plot
        """
        self.fig, self.ax1 = plt.subplots(1)

    def output(self):
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

            pprint(data)

            break


if __name__ == "__main__":
    batteries = access_data('district-1_batteries.csv')

    houses = access_data('district-1_houses.csv')

    true_grid = Grid(houses, batteries)

    print(true_grid.count_objects())
