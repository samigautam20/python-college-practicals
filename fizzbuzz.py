user=int(input("Enter a number: "))
if user%3==0 and user%5==0:
    print('Fizzbizz')
elif user%3==0:
    print('Fizz')
elif user%5==0:
    print('Buzz')
else:
    print('Not divisible by5 nor 3')
print('Sami Gautam')