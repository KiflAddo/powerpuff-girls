"""
House class
"""

class House():
    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_y = (pos_x, pos_y)
        self.capacity = capacity
