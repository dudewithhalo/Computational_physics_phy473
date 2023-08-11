# 2d Plotting


from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt


# define perimeters for walk

dims = 2
step_n = 10000
step_set = [-1,0,1]
origin = np.zeros((1,dims))

# simulating steps in 2D

step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin,steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

# plotting the path
fig = plt.figure(figsize = (8,8), dpi = 200)
ax = fig.add_subplot(111)

ax.scatter(path[:,0], path[:,1], c='blue',alpha=0.25,s=0.05)
ax.plot(path[:,0], path[:,1], c='blue',alpha=0.5,lw=0.5,ls='--')
ax.plot(start[:,0],start[:,1],c='red',marker="+")
ax.plot(stop[:,0],stop[:,1],c='black',marker = 'o')

plt.show()
