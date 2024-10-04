# Write a Python program that takes two numbers as input and compares them. Print whether the first number is greater than, 
# less than, or equal to the second number.


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater than the second number.")
elif num1 < num2:
    print("The first number is less than the second number.")
else:
    print("The first number is equal to the second number.")
