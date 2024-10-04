# Write a Python program to take a list of 10 elements and slice it to create a sublist containing every second element.

# Taking input for a list of 10 elements
elements = []
for i in range(10):
    element = input(f"Enter element {i + 1}: ")
    elements.append(element)

# Creating a sublist containing every second element
sublist = elements[1::2]

# Displaying the original list and the sublist
print("Original list:", elements)
print("Sublist containing every second element:", sublist)
