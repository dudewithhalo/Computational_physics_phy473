# plotting the starting and ending points

import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    '''a class to generate random walks'''

    def __init__(self, num_points = 5000):
        '''initialise attributes of a walk'''
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''calculate all the points in the walk'''

# keep taking steps until walk reaches desired length
        while len(self.x_values) < (self.num_points):

            # decide which direction to go and how far to go in
            # that direction

            x_direction = choice([1,-1])
            x_distance = choice ([0,1,2,3,4,5])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice ([0,1,2,3,4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# make a random walk
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # plot thep oints in the walk
    plt.style.use('classic')
    fig ,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers,
    cmap = plt.cm.Blues, edgecolors = 'none', s = 15)

    #emphasise the first and last points
    ax.scatter(0,0, c ='green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1] ,
    c = 'red', edgecolors = 'none', s = 100)
    plt.show()

    keep_running = input('Make another walk ? (y/n): ')
    if keep_running == 'n':
        break


# green for start
# red for finish
        
