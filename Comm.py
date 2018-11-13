#Started: November 13 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:
#http://letzgro.net/blog/creating-ai-using-python/

from Card import Card
#Deck class
from Deck import Deck
#Player and team classes
from Player import Player, Team

import random

suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

class Comm :

	def __init__(self, player) :

		self.player = player

	def playCard(self) :

		return self.player.hand.playCard(1)

	def declare(self) :

		global suites

		lis = [0, 0, 0, 0]

		for i in range(0, self.player.hand.deck) :

			if self.player.hand.deck[i].suite == "Diamonds" :

				lis[0] += 1

			elif self.player.hand.deck[i].suite == "Hearts" :

				lis[1] += 1

			elif self.player.hand.deck[i].suite == "Spades" :

				lis[2] += 1

			elif self.player.hand.deck[i].suite == "Clovers" :

				lis[3] += 1

		high = 0

		for i in range(0, len(lis)) :

			if lis[i] > high :

				high = lis[i]

		return 5, high


print ("I work!!")


