from decimal import Decimal

# class for user
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

# class for expense
class Expense:
    def __init__(self, exp_id, description, amt, paid_by):
        self.exp_id = exp_id
        self.description = description
        self.amt = amt
        self.paid_by = paid_by


        