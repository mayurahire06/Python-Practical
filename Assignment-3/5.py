# Create a function that rounds a list of numbers to the nearest whole number.
# Example: round_list([1.2, 2.5, 3.8]) should return [1, 3, 4].

def round_list(numbers):
    return [round(num) for num in numbers]

result = round_list([1.2, 2.5, 3.8])
print(result)  
