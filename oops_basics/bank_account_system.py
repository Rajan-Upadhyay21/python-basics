# ---------------------------------------------------------
# Program: Bank Account System
# Description:
# This program demonstrates encapsulation and object-based
# operations like deposit, withdraw, and balance checking.
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Current Balance:", self.__balance)

    def display_account_info(self):
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)


account1 = BankAccount("ACC1001", "Rajan", 5000)

account1.display_account_info()
account1.check_balance()
account1.deposit(2000)
account1.withdraw(1500)
account1.check_balance()
