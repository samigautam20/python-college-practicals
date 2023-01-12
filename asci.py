def next_char(char):
    next_char_num = ord(char) + 1
    next_char = chr(next_char_num)
    return next_char

user_input = input("Enter a character: ")
print("The next character in alphabetical order is: " + next_char(user_input))
print('Sami gautam')