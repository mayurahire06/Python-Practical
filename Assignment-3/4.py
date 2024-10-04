# Write a function that imports your custom module (e.g., math_utils.py) and uses a function from it to calculate the factorial of a number.

from math_utils import factorial

number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
