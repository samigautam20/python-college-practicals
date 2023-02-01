file_name = input("Enter the file name: ")
word_to_search = input("Enter the word to search for: ")

try:
    with open(file_name, 'r') as f:
        text = f.read()
        word_count = text.count(word_to_search)
        print("The word '{}' appears {} times in the file.".format(word_to_search, word_count))
except:
    print("Error reading the file.")