user=int(input('What is your credit score: '))
if user>= 90:
    print("Senior Status")
elif user>=30 and user<60:
    print("Junior")
elif user>=60 and user<90:
    print("Sophomore")
else:
    print("join the college!")
print("Sami Gautam")