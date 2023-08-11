# 1d plot of Randow Walk
# starts from + red markers and end at black o marker

from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt


# define perimeters for walk

dims = 1
step_n = 10000
step_set = [-1,0,1]
origin = np.zeros((1,dims))

# simulating steps in 1D

step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size=step_shape)
path = np.concatenate([origin,steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

# plotting the path
fig = plt.figure(figsize = (8,4), dpi = 200)
ax = fig.add_subplot(111)

ax.scatter(np.arange(step_n+1), path, c='blue',alpha=0.25,s=0.05)
ax.plot(path, c='blue',alpha=0.5,lw=0.5,ls='--')
ax.plot(0,start,c='red',marker="+")
ax.plot(step_n,stop,c='black',marker = 'o')

plt.show()
