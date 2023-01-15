import random
print("Welcome to the game!")
def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Your number is too low!")
        else:
            print("Your number is too high!")
        
        if attempts == 5:
            print("Ooopsieee! you reached the maximum number of attempts.")
            guess_again = input("Do you want to play again? (yes/no) ")
            if guess_again.lower() == "yes":
                guessing_game()
            else:
                print("Thank you for playing!")


guessing_game()
