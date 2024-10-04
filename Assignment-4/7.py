# Write a Python program that removes the duplicate values from the list using a set.
# Convert the set back into a list.
# List=> numbers = [1, 2, 2, 3, 4, 4, 5]

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers_set = set(numbers)

unique_numbers_list = list(unique_numbers_set)

print(unique_numbers_list)

