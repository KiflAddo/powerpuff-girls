import matplotlib.pyplot as plt
from pprint import pprint
import re

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

        self.setup_plot()
        self.visualize()

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
        # plt.figure(figsize=(50, 50))
        #{value for value in variable}self.ax1.axis([0, 50, 0, 50])

        # plot houses
        x_pos_list = []
        y_pos_list = []

        for house in self.houses:
            x_pos_list.append(int(house.pos_x))
            y_pos_list.append(int(house.pos_y))

        # plot batteries
        x_pos_list_bat = []
        y_pos_list_bat = []
        colour_bat = []

        for battery in self.batteries:
            x_pos_list_bat.append(int(battery.pos_x))
            y_pos_list_bat.append(int(battery.pos_y))
            colour_bat.append('r')

        # print(x_pos_list)
        # print(y_pos_list)
        # print(x_pos_list_bat)
        # print(y_pos_list_bat)

        # print(x_pos_list)
        self.ax1.scatter(x_pos_list, y_pos_list)
        self.ax1.scatter(x_pos_list_bat, y_pos_list_bat, c=colour_bat)

        plt.xticks(list(range(0,51)))
        plt.yticks(list(range(0,51)))
        
        # x_ticks = [i * 10 for i in list(range(0,6))]
        # print(x_ticks)


        # plt.setp(self.ax1.get_xticklabels(), visible=False)
        # plt.setp(self.ax1.get_xticklabels()[::10], visible=True)
        # plt.set_xticks(labels=x_ticks)

        self.ax1.grid()
        # self.ax1.minorticks_on()
        # plt.tight_layout()
        plt.show()



    def setup_plot(self):
        """
        Sets up the plot
        """
        self.fig, self.ax1 = plt.subplots(1)
        # self.ax1.set_aspect('equal')
        # self.ax1.axes.get_xaxis().set_visible(True)
        # self.ax1.axes.get_yaxis().set_visible(True)





if __name__ == "__main__":
    batteries = access_data('district-1_batteries.csv')

    houses = access_data('district-1_houses.csv')

    true_grid = Grid(houses, batteries)

    print(true_grid.count_objects())
