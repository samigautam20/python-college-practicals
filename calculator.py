def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def trunc_divide(num1, num2):
    return num1 // num2

def modulus(num1, num2):
    return num1 % num2

def exponentiation(num1, num2):
    return num1 ** num2
def help():
    print("add(num1,num2)")
    print("subtract(num1,num2)")
    print("multiply(num1,num2)")
    print("divide(num1,num2)")
    print("trunc_divide(num1,num2)")
    print("modulus(num1,num2)")
    print("exponentiation(num1,num2)")

result = add(4.2, 3.1)
print(result)
result=subtract(6,4)
print(result)
result=multiply(4,5)
print(result)
result=divide(6,7)
print(result)
result=trunc_divide(8,8)
print(result)
result=modulus(2,4)
print(result)
result=exponentiation(8,9)
print(result)

help()