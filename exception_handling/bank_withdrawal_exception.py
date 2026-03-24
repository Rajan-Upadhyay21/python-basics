# ---------------------------------------------------------
# Program: Bank Withdrawal Exception Example
# Description:
# This program simulates a bank withdrawal system and raises
# an exception if the withdrawal amount exceeds balance.
# ---------------------------------------------------------

class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount is greater than balance."""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance for withdrawal.")
    return balance - amount


try:
    account_balance = 5000
    withdrawal_amount = 7000

    remaining_balance = withdraw(account_balance, withdrawal_amount)
    print("Withdrawal successful.")
    print("Remaining balance:", remaining_balance)

except InsufficientBalanceError as error:
    print("Transaction Error:", error)
