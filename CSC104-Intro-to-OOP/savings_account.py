from account import Account

class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)
#method overriding having  method in a parent class
#method overloading having a method with the same name in a calls with diff signatures
    def withdraw(self, amount):
        if amount < 2000:
            super().withdraw(amount)
        else:
            print("You cannot withdraw this amount")
savings = SavingsAccount()
savings.withdraw(3000)