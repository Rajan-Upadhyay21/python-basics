# ---------------------------------------------------------
# Program: Encapsulation Example
# Description:
# This program demonstrates encapsulation using private
# variables and getter/setter methods.
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rajan", 5000)

account.deposit(1500)
print("Current Balance:", account.get_balance())
