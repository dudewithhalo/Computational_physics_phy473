'''
Write a set of python statements to insert an integer (taken from input)
into a list A=[12,18,1,5,6,10]
and then delete the n
th element from the updated list A. Print the final list as an output.

The integer (needs to be inserted) and n
should be taken as input from the keyboard. The input contains two lines.
The first and second lines contain the integer to be inserted in the list and n respectively.

Example:
Input:
1
3

Output:
[12, 18, 1, 6, 10, 1]
'''

i = int(input())
n = int(input())

A = [12,18,1,5,6,10]

A.append(i)


A.pop(n)
print(A)
