# Write a function that takes two lists and uses map() to return a list of the sums of corresponding elements.
# Example: add_lists([1, 2], [3, 4]) should return [4, 6].

def add_lists(list1, list2):
    return list(map(lambda x, y: x + y, list1, list2))

result = add_lists([1, 2], [3, 4])
print(result) 

