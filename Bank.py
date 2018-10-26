import random

def randomID (length) :

	alphaDig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	iD = ""

	for i in range(1, length) :

		if random.random >= 0.5 :

			iD += random.choice(alphaDig)

		else:

			iD += str(random.randInt(0, 10))

	return iD

class Bank :

	def __init__ (self, firstName, lastName, pin, number, status, balance, typer) :

		self.firstName = firstName
		self.lastName = lastName
		self.pin = pin
		self.number = randomID(10)
		self.status = "OPEN"
		self.balance = balance
		self.typer = typer

	def withdraw (amount) :

		balance = balance - amount

	def deposit (amount) :

		balance = balance + amount

	def printStats () :

		return "Account Number: " + self.number + "\nName: " + self.firstName + " " + self.lastName + "\nCurrent Status: " + self.status + "\nBalance: $" + self.balance

response = input("What would you like to do?\n\n(1) Create a Bank Account\n(2) Access your bank account\n")

if response == 1:


elif response == 2:

	response = input("Please enter your Account Number")

	response2 = input("Please enter your password")







