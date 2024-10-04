# Write a Python program that reads a text file and counts how many times each word appears in the file. The program should display the word frequency in descending order.

def count_word_frequency(file_name):
    with open(file_name, 'r') as file:
        text = file.read()

    words = text.split()
    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    for word, count in sorted_word_count:
        print(f"{word}: {count}")

def get_file_name():
    return input("Enter the name of the text file (e.g., input.txt): ")

file_name = get_file_name()
count_word_frequency(file_name)
