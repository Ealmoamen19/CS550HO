#ٍStarted Tuesday, 6th November 2018

from Card import Card

import random

class Deck :

	def __init__ (self, stats) :

		self.deck = []

		self.main = stats

		if self.main == True :

			for i in range(1, 5) :
				for j in range(1, 13):

					self.deck.append(Card(i, j))

		self.printer = ""

	def addCard (self, appendee) :

		self.deck.append(appendee)

	def printCard (self, position) :

		return self.deck[position]

	def __str__ (self) :

		for i in range(0, len(self.deck)) :

			self.printer = self.printer + "\n" + str(self.deck[i])

		return self.printer

	def shuffle (self) :

		shuffled = []

		for i in range(0, len(self.deck)) :

			shuffled.append(random.choice(self.deck))

		self.deck = shuffled

	def drawCard (self, other) :

		card = self.deck[len(self.deck) - 1]

		self.deck.remove(len(self.deck) - 1)

		other.deck.append(card)


mainDeck = Deck(True)

print(mainDeck)

mainDeck.shuffle()

print(mainDeck)
