'''
Write a python program that takes two complex numbers (whose real and imaginary
parts are integer) as inputs and performs multiplication of these two numbers.
You should print the real and imaginary parts separately after multiplication as the output.

The input will be of two lines. The first line will contain the first complex
number and the second line, the second complex number.
The output contains only one line with real and imaginary parts of the
multiplication of two complex numbers.

Example:
INPUT:
2+3j
1+2j

OUTPUT:
-4	 7
'''

x = complex(input("Enter number with spaces : "))
y = complex(input("Enter the second number : "))
z = (x*y)
print(f"Product : {z}")
print(f'Real part : {z.real}')
print(f'Imaginary part : {z.imag}')
