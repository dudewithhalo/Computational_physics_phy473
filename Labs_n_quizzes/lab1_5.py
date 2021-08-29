'''
A processor with N
cores performs M
floating-point operations per clock cycle. The average frequency of the processor is F
(GHz). Write a python program to estimate the peak FLOPS of the processor [in TFLOPS].


The input contains three lines. The first and second line contain values of N and
M and the last line contains the value of F
.

Example:
Input:
20
20
3
Output:
1.2

'''

N = int(input('Enter Processor count:'))
M = int(input('Enter flops per cycle : '))
F = float(input('Enter processor power : '))

T = ((N*F)*M)*1e-3 #put the proper formula inside the bracket

print(T)
