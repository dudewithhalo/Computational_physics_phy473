'''
Write a set of python statements to print the factorial of a given integer.
Your code should take the integer as input from the keyboard.

Note: Use the python function, factorial from the math module,  to get factorial.

Example:
Input:
5

Output:
120
'''

import math

n = int(input())

print(f"{math.factorial(n)}")
