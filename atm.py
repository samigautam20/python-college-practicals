print("Welcome to our bank management system ")
class atm:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} has been added to your account.")
        print(f"Your current amount is{self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account.")
        else:
            print("Insufficient funds.")
        print(f"Your current balance is {self.balance}")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

opening=input("Do you want to create a new account?(Y/N)" )
if opening=='Y':
    name=input("Enter your name here: ")
    age=input("Enter your age: ")
    address=input("Enter your address: ")
    
    account=atm(name,age,address)
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using our services.")
            break
        else:
            print("Invalid choice, Please enter valid choice.")
else:
    print("Thank you for visiting us.")
        