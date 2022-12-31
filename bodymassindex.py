# Getting the weight and height from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# Calculating the BMI
bmi = weight / (height/100)**2

# Printing the result
print("Your BMI is", bmi)
print("Sami Gautam")