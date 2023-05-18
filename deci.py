def divide():
    s=str(input("Enter your name:"))
    print("Welcome",s)
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("{} divided by {} is {:.2f}".format(num1, num2, result))
divide()
