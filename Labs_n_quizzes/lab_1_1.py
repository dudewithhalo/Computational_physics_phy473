'''
Write a python program that takes a decimal number (float) as input and print the
number up to two decimal places as an output.

Example:
INPUT:
1234.678968

OUTPUT:
1234.68'''

x = float(input("Enter the number : "))
print(f"{x:0.2f}")
