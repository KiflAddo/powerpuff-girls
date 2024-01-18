import random

class Cables():
    '''class for cables'''
    def __init__(self, x, y):
        self.coordinates_list = []
        # pos_x_y = x, y
        # self.coordinates_list.append(pos_x_y)
        self.connected = False

    # def step(self):
    #
    #     direction = random.randint(1, 4)
    #
    #     last_point_x = self.coordinates_list[-1][0]
    #     last_point_y = self.coordinates_list[-1][1]
    #
    #
    #     #Right
    #     if direction == 1 and last_point_x < 10 and last_point_x != last_point_x + 1:
    #         new_x = last_point_x + 1
    #         new_y = last_point_y
    #
    #     #Left
    #     elif direction == 2 and last_point_x > 0 and last_point_x != last_point_x - 1:
    #         new_x = last_point_x - 1
    #         new_y = last_point_y
    #
    #     #Up
    #     elif direction == 3 and last_point_y < 10 and last_point_y != last_point_y + 1:
    #         new_x = last_point_x
    #         new_y = last_point_y + 1
    #
    #     #Down
    #     elif direction == 4 and last_point_y > 0 and last_point_y != last_point_y - 1:
    #         new_x = last_point_x
    #         new_y = last_point_y - 1
    #
    #     else:
    #         new_x = last_point_x
    #         new_y = last_point_y
    #
    #     coordinates = (new_x, new_y)
    #
    #     self.coordinates_list.append(coordinates)
