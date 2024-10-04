# Create a dictionary with at least 5 key-value pairs. Write a Python program to:
# Add a new key-value pair to the dictionary.
# Update an existing key with a new value.
# Delete a key-value pair from the dictionary.

my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'profession': 'Engineer',
    'hobby': 'Painting'
}

print("Original Dictionary:", my_dict)

my_dict['country'] = 'USA'
print("After adding a new key-value pair:", my_dict)

my_dict['age'] = 31
print("After updating the 'age' key:", my_dict)

del my_dict['hobby']
print("After deleting the 'hobby' key:", my_dict)
