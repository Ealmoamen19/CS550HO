
class outOfBoundsError (Exception) :

	pass


class Card :

	def __init__ (self, suite, number) :

		suites = [1, 2, 3, 4, "Diamonds", "Hearts", "Spades", "Clovers"]

		self.suite = suites[suite + 3]

		if suite >= 5 :

			raise outOfBoundsError("Value out of bounds.")

		numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

		self.number = number

		self.rank = numbers[number + 12]

		if number > 13 or number < 1 :

			raise outOfBoundsError("Value out of bounds.")

	def __str__ (self) :

		return str(self.rank) + " of " + self.suite








