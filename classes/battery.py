"""
Battery class
"""
import random

class Battery():
    def __init__(self, pos_x, pos_y, pos_x_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_y = pos_x_y
        self.capacity = capacity
        self.used_capacity = 0
        self.full = False
        # self.bat_coords = []
