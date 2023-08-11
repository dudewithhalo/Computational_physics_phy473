'''random walk in a city where a body can go in either
direction of North,South,East or West
'''

import random

def random_walk_in_citygrid(n):
    x, y = 0, 0

    for i in range(n):
        step = random.choice(['N','S','E','W'])
        print(f"Step is {step}")

        if step == 'N':
            y = y+1
        elif step == 'E':
            x = x+1
        elif step == 'W':
            x = x-1
        else:
            y = y-1

    return (x,y)

number_of_walk = int(input("Number of walk : "))
walk_length = int(input("How long will be the walk : "))

for i in range(number_of_walk):
    walk = random_walk_in_citygrid(walk_length)

    print(walk, f"Distance from start : {abs(walk[0] + abs(walk[1]))} \n")

        
