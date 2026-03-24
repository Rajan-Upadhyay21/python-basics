# ---------------------------------------------------------
# Program: Transaction Processor
# Description:
# This program simulates a transaction system and handles
# multiple kinds of exceptions during validation and
# processing of payments.
# ---------------------------------------------------------

class InvalidAmountError(Exception):
    pass

class PaymentFailedError(Exception):
    pass


def process_transaction(account_name, balance, amount):
    print("Processing transaction for:", account_name)

    if amount <= 0:
        raise InvalidAmountError("Transaction amount must be greater than zero.")

    if amount > balance:
        raise PaymentFailedError("Transaction failed due to insufficient funds.")

    balance -= amount
    return balance


try:
    user_name = "Rajan"
    available_balance = 3000
    purchase_amount = 4500

    remaining_balance = process_transaction(user_name, available_balance, purchase_amount)

    print("Transaction successful.")
    print("Remaining balance:", remaining_balance)

except InvalidAmountError as error:
    print("Amount Error:", error)

except PaymentFailedError as error:
    print("Payment Error:", error)

except Exception as error:
    print("Unexpected Error:", error)

finally:
    print("Transaction process finished.")
