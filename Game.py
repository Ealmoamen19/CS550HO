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

HK = ""

def initialize (players) :

	global mainDeck

	global HK

	print("\n")

	mainDeck.shuffle()

	print(mainDeck)

	Deal(mainDeck, players)

	high = 0

	for i in range(0, 4) :

		print(players[i])

		answer = input("Do you want to challenge?\n")

		if str(answer).lower() == "yes" or str(answer).lower() == "y" :

			bet = 0

			while (bet < 5 or bet > 8) :

				xer = True

				xcr = True

				while xer == True or xcr == True :

					bet = input("How Much? \n")

					if str(bet).isnumeric() == True :	

						bet = int(bet)

						xer = False

						if bet > 4 and bet > high and bet < 9 :

							high = bet 

							lastPlayer = i

							xcr = False

							xbr = True

							while xbr == True :

								HK = input("Choose your suite:\n1) Diamonds\n2) Hearts\n3) Spades\n4) Clovers\n")

								if HK.isnumeric() == True :

									if int(HK) >= 1 and int(HK) <= 4 :

										HK = int(HK)

										xbr = False

									else :

										print("Invalid input\nTry again.\n\n")

								else: 

									print("Invalid input\nTry again.\n\n")

						else :

							print("Invalid input\nTry again.\n\n")

					else:

						print("\nInvalid input\nTry Again.\n\n")

		if high == 8 :

			return [lastPlayer, high]

			break

	return [lastPlayer, high]

	players[lastPlayer].team.challenge = True

def teamUp (player1, player2) :

	return player1.teamUp(player2)

def suiteCheck (player, suite) :

	for i in range(0, len(player.hand.deck)) :

		if player.hand.deck[i].suite == suite :

			return True

	return False

def roundCheck (roundSuite, HK, pile) :

	highnum = 0

	piled = pile

	for i in range(0, len(piled)) :

		if piled[i].suite == "Joker" :

			return i

		elif piled[i].suite == HK :

			high = i

			highnum = piled[i].number

			for j in range(i, len(piled)) :

				if piled[j].suite == "Joker" :

					return j

				elif piled[j].suite ==	HK :

					if piled[j].number > highnum :

						high = j 

						highnum = piled[j].number

			return high

		else :

			if piled[i].suite == roundSuite and piled[i].number > highnum :

				high = i

				highnum = piled[i].number

	return high

def checkWin (bet, rounds) :

	if rounds < bet :

		return (-2 * bet)

	else :

		return bet

def rounds (players, stage, bet, challenger) :

	global HK

	if stage <= 8 :

		pile = []

		print(players[0])

		xer = True

		while xer == True :

			card = input("Play a card:\n")

			if card.isnumeric() == True :

				card = int(card)

				if card > 0 and card <= len(players[0].hand.deck) :

					card = int(card) - 1

					xer = False

				else :

					print("\nInvalid input\nTry Again.\n\n")

			else:

				print("\nInvalid input\nTry Again.\n\n")

		roundSuite = players[0].hand.deck[card].suite


		pile.append(players[0].hand.playCard(card))


		for i in range(1, 3) :

			print("i: " + str(i))

			print("Current pile:")

			for i in range(0, len(pile)) :

				print(str(pile[i]))

			print(players[i])

			xer = True

			while xer == True :

				card = input("Play a card:\n")

				if card.isnumeric() == True :

					card = int(card)

					if card > 0 and card <= len(players[i].hand.deck) :

						card = int(card) - 1

						if suiteCheck(players[i], roundSuite) == True and players[i].hand.deck[card].suite != roundSuite and players[i].hand.deck[card].suite != "Joker" :

							print("Suite invalid.\nTry Again.\n\n")

						else :

							pile.append(players[i].hand.playCard(card))

							xer = False

							print("Current pile:")

							for i in range(0, len(pile)) :

								print(str(pile[i]))

					else :

						print("\nInvalid input\nTry Again.\n\n")

				else:

					print("\nInvalid input\nTry Again.\n\n")

		winner = roundCheck(roundSuite, HK, pile)

		stage += 1

		players[winner].wonRound()

		rounds([players[winner], players[(winner + 1) % 4], players[(winner + 2) % 4], players[(winner + 3) % 4]], stage, bet, challenger)

	return checkWin(bet, challenger.team.rounds)


scanner = str(input ("Player 1 Name: "))

player1 = Player(scanner)

scanner = str(input ("Player 2 Name: "))

player2 = Player(scanner)

scanner = str(input ("Player 3 Name: "))

player3 = Player(scanner)

scanner = str(input ("Player 4 Name: "))

player4 = Player(scanner)

team1 = teamUp(player1, player3)

team2 = teamUp(player2, player4)

lis = [team1.player1, team2.player1, team1.player2, team2.player2]

param = initialize(lis)

lastPlayer = lis[param[0]]

rounds ([ lis[(param[0] + 1) % 4], lis[(param[0] + 2) % 4], lis[(param[0] + 3) % 4], lis[param[0]]], 0, param[1], lastPlayer)


print("\n\n")
