positive_count = 0
negative_count = 0

while True:
    number = int(input("Enter an integer value (Enter 0 to stop): "))
    if number == 0:
        break
    elif number > 0:
        positive_count += 1
    else:
        negative_count += 1

print("Number of positive integers entered:", positive_count)
print("Number of negative integers entered:", negative_count)