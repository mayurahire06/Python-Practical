# Create a simple calculator that allows the user to input two numbers and an operator (+, -, *, /, %, **, //). Based on the operator provided,
#  the program should perform the corresponding arithmetic operation and display the result.

def cal(op, n1, n2):
    return eval(f"{n1} {op} {n2}")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %, **, //): ")

result = cal(operator, num1, num2)
print(f"Result: {result}")
