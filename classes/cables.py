import random

class Cables():
    '''class for cables'''
    def __init__(self):
        self.coordinates_list = []
        self.connected = False

    def step(self, x, y):

        direction = random.randint(1, 4)

        last_point_x = self.coordinates_list[len(coordinates_list)][0]
        last_point_y = self.coordinates_list[len(coordinates_list)][1]

        #Right
        if direction == 1 and x < 50 and last_point_x != x + 1:
            x = x + 1
            y = y
        #Left
        if direction == 2 and x > 0 and last_point_x != x - 1:
            x = x - 1
            y = y
        #Up
        if direction == 3 and y < 50 and last_point_y != y + 1:
            x = x
            y = y + 1
        #Down
        if direction == 4 and y > 0 and last_point_y != y - 1:
            x = x
            y = y - 1

        coordinates = (x, y)

        self.coordinates_list.append(coordinates)
