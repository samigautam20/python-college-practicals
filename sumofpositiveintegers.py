total = 0
while True:
    num = int(input("Enter a positive integer (0 to exit): "))
    if num == 0:
        break
    if num > 100:
        continue
    total += num

print("The total of the entered numbers is:", total)
print("Sami Gautam")