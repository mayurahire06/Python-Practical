# Write a Python script that:
# Creates a package math_operations with two modules: basic_operations.py and advanced_operations.py.
# The basic_operations.py module should contain functions for addition, subtraction, multiplication, and division.
# The advanced_operations.py module should contain functions for power and square root.
# Import these modules in a main script and demonstrate their usage.

from math_operations.basic_operations import add, subtract, multiply, divide
from math_operations.advanced_operations import power, square_root

print("Basic Operations:")
print("Addition (5 + 3):", add(5, 3))
print("Subtraction (10 - 4):", subtract(10, 4))
print("Multiplication (7 * 2):", multiply(7, 2))
print("Division (8 / 2):", divide(8, 2))
print("Division (8 / 0):", divide(8, 0))  


print("\nAdvanced Operations:")
print("Power (2^3):", power(2, 3))
print("Square Root (16):", square_root(16))
print("Square Root (-4):", square_root(-4)) 
