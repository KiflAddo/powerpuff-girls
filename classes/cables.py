import random

class Cables():
    '''class for cables'''
    def __init__(self):
        self.coordinates_list = []
        self.connected = False

    def step(self, x, y):
        x = int(x)
        y = int(y)

        direction = random.randint(1, 4)

        if self.coordinates_list:
            last_point_x = self.coordinates_list[-1][0]
            last_point_y = self.coordinates_list[-1][1]
        else:
            last_point_x = x
            last_point_y = y

        #Right
        if direction == 1 and x < 10 and last_point_x != x + 1:
            x = x + 1
            y = y

        #Left
        elif direction == 2 and x > 0 and last_point_x != x - 1:
            x = x - 1
            y = y

        #Up
        elif direction == 3 and y < 10 and last_point_y != y + 1:
            x = x
            y = y + 1

        #Down
        elif direction == 4 and y > 0 and last_point_y != y - 1:
            x = x
            y = y - 1

        coordinates = (x, y)

        self.coordinates_list.append(coordinates)
