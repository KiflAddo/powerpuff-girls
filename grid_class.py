class Grid():
    def __init__(self, house_data, battery_data):
        self.house_data = house_data
        self.battery_data = battery_data
        self.houses = []
        self.batteries = []
        self.add_houses()
        self.add_batteries()


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
