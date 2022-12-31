# Importing  sqrt function from the math module
from math import sqrt

# Geting the distance 
distance_to_shadow = float(input("Enter the distance between the observer and the shadow: "))
perpendicular_distance = float(input("Enter the perpendicular distance between the bird and its shadow: "))

# Calculating the total distance between the bird and the observer using the height and distance formula
total_distance = sqrt(distance_to_shadow**2 + perpendicular_distance**2)

# Printing the result
print("The total distance between the bird and the observer is", total_distance, "meters")
print("Sami Gautam")