class Anan :

	def __init__ (self, name, hunger, energy, annoyingness) :

		self.hunger = 5

		self.energy = 25

		self.annoyingness = 100

		self.brains = None

		self.name = name

	def annoy(self, time):

		annoyingness += (time * 1.6)

		energy -= (time * 0.4)

	def stats(self) :

		return "Name: " + str(self.name) + "\nHunger: " + str(self.hunger) + "\nEnergy: " + str(self.energy) + "\nAnnoyingness: " + str(self.annoyingness) + "\nBrains: " + str(self.brains)


anan1 = Anan("Anan", 0, 20, 0)

print(anan1.stats())