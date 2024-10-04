# Use round() inside map() to round a list of floating-point numbers to 1 decimal place.
# Example: round_to_one([3.14159, 2.71828, 1.61803]) should return [3.1, 2.7, 1.6].


def round_to_one(numbers):
    round_one = lambda x: round(x, 1)
    return list(map(round_one, numbers))

result = round_to_one([3.14159, 2.71828, 1.61803])
print(result) 
