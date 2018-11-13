from Deck import Deck

from Card import Card

class Player :

	def __init__ (self, name) :

		self.name = name

		self.hand = Deck(False)

		self.rounds = 0

	def __str__ (self) :

		printer = "\nName: " + self.name + "\nHand:" 

		for i in range(0, len(self.hand.deck)) :

			printer += "\n"

			printer += str(i + 1) + ") " + str(self.hand.deck[i])

		return printer

	def playCard (self, card) :

		return self.hand.playCard(card)

	def wonRound (self) :

		self.rounds += 1

	def declare (self, number = 0, suite = "NaN") :

		self.number = number

		suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

		self.suite = suites[suite]

	def teamUp (self, other) :

		self.team = Team(self, other)

		other.team = self.team

		return self.team

class Team :

	def __init__ (self, player1, player2) :

		self.player1 = player1

		self.player2 = player2

		self.score = 0

		self.challenge = False

	def __str__ (self) :

		return "Team:\n" + str(self.player1) + "\n" + str(self.player2) + "\n"





