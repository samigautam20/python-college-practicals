def sort_words_in_file(file_name):
    try:
        with open(file_name, 'r') as f:
            words = f.readlines()
            words.sort()
    except IOError:
        print("Error reading the file.")
        return
    try:
        with open("sorted_"+file_name, 'w') as f:
            for word in words:
                f.write(word)
    except IOError:
        print("Error creating the new file.")

file_name = input("Enter the file name: ")
sort_words_in_file(file_name)