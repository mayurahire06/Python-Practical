# Create a function greet(name, msg="Hello") that prints a greeting message. If msg is not provided, it should default to "Hello". Test the function with different arguments.

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")
greet("Bob", "Good morning")
greet("Charlie", "Welcome")
greet("Dana")
