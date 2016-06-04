class Account:
	def __init__(self, funds, interest_rate):
		self.funds = funds
		self.interest_rate = interest_rate


	@property
	def has_funds(self):
		return self.funds > 0

my_account = Account(300, 0.1)
print my_account.has_funds
