def __init__(self, x_house, y_house, x_battery, y_battery):
    self.coordinates_list = []
    # pos_x_y = x, y
    self.x_house = x_house
    self.y_house = y_house
    self.x_battery = x_battery
    self.y_battery = y_battery

    # self.coordinates.append(pos_x_y)
    self.connected = False

def step(self):
    # Determine how many steps we have to take on each axis. Negative means to
    # the left, positive means to the right
    x_steps = self.x_battery - self.x_house
    y_steps = self.y_battery - self.y_house

    # The positions that will be updated
    pos_h_x = self.x_house
    pos_h_y = self.y_house

    # Counting steps for x and y
    count_x = 0
    count_y = 0

    steps_needed = abs(x_steps)+abs(y_steps)

    # Take the right amount of steps
    while steps_needed > steps_taken:
        # Pick a random direction: 1=along x axis, 2=along y axis
        direction = random.randint(1, 2)

        if direction == 1 and count_x < abs(x_steps):
            # Check if the value is negative or positive
            if x_steps > 0:
                pos_h_x+=1
            elif x_steps < 0:
                pos_h_x -= 1

            steps_taken += 1
            count_x += 1

        if direction == 2 and count_y < abs(y_steps):
            # Check if the value is negative or positive
            if y_steps > 0:
                pos_h_y+=1
            elif y_steps < 0:
                pos_h_y -= 1

            steps_taken += 1
            count_y += 1

        # Save coordinate to list
        self.coordinates.append((pos_h_x, pos_h_y))

    print(self.coordinates)