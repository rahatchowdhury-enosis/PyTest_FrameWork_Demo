from src.library import LibraryAccount
from src.calculator import Calculator

class User:
    def __init__(self, username, balance=0):
        self.username = username
        self.balance = balance
        self.account = LibraryAccount(username)
        self.calculator = Calculator()

    def add_funds(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance = self.calculator.add(self.balance, amount)

    def pay_fee(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance = self.calculator.subtract(self.balance, amount)
