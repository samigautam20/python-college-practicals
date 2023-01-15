def temperature():
 temp=float(input("Please enter your temperture in Celsius: "))
 if temp==37.0 :
  print("You have a normal temperature.")
 elif temp<37.0 :
  print("Your temperature is low")
 else:
  print("You have a fever.")
temperature()