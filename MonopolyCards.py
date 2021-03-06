#Started Tuesday, 11th of November, 2018

#Monopoly Deal card game card library
#Card values store all the info related to a card from its value to the type of card

#Error for all out of bounds values
class outOfBoundsError (Exception) :
	
	pass

#A class to store all the data related to any money card
class moneyCard :

	def __init__(self, value) :

		self.value = value

		if value != 1 and value != 2 and value != 3 and value != 4 and value != 5 and value != 10 :

			raise outOfBoundsError("Value out of bounds.")

#A class for action cards that apply to either no-one or everyone playing the game

class actionCardAll :

	def __init__ (self, cat) :

		types = ["rent", "passGo", "payment"]

		self.cat = types[cat - 1]


#A class for action cards which are played directly towards another player, and they have a self.player attribute which denotes which player they affect

class actionCardSpecific :

	def __init__ (self, cat) :

		types = ["rent", "payment", "cardSwap"]

		self.cat = types[cat - 1]

#Buildings don't fit in with the rest of the action cards and their dynamic is different so they have their own class

class buildings :

	def __init__(self, cat, set) :

		types = ["House", "Hotel"]

		values = [3, 4]

		self.cat = types[cat - 1]

		self.value = values[cat - 1]

#Property cards have many detailed attributes including color, title, rent value...etc

class propertyCard :

	def __init__(self, color, number, utilityStatus) :

		self.util = utilityStatus

		self.number = number

		if self.utilityStatus == False :

			if color > 8 or color < 1 :

				raise outOfBoundsError("Value out of bounds.")

			colors = ["Red", "Green", "Yellow", "Baby Blue", "Pink", "Orange", "Blue", "Brown"]

		else :

			if color > 2 or color < 1 :

				raise outOfBoundsError("Value out of bounds.")

			colors = ["Utility", "Train Station"]

		self.color = colors[color - 1]

		if color == 1 and self.utilityStatus == False :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["STRAND", "TRAFALGAR SQUARE", "FLEET STREET"]

			self.value = 3

		elif color == 2 and self.utilityStatus == False :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["REGENT STREET", "OXFORD STREET", "BOND STREET"]

			self.value = 4

		elif color == 1 and self.utilityStatus == True :

			if self.number > 2 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["ELECTRIC COMPANY", "WATER WORKS"]

			self.value = 2

		elif color == 2 and self.utilityStatus == True :

			if self.number > 4 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["LIVERPOOL ST. STATION", "KINGS CROSS STATION", "FENCHURCH ST. STATION", "MARYLEBONE STATION"]

			self.value = 2

		elif color == 3 :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["PICCADILLY", "LECIESTER SQUARE", "COVENTRY STREET"]

			self.value = 3

		elif color == 4 :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["PENTONVILLE ROAD", "EUSTON ROAD", "THE ANGEL, ISLINGTON"]

			self.value = 1

		elif color == 5 :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["WHITEHALL", "PALL MALL", "NORTHUMBERLAND AVENUE"]

			self.value = 2

		elif color == 6 :

			if self.number > 3 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["BOW STREET", "VINE STREET", "MARLBOROUGH STREET"]

			self.value = 2

		elif color == 7 :

			if self.number > 2 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["PARK LANE", "MAYFAIR"]

			self.value = 4

		elif color == 8 :

			if self.number > 2 or self.number < 1 :

				raise outOfBoundsError("Value out of bounds.")

			titles = ["OLD KENT ROAD", "WHITECHAPEL ROAD"]

			self.value = 1

		else:

			raise outOfBoundsError("Value out of bounds.")

		self.title = titles[number - 1]

#The card class is a general class for all cards, instances of different types of cards are stored as an attribute to the card

class Card :

	def __init__ (self, kind, customStat) :

		types = ["ActionA", "ActionS", "Building", "Property", "Money"]

		self.kind = types[kind - 1]

		if kind > 5 or kind < 1 :

			raise outOfBoundsError("Value out of bounds.")

		if kind == 1 :

			self.card = actionCardAll(customStat[0])

		elif kind == 2 :

			self.card = actionCardSpecific(customStat[0])

		elif kind == 3 :

			self.card = buildings(customStat[0])

		elif kind == 4 :

			self.card = propertyCard(customStat[0], customStat[1], customStat[2])

		elif kind == 5 :

			self.card = moneyCard(customStat[0])

	def __str__ (self) :

		return










