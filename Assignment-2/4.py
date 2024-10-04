# Create a function print_details that accepts keyword arguments and prints them in the format: "key: value". Test the function with different sets of keyword arguments.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
print_details(course="Computer Science", year=2024)
print_details(product="Laptop", price=1200, brand="Dell")
print_details()  # No keyword arguments

