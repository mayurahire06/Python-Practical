# Write a Python program to reverse a given string without using built-in functions. For example, input "hello" should return "olleh".

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string)):
        reversed_string = input_string[i] + reversed_string
    return reversed_string

input_str = "hello"
result = reverse_string(input_str)
print("Reversed string:", result)  # Expected output: "olleh"
