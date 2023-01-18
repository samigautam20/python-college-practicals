#author- Sami Gautam
#importing string module which is used to define the variable "charctr" as a concatenation of the string of uppercase letters from the ASCII character set
import string
charctr = string.ascii_uppercase + string.ascii_uppercase

#defining users which greets the user and explains the purpose of program.
def welcome():
    print('Welcome to the Caesar Cipher')
    print("This program encrypts and decrypts text with the Casesar Cipher.")

#defining a function to prompt the user to choose whether they want to encrypt or decrypt a message
def enter_message():
    while True:
        user = input("Would you like to encrypt (enc) or decrypt (dec):")
        if user == 'enc':
            encrypt()
            break
        elif user == 'dec':
            decrypt()
            break
        else:
            print("Invalid Mode")
            continue

#function to encrypt by shifting the letters of input message 
def encrypt():
    encrypt = list(input("What message would you like to encrypt: ").upper())
    while True:
        shift = input("What is the shift number: ")
        if shift.strip().isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift")
            continue
    for i in range(len(encrypt)):
        if encrypt[i] == ' ':
            encrypt[i] == ' '
        else:
            var = charctr.index(encrypt[i]) + shift
            encrypt[i] = charctr[var]
    print(''.join(map(str, encrypt)))

#defining function to decrypt the input message
def decrypt():
    decrypt = list(input("What message would you like to decrypt: ").upper())
    while True:
        shift = input("What is the shift number: ")
        if shift.strip().isdigit():
            shift = int(shift)
            break
        else:
            print("Invalid shift")
            continue
    for i in range(len(decrypt)):
        if decrypt[i] == ' ':
            decrypt[i] = ' '
        else:
            var = charctr.index(decrypt[i]) - shift
            decrypt[i] = charctr[var]
    print(''.join(map(str, decrypt)))

#calling the functions defined above as welcome and enter_message
welcome()
enter_message()

#validating the program, whether the user wants to continue or end the program
#if the user wants to end the program, it displays a thank you message
while True:
    again = input("Would you like to encrypt or decrypt another message? (Y/N): ")
    if again == 'Y':
        enter_message()
    elif again == 'N':
        print("Thank you for using the program, bye bye!")
        break
    else:
        continue
#the program ends here