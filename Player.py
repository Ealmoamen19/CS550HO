from Deck import Deck

from Card import Card

class Player :

	def __init__ (self, name) :

		self.name = name

		self.hand = Deck(False)

		self.rounds = 0

	def __str__ (self) :

		return "Name: " + self.name + "\nHand: " + str(self.hand) + "\n"

	def playCard (self, card) :

		return self.hand.playCard(card)

	def wonRound (self) :

		self.rounds += 1

class Team :

	def __init__ (self, player1, player2) :

		self.player1 = player1

		self.player2 = player2

		self.score = 0

	def __str__ (self) :

		return str(player1) + "\n" + str(player2) + "\n"



