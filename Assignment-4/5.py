# Write a lambda function that:
# Takes two arguments and returns Power of 1st arg by 2nd.
# Use this lambda function in the map() function to add corresponding elements of two lists:
# list1 = [1, 2, 3, 4]   list2 = [5, 6, 7, 8]


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

power_function = lambda x, y: x ** y

result = list(map(power_function, list1, list2))

print(result)
