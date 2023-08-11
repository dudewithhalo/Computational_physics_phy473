'''random walk on a grid where body is independent to move in
either of x and y axis with each alterations(increment/decrement)
being registered as dx and dy
'''

import random

def random_walk_2d(n):
    x, y = 0, 0

    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    print(f"Step is at {[x,y]}")
    return (x,y)

number_of_walk = int(input("Number of walk : "))
walk_length = int(input("How long will be the walk : "))

for i in range(number_of_walk):
    walk = random_walk_2d(walk_length)
    print(walk, f"Distance from start : {abs(walk[0]) + abs(walk[1])}\n")
