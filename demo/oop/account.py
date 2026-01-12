class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return  f'Insufficient Balance! Available for withdraw is :{self.balance}, withdraw amount is : {self.amount}'


class Account:
    # class attributes or static attributes
    minbal = 5000

    @staticmethod   # decorator
    def getminbal():
        return Account.minbal

    def __init__(self, acno, customer, balance):
        #object attributes
        self.acno = acno
        self.customer = customer
        if balance >= Account.minbal:
             raise ValueError(f"Invalid Balance! It must be >= {Account.minbal}")
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Invalid Amount. It must be > 0')

        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceError(self.balance - Account.minbal, amount)

    def getbalance(self):
        return self.balance

    def __str__(self):
        return f"{self.acno}, {self.customer}, {self.balance}"

    def __eq__(self, other):
        return self.acno == other.acno

    def __gt__(self, other):
        return self.balance > other.balance


print(Account.getminbal())  # call static method

a1 = Account(1, "Scott", 10000)
a1.deposit(5000)
try:
    a1.withdraw(20000)
    print(a1.getbalance())
except InsufficientBalanceError as e:
    print(e)

a2 = Account(2, "Barry", 10000)
a2.withdraw(2000)
print(a2.getbalance())
