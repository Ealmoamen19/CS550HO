from Card import Card

from Deck import Deck

from Player import Player, Team

def Filter (Deck) :

	filtered = []

	for i in range(0, len(Deck.deck)) :

		if int(Deck.deck[i].number) >= 7 or int(Deck.deck[i].number) < 2 :

			filtered.append(Deck.deck[i])

	del filtered[1]

	return filtered

def Deal (deck, players) :

	for i in range (0, 4) :

		for j in range (0, 8) :

			players[i].hand.drawCard(deck)


mainDeck = Deck()

mainDeck.deck = Filter(mainDeck)

scanner = str(input ("Player 1 Name: "))

player1 = Player(scanner)

scanner = str(input ("Player 2 Name: "))

player2 = Player(scanner)

scanner = str(input ("Player 3 Name: "))

player3 = Player(scanner)

scanner = str(input ("Player 4 Name: "))

player4 = Player(scanner)

team1 = Team(player1, player3)

team2 = Team(player2, player4)

print("\n")

mainDeck.shuffle()

Deal(mainDeck, [player1, player2, player3, player4])



print(str(player1) +  "\n" + str(player2) + "\n" + str(player3) + "\n" + str(player4)) 


