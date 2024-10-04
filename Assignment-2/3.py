# Write a Python function sum_numbers that takes a variable number of arguments and returns their sum. Test the function with different numbers of arguments.

def sum_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print("Sum of numbers:", sum_numbers(1, 2, 3))           
print("Sum of numbers:", sum_numbers(5, 10, 15, 20))     
print("Sum of numbers:", sum_numbers(0))                  
print("Sum of numbers:", sum_numbers(2.5, 3.5, 4.0))     
print("Sum of numbers:", sum_numbers())                   
