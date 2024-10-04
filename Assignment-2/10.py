# Write a Python program to create a list with 10 elements. Perform the following operations:
# Append a new element to the list.
# Insert an element at the third position.
# Remove an element from the list.
# Sort the list in ascending order.


my_list = [10, 5, 8, 3, 15, 1, 7, 12, 6, 9]

print("Original List:", my_list)

my_list.append(20)
print("After appending 20:", my_list)

my_list.insert(2, 11)
print("After inserting 11 at the third position:", my_list)

my_list.remove(5)
print("After removing 5:", my_list)

my_list.sort()
print("After sorting the list in ascending order:", my_list)
