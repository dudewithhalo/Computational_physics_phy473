# using 2D plot

import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 5,3

x = np.linspace(-1,1,10)
y = x**2
y1 = x**3

plt.plot(x,y,'r--',label = r'$y=x^2$')
plt.plot(x,y1, lw=3, c='g', label = r'$y=x^3$')

plt.axhline(0,color='k')
# draws horizontal axis
plt.axvline(0,c='k')
# vertical axis

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.xlabel(r'$x$', fontsize = 20)
plt.ylabel(r'$y$', fontsize = 20)
plt.legend(loc=4)
plt.show()
