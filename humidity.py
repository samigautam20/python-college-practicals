temp=int(input("Enter current temperature: "))
humidity=int(input("Enter current humidity: "))
if temp >=85 and humidity > 60:
    print('muggy day today')
elif temp >=85:
    print('warm, but not muggy today')
elif temp>=65:
    print('Pleasant today')
elif temp<=45:
    print('cold today')
else:
    print('Cold today')
print('Sami Gautam')