from Card import Card

class Deck :

	def __init__ (self) :

		self.deck = []

		self.printer = "Deck:"

	def addCard (self, appendee) :

		self.deck.append(appendee)

	def printCard (self, position) :

		return self.deck[position]

	def __str__ (self) :

		for i in self.deck :

			self.printer = self.printer + "\n" + str(self.deck[i])

		return self.printer



mainDeck = Deck()

for i in range(1, 4) :
	for j in range(1, 13):

		mainDeck.addCard(Card(i, j))

print(mainDeck.printCard(10))

x = str(mainDeck)

print(x)
