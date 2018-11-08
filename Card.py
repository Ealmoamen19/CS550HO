
class outOfBoundsError (Exception) :

	pass


class Card :

	def __init__ (self, suite, number) :

		suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

		self.flipped = False

		self.suite = suites[suite - 1]

		if suite > 4 :

			raise outOfBoundsError("Value out of bounds.")

		numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

		self.number = number

		self.rank = numbers[number - 1]

		if number > 13 or number < 1 :

			raise outOfBoundsError("Value out of bounds.")

	def __str__ (self) :


		if self.flipped == False :

			return str(self.rank) + " of " + self.suite

		else :

			return "Flipped Card"







