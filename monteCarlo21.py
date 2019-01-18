#Date Started: 01/16/2018
#Date Completed: 01/18/2018

#Sources:
#https://www.bicyclecards.com/how-to-play/blackjack/
#https://www.youtube.com/watch?v=ogtAvjVOmcI
#http://greatbridgelinks.com/casino-games-explained/
#Strategy: https://wizardofodds.com/games/blackjack/strategy/4-decks/
#Card class: https://github.com/Ealmoamen19/CS550HO/blob/master/Card.py
#Deck class: https://github.com/Ealmoamen19/CS550HO/blob/master/Deck.py

#Honor Pledge: I have not given nor recieved any unauthorized aid.

#########     MONTE CARLO BLACKJACK SIMULATION     #########

#	Project Summary: This program simulates the outcomes of Blackjack using Monte Carlo Simulations. It calculates the chances of a blackjack, normal win,
# normal loss, bust, and tie. It simulates the game in 5 scenarios: a scenario in which the player always stands, a scenario in which the player
# always hits once, a scenario in which the player always hits twice, and last but not least, a scenario in which the player uses a special strategy 
# I've retrieved online. 

#	Blackjack Explanation: Blackjack is a card game that uses a standard 52 card deck. All the players in the game play against the dealer. The goal is
# to accumulate more points than the dealer in the round without going above 21. The amount of points for all the number cards is their number. For 
# example, 10 of Spades will give you 10 points. The image cards (Jack, Queen, King) are worth 10 points each, the ace, on the other hand can either 
# be worth 1 point or 11 points depending on the situation. For example if the player had an ace and a 4, the ace would be worth 11 points and the 
# total points would add up to 15. But if the player had a king, a 5, and an ace, if theace was worth 11, the total points would add up to 26 which 
# is higher than 21, hence, in cases like this, the ace is worth 1 point. 

#	The best hand in the game is a natural blackjack, which is an ace and a 10-point card (10, Jack, Queen, King). If the player has a blackjack and
# the dealer doesn't, the player wins immediately and gets 3/2 of the amount he/she gambled extra. If both the player and the dealer have a blackjack 
# it's a tie The player can also win without a blackjack by having more points than the dealer, in which case the player gets the amount they gambled 
# extra. If the dealer's points are equal to the player's points, it's a tie and the player gets his/her money back, unless either has a blackjack that 
# is. If the player goes over 21 points, he/she losses immediately, even if the dealer also busts (goes over 21 points).

#	Each player gets two cards initially. The dealer gets one face-up card and one face-down card. From there the player can stand; or stick with 
# whatever cards he/she got. The player can also hit; or draw another card from the deck. There are other options such as doubling down and splitting, 
# but this project only tackles standing and hitting. After the player makes their move, the dealer can make his moves, then the points are calculated,
# and whoever has the highest number of points without going over 21 wins.

#I used my card and deck class from my fall term final project for the structure of the game.
from Card import Card

from Deck import Deck

#Sys is used here to gain user input on the number of times the simulation is to be repeated.
import sys

#evald is a function that returns the number of points in a given hand to be inserted as a parameter.
def evald(hand) :

	#count holds the amount of points.
	count = 0

	#aces are dealt differently based on the rest of the hand, so they're kept in a list until the rest of the cards are accounted for.
	aces = []


	#hand.deck is a list that belongs to the deck class and contains all the cards in the deck.
	for i in range(len(hand.deck)) :

		#Jacks, Queens, and Kings in the card class have the number variables 11, 12, 13 respectively, and they all add 10 points.
		if hand.deck[i].number >= 10 :

			count += 10

		elif hand.deck[i].number == 1 :

			#Aces are initially added to the list 'aces' to be dealt with later
			aces.append(hand.deck[i])

		else :

			#The rest of the cards add their number to the count
			count += hand.deck[i].number

	if len(aces) > 0 :

		#Since 2 aces would add up to 22, which is higher than 21, only one ace, if any, is worth 11 points. The equation checks if --after adding 
		#11 points for one ace and 1 for the rest-- the total amount of points would surpass 21, if it does, it adds all aces as worth 1 point.
		if count + 11 + (len(aces) - 1) <= 21 :

			count += 11

			count += (len(aces) - 1)

		else :

			count += len(aces)

	#The amount of points is returned.
	return count

#check21 checks whether or not there's a blackjack, if so, it returns true, otherwise, it returns false.
def check21(hand) :

	#If the first card is a 10-point card and the other is an ace.
	if hand.deck[0].number >= 10 :

		if hand.deck[1].number == 1 :

			return True

		return False

	#If the second card is a 10-point card and the first is an ace.
	elif hand.deck[1].number >= 10 :

		if hand.deck[0].number == 1 :

			return True

		return False

	return False

#This is the class that runs the game, and the parameter 'num' is the number of hits the player will constantly do, so if 0 is put into this, the 
#player always stands. The function returns int values, each means a different result: 
#1 - blackjack
#2 - tie
#3 - loss
#4 - win
#5 - bust

def game(num) :

	#Deck() with empty parenthesis in the deck class creates a standard 52 card deck plus the joker. 
	deck = Deck()

	#The joker would be useless in this game, so it is removed from the deck.
	del(deck.deck[52])

	#The 'shuffle' function shuffles the deck given.
	deck.shuffle()

	#Deck with a false parameter creates an empty deck in the deck class, which could be used for hands, as in this case
	dealer = Deck(False)

	player = Deck(False)

	#Both the player and the dealer get dealt two cards in the beginning.
	for i in range(2) :

		dealer.drawCard(deck)

		player.drawCard(deck)


	#Before any plays are made, the program checks if there are any blackjacks, because that would end the game immediately.
	if check21(player) == True and check21(dealer) == False :

		#blackjack
		return 1

	elif check21(player) == True and check21(dealer) == True :

		#tie
		return 2

	elif check21(player) == False and check21(dealer) == True :

		#loss
		return 3

	
	#This for loop makes hits as many times as the parameter suggests.
	for i in range(num) :

		player.drawCard(deck)

	#playerHand and dealerHand hold the amount of points for both the player and the dealer.
	playerHand = evald(player)

	dealerHand = evald(dealer)

	#The dealer is made to always hit if the amount of points they have is less than 16.
	while dealerHand < 16  :

		dealer.drawCard(deck)

		dealerHand = evald(dealer)

	#If the player busts, they lose immediately.
	if playerHand > 21 :

		#Bust
		return 5

	#If the dealer busts, or the player has more points than them, it's a win.
	elif dealerHand > 21 or playerHand > dealerHand :

		#Win
		return 4

	#If the dealer has more points than the player, the player loses.
	elif dealerHand > playerHand :

		#Loss
		return 3

	elif dealerHand == playerHand :

		#Tie
		return 2


#Strategy is a modified version of the game function that makes the player follow a specific strategy I found online.
#The strategy code is acknowledged in this function.
def strategy() :

	deck = Deck()

	del(deck.deck[52])

	deck.shuffle()

	dealer = Deck(False)

	player = Deck(False)

	for i in range(2) :

		dealer.drawCard(deck)

		player.drawCard(deck)

	if check21(player) == True and check21(dealer) == False :

		return 1

	elif check21(player) == True and check21(dealer) == True :

		return 2

	elif check21(player) == False and check21(dealer) == True :

		return 3

	playerHand = evald(player)

	#The strategy has two cases: the case in which there's an ace in the player's hand, and the case where there isn't. This strategy also takes
	#into account the top card in the dealer's hand. The details of the strategy are in the graph in the link commented above.
	if player.deck[0].number != 1 and player.deck[1] != 1 :

		if playerHand <= 11 :

			player.drawCard(deck)

		elif (playerHand <= 16 and (dealer.deck[1].number == 1 or dealer.deck[1].number >= 7)) :

			player.drawCard(deck)

		elif playerHand == 12 and (dealer.deck[1].number == 2 or dealer.deck[1].number == 3) :

			player.drawCard(deck)

	else :

		if playerHand <= 17 :

			player.drawCard(deck)

		elif (player == 18 and (dealer.deck[1].number >= 9 or dealer.deck[1].number == 1)) :

			player.drawCard(deck)

	playerHand = evald(player)

	dealerHand = evald(dealer)

	while dealerHand < 16  :

		dealer.drawCard(deck)

		dealerHand = evald(dealer)

	dealerHand = evald(dealer)

	if playerHand > 21 :

		return 5

	elif dealerHand > 21 or playerHand > dealerHand :

		return 4

	elif dealerHand > playerHand :

		return 3

	elif dealerHand == playerHand :

		return 2


#The number of simulations 'number' is taken from the command line

number = int(sys.argv[1])


#A friendly introduction to the program before the simulations start

print("\n\nWelcome to Blackjack Simulation, this program simulates the outcomes of\nBlackjack using Monte Carlo Simulations in a few scenarios including:\n\nAlways Stand\n\nSpecial Strategy\n\nAlways Hit Once\n\nAlways Hit Twice\n\n")

print("--   STAND SIMULATION   --\n\n")

#Results are stored in the list 'counter'.
#If it's a blackjack, 1 is added to the first slot, if it's a tie, 1 is added to the second slot, if it's a loss 1 is added to the third slot, if 
#it's a win, 1 is added to the fourth slot, and finally, if it's a bust, 1 is added to the fifth slot.

counter = [0] * 5

for i in range(number) :

	#This is always stand simulation, hence, the parameter in game is 0.
	result = game(0)

	counter[result - 1] += 1

total = sum(counter)

#All the numbers and rates are printed following the header.

print("Blackjacks: " + str(counter[0]))

print("Blackjack Rate : " + str((counter[0]/total) * 100) + "%\n")

print("Wins: " + str(counter[3]))

print("Win Rate : " + str((counter[3]/total) * 100)+ "%\n")

print("Losses: " + str(counter[2]))

print("Loss Rate : " + str((counter[2]/total) * 100)+ "%\n")

print("Bust: " + str(counter[4]))

print("Bust Rate : " + str((counter[4]/total) * 100)+ "%\n")

print("Ties: " + str(counter[1]))

print("Tie Rate : " + str((counter[1]/total) * 100)+ "%\n\n")

#The rest of the simulations follow the same pattern.

print("--   STRATEGY SIMULATION   --\n\n")

counter = [0] * 5

for i in range(number) :

	result = strategy()

	counter[result - 1] += 1

total = sum(counter)

print("Blackjacks: " + str(counter[0]))

print("Blackjack Rate : " + str((counter[0]/total) * 100) + "%\n")

print("Wins: " + str(counter[3]))

print("Win Rate : " + str((counter[3]/total) * 100)+ "%\n")

print("Losses: " + str(counter[2]))

print("Loss Rate : " + str((counter[2]/total) * 100)+ "%\n")

print("Bust: " + str(counter[4]))

print("Bust Rate : " + str((counter[4]/total) * 100)+ "%\n")

print("Ties: " + str(counter[1]))

print("Tie Rate : " + str((counter[1]/total) * 100)+ "%\n\n")


print("--   1 HIT SIMULATION   --\n\n")

counter = [0] * 5

for i in range(number) :

	result = game(1)

	counter[result - 1] += 1

total = sum(counter)

print("Blackjacks: " + str(counter[0]))

print("Blackjack Rate : " + str((counter[0]/total) * 100) + "%\n")

print("Wins: " + str(counter[3]))

print("Win Rate : " + str((counter[3]/total) * 100)+ "%\n")

print("Losses: " + str(counter[2]))

print("Loss Rate : " + str((counter[2]/total) * 100)+ "%\n")

print("Bust: " + str(counter[4]))

print("Bust Rate : " + str((counter[4]/total) * 100)+ "%\n")

print("Ties: " + str(counter[1]))

print("Tie Rate : " + str((counter[1]/total) * 100)+ "%\n\n")

print("--   2 HIT SIMULATION   --\n\n")

counter = [0] * 5

for i in range(number) :

	result = game(2)

	counter[result - 1] += 1

total = sum(counter)

print("Blackjacks: " + str(counter[0]))

print("Blackjack Rate : " + str((counter[0]/total) * 100) + "%\n")

print("Wins: " + str(counter[3]))

print("Win Rate : " + str((counter[3]/total) * 100)+ "%\n")

print("Losses: " + str(counter[2]))

print("Loss Rate : " + str((counter[2]/total) * 100)+ "%\n")

print("Bust: " + str(counter[4]))

print("Bust Rate : " + str((counter[4]/total) * 100)+ "%\n")

print("Ties: " + str(counter[1]))

print("Tie Rate : " + str((counter[1]/total) * 100)+ "%\n\n")

#End of program.
###
##
#


	

	