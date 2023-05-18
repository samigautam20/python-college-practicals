import numpy as np

# function to check if input is a valid number
def is_valid_number(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

# function to get valid input from user
def get_valid_input(prompt):
    while True:
        input_value = input(prompt)
        if is_valid_number(input_value):
            return float(input_value)
        else:
            print("Invalid input. Please enter a valid number.")

# prompt user for 9 values and populate them into a 3x3 matrix
A = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        A[i][j] = get_valid_input("Enter a value for row " + str(i+1) + " column " + str(j+1) + ": ")

# print created matrix
print("Matrix A:")
print(A)

# print determinant of matrix
print("Determinant of A: ", np.linalg.det(A))

# check if inverse exists and print it if it does
if np.linalg.det(A) != 0:
    print("Inverse of A:")
    print(np.linalg.inv(A))
else:
    print("A is singular, inverse does not exist")

# print A*A and A*A*A
print("A*A:")
print(np.dot(A,A))
print("A*A*A:")
print(np.dot(np.dot(A,A),A))

# count number of values in matrix that are >= 10
count = 0
for i in range(3):
    for j in range(3):
        if A[i][j] >= 10:
            count += 1
print("Number of values in matrix that are >= 10: ", count)