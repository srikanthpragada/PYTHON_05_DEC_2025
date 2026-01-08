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
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            print('Insufficient Balance!')

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
a1.withdraw(2000)
print(a1.getbalance())

a2 = Account(2, "Barry", 5000)
a2.withdraw(2000)
print(a2.getbalance())
