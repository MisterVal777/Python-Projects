#importing abstract method form the abc module
from abc import ABC, abstractmethod
# class named coffee utilizing abstraction
class coffee(ABC):
	def charge(self, amount):
		print("Your coffee charge amount: ",amount)
# this functioin tells to pass in an argument hiding the how using abstraction
	@abstractmethod	
	def lightning(self, amount):
		pass

class StrikePayment(coffee):
# implementing the payment function from its parent lightning class.
	def lightning(self, amount):
		print('Your purchase amouont of {} has earned you Strike credit points '.format(amount))

obj = StrikePayment()
obj.charge(".00007500 Sats")
obj.lightning(".00007500 Sats")
