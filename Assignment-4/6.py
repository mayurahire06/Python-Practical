# Write a lambda function that checks if a number is even. Use this lambda with the filter() function to filter out even numbers from the following list:    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = lambda x: x % 2 == 0

even_numbers = list(filter(is_even, numbers))

print(even_numbers)
