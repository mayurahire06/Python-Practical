# write a menu driven program for file handling on functions like, open, write, read, writeline, readline, close, rename

import os

def open_file(filename, mode):
    try:
        return open(filename, mode)
    except FileNotFoundError:
        print("File not found.")
        return None

def write_to_file(file):
    if file:
        data = input("Enter text to write to the file: ")
        file.write(data + '\n')
        print("Data written successfully.")
    else:
        print("File is not open.")

def write_lines_to_file(file):
    if file:
        print("Enter lines of text (type 'STOP' to end):")
        while True:
            line = input()
            if line.upper() == 'STOP':
                break
            file.write(line + '\n')
        print("Lines written successfully.")
    else:
        print("File is not open.")

def read_file(file):
    if file:
        file.seek(0)
        print("Reading file content:")
        content = file.read()
        print(content)
    else:
        print("File is not open.")

def read_line_from_file(file):
    if file:
        line = file.readline()
        print("Reading one line from the file:")
        print(line)
    else:
        print("File is not open.")

def close_file(file):
    if file:
        file.close()
        print("File closed.")
    else:
        print("File is not open.")

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File renamed to {new_name}.")
    except FileNotFoundError:
        print("File not found.")

def main():
    file = None
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Write to File")
        print("3. Write Lines to File")
        print("4. Read File")
        print("5. Read One Line from File")
        print("6. Close File")
        print("7. Rename File")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            filename = input("Enter the filename to open: ")
            mode = input("Enter mode (r/w/a): ")
            file = open_file(filename, mode)

        elif choice == '2':
            write_to_file(file)

        elif choice == '3':
            write_lines_to_file(file)

        elif choice == '4':
            read_file(file)

        elif choice == '5':
            read_line_from_file(file)

        elif choice == '6':
            close_file(file)
            file = None

        elif choice == '7':
            old_name = input("Enter the old filename: ")
            new_name = input("Enter the new filename: ")
            rename_file(old_name, new_name)

        elif choice == '8':
            if file:
                close_file(file)
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
