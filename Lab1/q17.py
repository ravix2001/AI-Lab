# Create a class BankAccount with private attributes balance and account_number. Implement methods deposit() and withdraw() to modify the balance. Ensure that the balance cannot be accessed directly from outside the class

import os

os.system('cls')

class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # double underscore prefix (__) makes Private attribute
        self.__balance = initial_balance        # double underscore prefix (__) makes Private attribute

    def deposit(self):
        amount = float(input("Enter the amount to be deposited : "))
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs.{amount}. New balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn : "))
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn Rs.{amount}. New balance: Rs.{self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        # Provides a way to check balance without direct access
        return self.__balance

account = BankAccount("123456789", 1000)

account.deposit()
account.withdraw()
print(account.get_balance())

# Direct access to balance is not allowed
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
