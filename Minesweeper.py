# Started: 09/30/2018
# Finished: 10/15/2018

# Random module for randomly distributing mines
import random as rand

#Variables for the amount of rows and columns
xpr = False

while xpr == False:

	row = input("How Many Rows? ")

	col = input("How Many Columns? ")

	if row.isnumeric() == True and col.isnumeric() == True and int(row) > 0 and int(col) > 0 :

		row = int(row)

		col = int(col)

		xpr = True

	else :

		print("\nInvalid input.\nTry Again!\n\n")

cont = 0

array = []

# Horizontal axis for ease of reading
axis = []

axis.append(0)

axis.append(" ")

for i in range(1, col + 1) :
	
	if i < 11 :
		
		axis.append(i)

	elif i >= 11 :

		axis.append("")
		axis.append(i)


# Starting out with a full zero array
for i in range(0, row + 2) :
	
	array.append([0] * (col + 2))

count = 0

xpr = False

while xpr == False:

	mines = input("How Many Mines? ")

	if mines.isnumeric() == True and int(mines) > 0 and int(mines) <= row * col :

		mines = int(mines)

		xpr = True

	else :

		print("\nInvalid input.\nTry Again!\n\n")

# Randomly adding mines
while count < mines :

	x = rand.randint(1, row )

	y = rand.randint(1, col )

	if array[x][y] == 0 :

		array[x][y] = "*"
		
		count = count + 1

# Array print function for user friendly output
def printer (jay) :
	
	for j in range (1, row + 1) :
		
		xambia = []

		for i in range(1, col + 1) :

			if i < 11 :
		
				xambia.append(jay[j][i])

			elif i >= 11 :

				xambia.append(" ")
				xambia.append(jay[j][i])

		# Move the array for two digit numbers in the axis

		if j < 10 :

			print(j, end = "   ")

		else :

			print(j, end = "  ")
		
		print(*xambia)


# Adding numbers around each bomb
for i in range(row + 1) :

	for j in range(col + 1) :

		if array[i][j] == "*" :

			for a in range (i - 1 , i + 2) :

 				for z in range(j - 1, j + 2) :

 					if array[a][z] != "*" :

 						array[a][z] = array[a][z] + 1

# Zero Expansion function

def bloom (arr, rows, cols) :

	if array[rows][cols] == 0 :

		if rows < 1 :

			rows = 1

		elif rows > row:

			rows = row

		if cols < 1 :

			cols = 1

		elif cols > col:

			cols = col

		for i in range (rows - 1, rows + 2) :

			for j in range (cols - 1, cols + 2) :

				if array[i][j] == 0 and arr[i][j] == "o" :

					arr[i][j] = array[i][j] 

					global cont

					cont = cont + 1

					bloom (arr, i, j)

				elif array[i][j] != "*" and arr[i][j] == "o" :
					
					arr[i][j] = array [i][j]  



print("\n\n")

# Dummy array to fill from original whenever user picks a slot
arrayM = []

for i in range(0,row + 2) :
	
	arrayM.append(["o"] * (col + 2))

	# "o" denotes covered slots in array


# Variable to display the mines left after flagging

MinesLeft = mines

cont = 0


# cont is the number of uncovered spots
# Function runs while uncovered slots are less than all spots - mines
while cont < ((row * col) - mines):

	print(*axis)

	print()

	printer(arrayM)

	print("Mines Left: ")

	print(MinesLeft)

	print()

	xer = False

	# Checks if the value is numeric and valid

	while xer == False: 

		rowM = input("Row: ")

		colM = input("Column: ")

		if rowM.isnumeric() == True and colM.isnumeric() == True and int(rowM) > 0 and int(rowM) < row and int(colM) > 0 and int(colM)  < col:

			rowM = int(rowM)

			colM = int(colM)

			xer = True

		else :

			print("\nInvalid input.\nTry Again!\n\n")

	flag = input("Flag? ")

	if flag.lower() == "yes" or flag.lower() == "y" :

		#"F" Denotes the flag
		arrayM[rowM][colM] = "F"

		MinesLeft = MinesLeft - 1

	else:

		val = array[rowM][colM]

		if val == 0 :

			bloom(arrayM, rowM, colM)

		else:

			arrayM[rowM][colM] = val


		cont = cont + 1

		if val == "*" :

			# Game Over

			print("BOOM!\n\nGame Over.\n\n")

			quit()


print("You win!")