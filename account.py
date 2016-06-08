class Account:
    def __init__(self, funds, interest_rate):
        self.funds = funds
        self.interest_rate = interest_rate

    @property
    def has_funds(self):
        return self.funds > 0

    def can_afford(self, price):
        return self.funds >= price

    def add_funds(self, amount):
        self.funds += amount

    def take_funds(self, amount):
        self.funds -= amount


