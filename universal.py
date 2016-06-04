from account import Account


class UniversalBank:
	def __init__(self):
		self.account = Account(1000, 0)
		self.scenarios = []
