product = 1
num = int(input('Enter a number: '))
while num != 0:
 product *= num
 num = int(input('Enter another number or 0 to end: '))
print('Product:', product)