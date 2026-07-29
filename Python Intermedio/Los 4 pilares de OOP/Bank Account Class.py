class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal successful. New balance: ${self.balance}")


class SavingsAccount(BankAccount):

    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Error: Balance cannot go below the minimum balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: ${self.balance}")


account = SavingsAccount(1000, 200)

account.deposit(300)      
account.withdraw(500)     
account.withdraw(700)    #error