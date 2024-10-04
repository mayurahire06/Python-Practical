# Write a Python program that takes an integer as input and determines if it is even or odd. Print the result.

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
