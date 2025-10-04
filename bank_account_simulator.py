class Account:

    def __init__(self, name, email, mobilephone):
        self.name = name
        self.email = email
        self.mobilephone = mobilephone
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} added to you balance")
        print(f"Balance: {self.balance}")

    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Unfortunately, you don't have enough money for this withdrawal!")
            print(f"Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from your account")
            print(f"Balance: {self.balance}")


    def check_balance(self,):
        print(f"Balance: {self.balance}")



account1 = Account("Mohamad Abbas", "its.hamodi2005@gmail.com", "0700000000")




while True:
    print("(1) for deposit (2) for withdraw (3) to check your balance (4) Exit\n")
    try:
        UserChoice = int(input("How can i help you:  "))
    except ValueError:
        print("Plese enter a number between 1, 2, 3 and 4")
        continue

    if UserChoice == 1:
        try:
            print("How much you want to deposit?\n")
            amount = int(input(""))
            account1.deposit(amount)
        except ValueError:
            print("Plese enter a number between 1, 2, 3 and 4")
            continue
        

    elif UserChoice == 2:
        try:
            print("How much you want to withdraw?\n")
            amount = int(input(""))
            account1.withdraw(amount)
        except ValueError:
            print("Plese enter a number between 1, 2, 3 and 4")
            continue

    elif UserChoice == 3:
        account1.check_balance()

    elif UserChoice == 4:
        break

    else:
        print("Plese enter a number between 1, 2, 3 and 4")