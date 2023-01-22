class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def bark(self):
        print("Woof Woof!")

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
dog1=Dog("Fido",3)
print(dog1.get_name())
dog1.bark()
print(dog1.get_age())