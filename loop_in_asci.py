def next_char(char):
    if ord(char)>=97 and ord(char)<=122:
        next_char_num = ord(char) + 1
        next_char = chr(next_char_num)
        return next_char
    else:
        return "Invalid input"
    
while True:
    user_input = input("Enter a character: ")
    result = next_char(user_input)
    print("The next character in alphabetical order is: " + result)
    choice = input("Do you want to continue? Press Y or y for Yes and any other key for No: ")
    if choice.lower() != 'y':
        break
