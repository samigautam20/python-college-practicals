from random import shuffle
# Create a list of cars
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan", "Mazda"]

# Add some cars to the list
cars.append("Ferrari")
cars.append("Lamborghini")

# Delete some cars from the list
cars.remove("Toyota")
cars.remove("Honda")

# Print the list of cars
print("Original List: ", cars)

# Shuffle the list of cars
shuffle(cars)

# Print the shuffled list of cars
print("Shuffled List: ", cars)

# Remove some cars from the list
cars.pop(0)
cars.pop(1)

# Print the list after removing some cars
print("List after removing some cars: ", cars)

# Shuffle the list of cars
shuffle(cars)
# Print the final shuffled list of cars
print("Final shuffled List: ", cars)
