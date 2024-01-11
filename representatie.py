import matplotlib.pyplot as plt
from pprint import pprint

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
            split_data = battery.split(',')
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
        self.ax1.axis([0, 60, 0, 60])

        # plot houses
        x_pos_list = []
        y_pos_list = []

        for house in self.houses:
            x_pos_list.append(house.pos_x)
            y_pos_list.append(house.pos_y)

        # plot batteries
        x_pos_list_bat = []
        y_pos_list_bat = []
        colour_bat = []

        for battery in self.batteries:
            x_pos_list_bat.append(battery.pos_x)
            y_pos_list_bat.append(battery.pos_y)
            colour_bat.append('r')

        # print(x_pos_list)
        # print(y_pos_list)
        print(x_pos_list_bat)
        print(y_pos_list_bat)

        # print(x_pos_list)
        self.ax1.scatter(x_pos_list, y_pos_list)
        self.ax1.scatter(x_pos_list_bat, y_pos_list_bat, c=colour_bat)
        plt.show()

        # pass

    def setup_plot(self):
        """
        Sets up the plot
        """
        self.fig, self.ax1 = plt.subplots(1)
        self.ax1.set_aspect('equal')
        self.ax1.axes.get_xaxis().set_visible(True)
        self.ax1.axes.get_yaxis().set_visible(True)





if __name__ == "__main__":
    batteries = access_data('district-1_batteries.csv')

    houses = access_data('district-1_houses.csv')

    true_grid = Grid(houses, batteries)

    print(true_grid.count_objects())
