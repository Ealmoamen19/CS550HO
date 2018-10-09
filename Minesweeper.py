import random as rand

row = 10

col = 10

cont = 0

array = []

axis = []

axis.append(0)

axis.append(" ")

for i in range(1, col + 1) :
	
	axis.append(i)

for i in range(0, row + 2) :
	
	array.append([0] * (col + 2))

count = 0

mines = 5

while count < mines :

	x = rand.randint(1, row )

	y = rand.randint(1, col )

	if array[x][y] == 0 :

		array[x][y] = "*"
		
		count = count + 1

# Array print function

def printer (jay) :
	
	for j in range (1, row + 1) :
		
		xambia = []

		for i in range(1, col + 1) :

		
			xambia.append(jay[j][i])

		if j < 10 :

			print(j, end = "   ")

		else :

			print(j, end = "  ")
		
		print(*xambia)

for i in range(row + 1) :

	for j in range(col + 1) :

		if array[i][j] == "*" :

			for a in range (i - 1 , i + 2) :

 				for z in range(j - 1, j + 2) :

 					if array[a][z] != "*" :

 						array[a][z] = array[a][z] + 1

#Expansion function

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

#Dummy array
arrayM = []

for i in range(0,row + 2) :
	
	arrayM.append(["o"] * (col + 2))

MinesLeft = mines

cont = 0

while cont < ((row * col) - mines):

	print(*axis)

	print()

	printer(arrayM)

	print("Mines Left: ")

	print(MinesLeft)

	print()

	rowM = int(input("Row: "))

	colM = int(input("Column: "))

	flag = input("Flag? ")

	if flag == "yes" or flag == "Yes" or flag == "y" or flag == "Y" :

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

			print("BOOM!\n\nGame Over.\n\n")

			quit()

print("You win!")