# Write a Python program that:
# Asks the user for the name of a source file (e.g., source.txt) and a destination file (e.g., destination.txt).
# Copies the content of the source file to the destination file.

def copy_file_content(source_file, destination_file):
    with open(source_file, 'r') as infile:
        content = infile.read()
    
    with open(destination_file, 'w') as outfile:
        outfile.write(content)
    
    print(f"Content copied from '{source_file}' to '{destination_file}'.")

def get_file_name(prompt):
    return input(prompt)

source_file = get_file_name("Enter the name of the source file (e.g., source.txt): ")
destination_file = get_file_name("Enter the name of the destination file (e.g., destination.txt): ")

copy_file_content(source_file, destination_file)
