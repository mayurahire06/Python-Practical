# Write a Python program that:
# Reads the content of a file named input.txt.
# Writes the reversed content to another file named reversed.txt.

import os

def reverse_file_content(input_file, output_file):
    if os.path.exists(input_file):
        with open(input_file, 'r') as infile:
            content = infile.read()  # Read the entire content of the file
        
        reversed_content = content[::-1]  # Reverse the content
        
        with open(output_file, 'w') as outfile:
            outfile.write(reversed_content)  # Write the reversed content to the output file

        print(f"The content has been reversed and saved to '{output_file}'.")
    else:
        print(f"Error: The file '{input_file}' does not exist.")

def get_input_file_name():
    return input("Enter the name of the input file (e.g., input.txt): ")

input_file = get_input_file_name()
output_file = 'reversed.txt'

reverse_file_content(input_file, output_file)
