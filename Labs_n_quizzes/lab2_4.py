'''
Write a set of python statements that create a NumPy array using the linspace
function of python. The start and end elements should be taken as input from
the keyboard along with the number of points between the elements.

The input contains three lines. The first and the second lines contain the
start and the end elements for the linspace function. The last line contains
the number of points used to create the array.

Example:
Input:
20
34
5

Output:
[20.  23.5 27.  30.5 34. ]'''

import numpy as np

#registering input from the user
start = int(input())
end = int(input())
step = int(input())

A = np.linspace(start,end,step)

print(A)
