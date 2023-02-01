# Import the module to handle exceptions
import sys

def calculate_factorial(number):
    """
    Calculates the factorial of a given number
    """
    # Initialize the factorial to 1
    factorial = 1

    # Loop through the range from 1 to the given number
    for i in range(1, number + 1):
        # Multiply the factorial with the current iteration number
        factorial *= i
    
    # Return the calculated factorial
    return factorial

# Prompt the user for a number
try:
    number = int(input("Enter a number: "))
    # Calculate the factorial of the given number
    result = calculate_factorial(number)
    print("The factorial of", number, "is", result)
except ValueError:
    print("Error: You must enter an integer.")
    sys.exit(1)