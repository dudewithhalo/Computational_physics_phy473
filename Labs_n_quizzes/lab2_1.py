'''
Write a set of python statements to perform the sum [element-wise] of two arrays A=[1,2,3,4,5,a,b]
 and B=[6,8,c,d,9,12,20]
, and assign the output in an another array, C
. Print C
 as an output. The values of a
, b
, c
 and d
 should be taken as input from the keyboard.

Note: a
, b
, c
 and d
 are integers in this problem.

Example:
INPUT:
1
2
3
4

OUTPUT:
[ 7 10  6  8 14 13 22]
'''


import numpy as np

#registering input from the user
a = int(input())
b = int(input())
c = int(input())
d = int(input())

A = np.array([1,2,3,4,5,a,b])
B = np.array([6,8,c,d,9,12,20])

# adding the arrays elements wise
C = np.add(A,B)

print(C)
