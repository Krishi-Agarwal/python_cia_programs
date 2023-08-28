from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance ):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    #balance = 0
    def __init__(self, balance, interest_rate):
        self.balance=balance
        try:
            super().__init__(self.balance)
        except:
            print()
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_fee):
        super().__init__(balance)
        self.overdraft_fee = overdraft_fee

    def deposit(self, amount):
        self.balance += amount
  
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_fee
            print("Insufficient funds")
            return
        self.balance -= amount

class StudentAccount(SavingsAccount, CheckingAccount):
    def __init__(self, balance, interest_rate, overdraft_fee):
        SavingsAccount.__init__(self,balance, interest_rate)
        CheckingAccount.__init__(self,balance, overdraft_fee)



accounts = [SavingsAccount(1000, 0.01), CheckingAccount(1000, 35), StudentAccount(1000, 0.01 ,35)]
for account in accounts:
    account.deposit(100)
    account.withdraw(200)
    print(f"{account.__class__.__name__} balance: {account.balance}")
