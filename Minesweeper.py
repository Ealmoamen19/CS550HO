import random as rand

row = 20

col = 20

cont = 0

array = []

for i in range(0, row + 2) :
	
	array.append([0] * (col + 2))

count = 0

mines = 100

while count < mines :

	x = rand.randint(1, row )

	y = rand.randint(1, col )

	if array[x][y] == 0 :

		array[x][y] = "*"
		
		count = count + 1

def printer (jay) :
	
	for j in range (1, row + 1) :
		
		xambia = []

		for i in range(1, col + 1) :

		
			xambia.append(jay[j][i])

		
		print(*xambia)

for i in range(row) :

	for j in range(col) :

		if array[i][j] == "*" :

			for a in range (i - 1 , i + 2) :

 				for z in range(j - 1, j + 2) :

 					if array[a][z] != "*" :

 						array[a][z] = array[a][z] + 1

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

				print("COL:")

				print(cols, rows)

				print()

				print(i,j)

				if array[i][j] == 0 and arr[i][j] == "o" :

					arr[i][j] = array[i][j] 

					global cont

					cont = cont + 1

					printer(arr)

					print()

					bloom (arr, i, j)

				elif array[i][j] != "*" and arr[i][j] == "o" :
					
					arr[i][j] = array [i][j]  

printer(array)

print("\n\n")

arrayM = []

for i in range(0,row + 2) :
	
	arrayM.append(["o"] * (col + 2))

printer(arrayM)

cont = 0

while cont < ((row * col) - mines):

	rowM = int(input("Row: "))

	colM = int(input("Column: "))

	val = array[rowM][colM]

	if val == 0 :

		bloom(arrayM, rowM, colM)

	else:

		arrayM[rowM][colM] = val

	printer(arrayM)

	cont = cont + 1

	if val == "*" :

		print("BOOM!\n\nGame Over.\n\n")

		quit()

print("You win!")






# for i in range(row) :

# 	print(*array[i])

#