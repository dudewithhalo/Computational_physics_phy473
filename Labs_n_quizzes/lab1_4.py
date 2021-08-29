'''
Write a python program that takes a three-digit positive integer as input
and remove the second digit from that number. Note that you need to print
the resultant two-digit positive integer, as an output from your program.

Example:

INPUT:
768

OUTPUT:
78
'''

x = (input("Enter number : "))
x_new = str(x[0]) + str(x[-1])
print(int(x_new))
