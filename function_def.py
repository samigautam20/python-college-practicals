def types(val):
    print("As a float: ", float(val))
    print("As an integer: ", int(val))
def squared(val):
    return val**2
def int_to_string(val):
    return str(val)
def hello_world(name):
    print("Hello World, my name is " + name)
def print_ast(n, symbol="*"):
    print(symbol * n)
from statistics import mean, median, mode

def improved_average(n1, n2, n3, n4, n5):
    nums = [n1, n2, n3, n4, n5]
    return mode(nums), median(nums), mean(nums)
def either_side(val):
    print("You typed {0}, one less than {0} is {1}, one more than {0} is {2}".format(val,val-1,val+1))
