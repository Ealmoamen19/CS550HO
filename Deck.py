#ٍStarted Tuesday, 6th November 2018

from Card import Card

import random

class Deck :

	def __init__ (self, stats = True) :

		self.deck = []

		self.main = stats

		if self.main == True :

			for i in range(1, 5) :
				for j in range(1, 14):

					self.deck.append(Card(i, j))

			self.deck.append(Card())

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

		card = other.deck[len(other.deck) - 1]

		del other.deck[len(other.deck) - 1]

		self.deck.append(card)

	def playCard(self, card) :

		store = self.deck[card]
		
		del self.deck[card]

		return store
