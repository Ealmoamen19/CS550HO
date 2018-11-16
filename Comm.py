#Started: November 13 2018
#Completed: November 13 2018

#Honor Pledge: I have not given nor recieved any unauthorized aid

#Sources:
#http://letzgro.net/blog/creating-ai-using-python/


suites = ["Diamonds", "Hearts", "Spades", "Clovers"]

class Comm :

	def __init__(self, player) :

		self.player = player

	def playCard(self) :

		if self.player.hand.deck[1].suite != "Joker" :

			return self.player.hand.playCard(0)

		else :

			return self.player.hand.playCard(1)

	def declare(self) :

		global suites

		lis = [0, 0, 0, 0]

		for i in range(0, self.player.hand.deck) :

			print(self.player.hand.deck[i].suite)

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

				high = i

		return [5, high]

	def commPlay(self, roundSuite) :

		for i in (0, len(self.player.hand.deck)) :

			if self.player.hand.deck[i].suite == suite :

				return self.player.playCard(i)

		return self.player.playCard(1)





