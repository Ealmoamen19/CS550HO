#Partner1: Eyad
#Partner2: Jansher

''' Instructions:
   Work with a partner to complete these tasks. You may assume that all variables/lists are declared and initialized (unless you are specifically asked to create/initialize a list); you need only write the code using the variables/lists indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Create a list of ints, faveNums, that holds 3 integers.
'''
 
faceNums = ["1", "2", "3"]
 
''' 2. 
   Create a list of Strings, holidays, that holds 14 holidays.  
'''
 
 holidays = ["holidays"] * 14
 
''' 3. 
   Create a list of characters, grades, that holds 5 letter grades.
'''
 
 grades = ['A'] * 5 
 
''' 4. 
   Create a list of booleans, funny, the can keep track of whether 18 things are funny or not. 
'''
 
 funny = [False] * 18
 
''' 5. 
   Create a list of floats, salaries, that holds the salaries of all the employees at a university. The number of employees is stored in the int numEmployees.
'''


salaries = [float(0)] * numEmployees
 
 
''' 6. 
   A picture's dimensions are stored in integer variables x and y. Create a single list of integers that can store the grayscale value for each pixel in the list.
'''
 
 grayscale = [0] * (x * y)
 
''' 7. 
   In a class, each student has 0, 1, 2 or 3 siblings. The numbers of students with no siblings is stored in the variable noSiblings, the number of students with one sibling is stored in the variable oneSibling, the number of students with two siblings is stored in the variable twoSiblings, and the number of students with three siblings is stored in the variable threeSiblings. Create a list that holds all the names of the students in the class, as well as the names of all their siblings.
'''

sib = ["noSiblings","oneSibling", "twoSiblings","threeSiblings"]
 
''' 8. 
   Create a list that holds all the months in the year. (No loop.)
'''
 months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
 
 
''' 9. 
   Create a list that holds all the days of the week. (No loop.)
'''
 
 days = ["Monday", "Tuesday", "Wenesday", "Thursday", "Friday", "Saturday"]
 
''' 10. 
   Create a list that holds all the possible values for boolean variables. (No loop.)
'''
 
boo = ["TRUE","FALSE"]
 
''' 11. 
   Create a list that holds the names of all the 3rd form dorms on campus. (No loop.)
'''
 
dorms = ["Mem","Squire","Pitman"]
 
''' 12.  
   Create a list that holds 3 random numbers with values between 0 and 1. (Loop optional.)
'''
 x = []
 for i in range(3):
   x.append(random.random())

 
''' 13. 
   Create a list that will represent a deck of cards. Some example data for cards would be AS (ace of spaces), 5H (5 of hearts), JC (jack of clubs), 9D (9 diamonds). (Loop required.) 
'''
lis = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
clas = ["H","S","D","C"]
deck = []
for x in range(4)
   for y in range(13)
      deck.append(clas[x] + lis[y])
 
''' 14. 
   Write a Yahtzee program that simulates the rolling of five dice and prints "Yahtzee" if all five dice are the same; otherwise it should print "Try again."
'''

 yahtzee = []

 for i in range(5) :

   yahtzee.append(random.randint(1, 6))

   if i > 0 :

      if yahtzee[i] != yahtzee[i - 1] :

         print("Try Again")
         break


      elif i == 4 :

         print("Yahtzee!")


 
''' 15. 
   In a list, specials are numbers in a list that have an even number before them, an odd number behind them, and they themselves are divisible by 3. Given a list of ints called numbers, print out the location in the list of the specials, as well as the value in front of them, their value, and the value behind them. For example:
   position 4: 14, 9, 25
'''
for x in range(0,y)
   if num%3 == 0:
      if before%2 == 0:
         if behind%2 != 0:
            position = num/3
            print(str("position",position+":",before+", "+num",",behind))
            num*3
   else:
      num += 1
 
''' 16. 
   Write a program to search for the "saddle points" in a 5 by 5 list of integers. A saddle point is a cell whose value is greater than or equal to any in its row, and less than or equal to any in its column. There may be more than one saddle point in the list. Print out the coordinates of any saddle points your program finds. Print out "No saddle points" if there are none.
'''

count = 0

for i in range(rowSpace) :

   x = max(num[i])

   col = num[i].index(x)

   comparison = []

   for j in range(rowSpace) :

      comparison.append(num[j][col])

   y = max(comparison)

   row = comparison.index(y)

   if x == y :

      print(row, col)

      count += 1

if count == 0 :

   print("No Saddle Points")




 
''' 17. 
   In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal. A chessboard can be represented by an 8 by 8 list. A 1 in the list represents a queen on the corresponding square, and a O in the list represents an unoccupied square. Given the two locations for queens (row1, col1, row2, col2), place the queens in the 2D list, chessboard. Then process the board and indicate whether or not the two queens are positioned so that they attack each other. 
'''
width = 7
height = 7
for x in range(width):
   for y in range(height):
      board = (height[x]),(width[y])
      position1 = [row1,col1]
      position2 = [row2,col2]
      if position1 = "1":
         position1 = queen1
      else: 
         position1 = empty

 
''' 18. 
   Given a list, write code that will reverse the order of the elements in the list. For example, dog, cat, bunny should become bunny, cat, dog.
'''

lis = [""] * x
lis.reverse()
print(*lis)
 
''' 19. 
   Given a list, doorknobs, that holds strings, swap the elements at positions 1 and 3, if possible.
'''
 x = doorknobs[3]

 doorknobs[3] = doorknobs[1]

 doorknobs[1] = x
 
 
''' 20. 
   In a list of ints called numbers, find the largest number in the list and place it at the end of the list.
'''
 
x = max(numbers)

numbers.remove(x)

numbers.append(x)

''' 21. 
   In a 2D list with dimensions w by h, filled with random numbers from from 1 to 100, replace every odd number with either 2 or 22; 2 if the number was a single digit number, 22 if the number was a 2-digit number. 
'''
 
 for i in range(w) :

   for j in range(h) :

      if lis[i][j] >= 10 :

         lis[i][j] = 22

      else :

         lis[i][j] = 2
 
''' 22. 
   In a 2D list with dimensions w by h, holding grayscale values for an image, adjust the colors so the image is inverted. All light portions should be dark, all dark portions should be light. A value of 200 should be 5, a value of 100 should be 155, etc. Remember, there are 256 levels for color, including 0.
'''
 
for i in range(w):

   for j in range (h):

      image[i][j] = abs(image[i][j] - 255)
 
''' 23.
   In a list, shifters, holding ints, shift all elements forward 1 position. For example, position 2 should move to position 1, position 1 to position 0, and position 0 to the end of the list (etc.)
'''
 
for i in range(len(lis)) :

   if i < len(lis) - 1

    lis2.append(lis[i] + 1)

   else:

    lis2.append(lis[0])

lis = lis2
 
''' 24. 
   Given an N-by-N grid of elevation values (in meters), a peak is a grid point for which all four neighboring cells are strictly lower. Write a code fragment that counts the number of peaks in a given N-by-N grid.
'''
 


count = 0

for i in range(N) :

   for j in range(N) :

      tempList = []

      if i > 0 and i < N and j > 0 and j < N :

         for a in range(i-1, i+2) :

            for b in range(j-1, j+2) :

               tempList.append(grid[a][b])

         if grid[i][j] = max(tempList) :

            count += 1

      elif i == 0 :

         if j != 0 and j != N :

            for a in range(2) :

               for b in range(j-1, j+2) :

                  tempList.append(grid[a][b])

            if grid[i][j] = max(tempList) :

               count += 1

         elif j == 0 :

            for a in range(2) :

               for b in range(2) :

                  tempList.append(grid[a][b])

            if grid[i][j] = max(tempList) :

               count += 1

         elif j == N :

            for a in range(2) :

               for b in range(N-1, N+1) :

                  tempList.append(grid[a][b])

            if grid[i][j] = max(tempList) :

               count += 1

      elif j == N :

         for a in range(i-1, i+2) :

            for b in range(N-1, N+1) :

               tempList.append(grid[a][b])

         if grid[i][j] = max(tempList) :

            count += 1

      elif j == 0 :

         for a in range(i-1, i+2) :

            for b in range(2) :

               tempList.append(grid[a][b])

         if grid[i][j] = max(tempList) :

            count += 1

 
''' 25. 
   90% of incoming college students rate themselves as above average. Write some code that, given a list of student rankings (stored in integer list rankings), prints the fraction of values that are strictly above the average value.
'''
 #Based on the assumption that the average is half lowest rank

avg = min(list2)

avg = avg / 2

count = 0

for i in list2 :

   if i > avg :

      count += 1

fraction = count/len(list2)

print(fraction)
 
 
''' 26. 
   Given a 9-by-9 list of integers between 1 and 9, check if it is a valid solution to a Sudoku puzzle: each row, column, and block should contain the 9 integers exactly once.
'''
 
def checkRow(grid, num) :

   for i in grid[num] :

      for j in grid[num] :

         if i == j :

            return False

   return True

def checkCol(grid, num) :

   for i in grid :

      for j in grid:

         if i[num] == j[num] :

            return False

   return True

def checkBlock(grid, x, y) :

   for i in range(3 * (x - 1), 3 * x) :

      for j in range(3 * (y - 1), 3 * y):

         for a in range(3 * (x - 1), 3 * x) :

            for b in range(3 * (y - 1), 3 * y):

               if grid[a][b] == grid[i][j] :

                  return False

   return True

for i in range(9) :

   checkRow(grid, i)

   checkCol(grid, i)

for i in range(1, 4) :

   for j in range(1, 4) :

      checkBlock(grid, i, j)
 
'''
    27. Create a list of 100 numbers between 1 and 10 (inclusive), create a new list whose first value is the number of 1s in the original list, whose 2nd value is the number of 2s in the original list, and so on. Average the number of occurences of each number in the list over 100 repetitions. Average the averages. Print the result to the screen.
'''
 

def occurances(lis) :
   
   count = 0

   counts = []

   for i in range(1, 11):

      for j in range(len(lis) - 1) :

         if lis[j] == i :

            count += 1

      counts.append(count)

   return counts

num = [0] * 10

for i in range(101) :

   lis = []

   for i in range(101) :

      lis.append(random.randint(1, 10))

   numTemp = occurances(lis)

   for i in range(10) :

      num[i] += numTemp[i]

average = 0

for i in range(10) :

   num[i] = num[i]/100

   average += num[i]

average = average/10

print(average)






 
''' Sources
   http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
   http://introcs.cs.princeton.edu/java/14array/