from src.calculator import Calculator

class Transaction:
    def __init__(self, user):
        self.user = user
        self.calculator = Calculator()

    def charge_late_fee(self, fee_amount):
        self.user.pay_fee(fee_amount)
        return f"Late fee of {fee_amount} charged to {self.user.username}. New balance: {self.user.balance}"

    def add_funds(self, amount):
        """Add funds to user balance"""
        self.user.add_funds(amount)
        return f"{amount} added to {self.user.username}'s account. New balance: {self.user.balance}"