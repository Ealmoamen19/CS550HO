import random

iDBank = []
accounts = []

def randomID (length) :

	global iDBank

	alphaDig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	iD = ""

	for i in range(1, length) :

		if random.random >= 0.5 :

			iD += random.choice(alphaDig)

		else:

			iD += str(random.randInt(0, 10))

		iDBank.append(iD)

	return iD

def checkForOverlap (iD) :

	for i in iDBank :

		if iD == iDBank[i]:

			return True

	return False

def checkForExist (iD) :

	for i in accounts :

		if accounts[i].number == iD :

			return accounts[i]

	return False

class Bank :

	def __init__ (self, firstName, lastName, pin, balance, typer) :

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

	firstName = input("First Name: ")

	lastName = input("Last Name: ")

	pin = input("PIN Number: ")

	typer = input("What type of account would you like to open?\n(1) Checking Account\n(2) Saving Account\n\n")

	accounts.append(Bank(firstName, lastName, pin, 0, typer))


elif response == 2:

	xer = True

		while xer == True :

			response = input("Please enter your Account Number")

			if checkForExist(response) == False :

				print("Invalid iD\nTry Again")


		response2 = input("Please enter your password")









