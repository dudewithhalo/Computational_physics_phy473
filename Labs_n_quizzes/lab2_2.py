'''
Write a set of python statements that print a sliced part of an array A=[10,a,12,b,89,c]
. The values of a
, b
, c
, and the slicing indices should be taken as input from the keyboard.

The input contains five lines. The first, second, and third lines contain the values of a
, b
, and c
 respectively. The last two lines contain the slicing indices (start index, end index).

Note: 1) All inputs should be taken as integers.
      2) Step is 1 between the start and end slice indices in this problem.


Example:
Input:
1
2
3
1
4

Output:
[ 1 12  2]
'''

import numpy as np

#registering input from the user
a = int(input())
b = int(input())
c = int(input())
start_index = int(input())
end_index = int(input())

A = np.array([10,a,12,b,89,c])

print(f"{A[start_index:end_index]}")
