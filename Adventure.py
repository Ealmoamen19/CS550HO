import random as rand

serialf = 1

orderf = 0

def Ques (num) :

    global choice
    
    choice = int(input())
    
    if 1 <= choice and choice <= num :

        xer = True

    else :

        xer = False
    

    if xer == False :

        print("Invalid input!\nTry again.\n\n")

        Ques (num)

    global serialf

    serialf = serialf + (choice * ((1/10) ** orderf)) 

    functions(serialf)

def functions (code) :

    if code == 1 :

     Intro ()

    elif code == 1.1 :

     fiddle ()

    elif code == 1.11 :

     number()

    elif code == 1.111 :

     enter()

    elif code == 1.1111 :

     hidden()

    elif code == 1.1112 :

     futureself()

    elif code == 1.112 :

     mash()

    elif code == 1.12 :

     red()
    
    elif code == 1.121 :

     explosion()
    
    elif code == 1.122 :

     randoexpo()
    
    elif code >= 1.13 and code < 1.131 :

     green()

    elif code == 1.131 :

     beamhand()

    elif code == 1.132 :

     explosion()
    
    elif code == 1.2 :

     dispose()
    
    elif code == 1.21 :

     flush()

    elif code <= 1.211 and code > 1.21 :

     candle()

    elif code == 1.212 :

     maze()

    elif code == 1.22 :

     garbage()
    
    elif code == 1.23 :

     slam()

    elif code >= 1.231 and code < 1.232 :

     zombie()

    elif code >= 1.232 and code < 1.233 :

     hide()

def Intro ():

  print("\n\n\nYou're sitting there in your room, when all of a sudden you notice a mysterious contraption on your table. \nDo you: \n(1) You investigate it. \n(2) You dispose of it.")
  
  global orderf
  
  orderf = 1

  Ques(2)

def fiddle () :
    
    print("\n\nYou find a number pad, a red button, and a green button on the contraption.\nDo you:\n(1) Enter a number.\n(2) Hit the RED button.\n(3) Hit the GREEN button.")

    global orderf

    orderf = 2
    
    Ques (3)    

def dispose () :
    
    print("\n\nHow do you dispose of it?\nDo you:\n(1) Flush it down the toilet.\n(2) Throw it in the dumpster.\n(3) Use a sledgehammer on it.")

    global orderf

    orderf = 2
    
    Ques (3)

def number () :

    print("\n\nDo you:\n(1) Enter a number.\n(2) Randomly mash the number pad.")

    global orderf

    orderf = 3
    
    Ques (2)

def green () :

    print("\n\nA green light is beamed from the contraption\nDo you:\n(1) Put your hand in the beam.\n(2) Break the light source.")

    global orderf

    orderf = 3
    
    Ques (2)

def red () :

    print("\n\nGood job!\nYou have initiated a nuclear explosion.\nDo you:\n(1) RUN!\n(2) Hit all the buttons on the contraption")

    global orderf

    orderf = 3
    
    Ques (2)

def flush () :

    print("\n\nYou cause a nationwide blackout. It's dark and you can't see a thing.\nDo you:\n(1) Light a candle\n(2) Try to make your way out of the house")

    global orderf

    orderf = 3
    
    Ques (2)

def garbage () :

    print("\n\nCongrats!\nYou managed to end this game in the fastest, most boring way possible.\n")

    quit()

def slam () :

    print("\n\nThe contraption starts making sounds...\nIt starts glowing...\nIt blows up in your face, and next thing you know, your house\nis in ruins and your neighborhood is in what looks like a zombie apocalypse\nDo you:\n(1) Pretend you're a zombie.\n(2) Hide.")

    global orderf

    orderf = 3
    
    Ques (2)

def zombie () :

	print("\n\nA zombie gets close to you.\nIt says: BRAIINNS\nDo you:\n(1) Freak out.\n(2) Repeat: BRAIINNS")

	choose = int(input())
    
	if choose == 1 :

		print("The zombies now know you have brains.\nThey pile up over you and you end up a brainless blah.")

		quit()

	elif choose == 2 :

		print("Good job!\nYou survived managed to win this game...\nWhich is just like losing except for the fact that we say you won.")

		quit()

def hide () :

	print("While you were looking for somewhere to hide, you fell into the sewer...")

	print("The sewer is filled with sulfuric acid and you are now effectively nothing but a puddle.")

	quit()

def candle () :

	print("You somehow manage to find the matches, you light one up and accidentaly set the house on fire.")

	print("Rest in pieces...")

	quit()

def maze () :

	z = str(input("Which way do you go?\nForward, Backwards, Right, or Left?\nType F,B,R,L:"))

	while True :	

		if z == "F" or z == "f" :

			print("You fall out of the window\n\nMy condolences.")

			quit()

		elif z == "B" or z == "b" :

			print("You trip on a wire, you fall on the back of your head.\nYou wake up to find yourself in heaven, only to realize it's a dream, and\nreally wake up after two hours and find yourself fallen to the bottom floor of your house.")

			z = str(input("Which way do you go?\nForward, Backwards, Right, or Left?\nType F,B,R,L:"))

			while True :
				
				if z == "F" or z == "f" or z == "b" or z == "B" or z == "L" or z == "l" :

						print("You accidentally step on a powder fire extinguisher.\nThe powder fills the room, and you suffocate to death.")

						quit()

				elif z == "R" or z == "r" :

						print("Congrats!\nYou find the door and escape the house.\nSo...let's just say you won, which is the same as losing except we call it winning.")

						quit()

				else :

					print("Invalid input!\nTry again.")


		elif z == "R" or z == "r" or z == "L" or z == "l" :

			print("You slip on a banana peel you threw earlier (well done by the way) and fall on the stairs.\nUnfortunately, you don't recover from the fall :(\nWell, verdict is, you're dead.")

			quit()
		else :

			print("Invalid input!\nTry again.")

			z = str(input("Which way do you go?\nForward, Backwards, Right, or Left?\nType F,B,R,L:"))

def futureself () :

	print("You find it's a version of yourself, and with that you break all time...and existance...including your own existance")

	quit()

def hidden () :

	print("You see a version of yourself\nDo you:\n(1) Go up and say hi.\n(2) Stay hidden.")

	c = int(input ())

	jay = False

	while jay == False :
	
		if c == 1 :

			print("With that you break all time...and existance...including your own existance")

			quit()

		elif c == 2 :

			print("Yourself finds your hiding place, and with that you break all time...and existance...including your own existance")

			quit()

		else :

			print("Invalid input!\nTry again.")

def enter () :

    year = int(input("\n\nEnter a number: "))

    YEAR = str(year)

    jay = False

    while jay == False :

	    if year <= 2070 and year >= 2000:

	    	print("Turns out the contraption's a time machine...")

	    	print("You're in your room and the calendar is on the year" + YEAR + ".")

	    	print("Everything looks the same...")

    		print("all of a sudden you hear someone coming\nDo you:\n(1) Hide. \n(2) Go to see who it is.")

	    	global orderf
    	
	    	orderf = 4 

    		Ques(2)

	    elif year <= 2000 and year >= 400 :

	    	print("Turns out the contraption's a time machine...")

	    	print("We are now in the year " + YEAR + ".")

	    	print("You are somehow lost in the middle of a corn field with a fire 400 yards away and closing")

	    	print("Try to run?")

	    	j = input("Yes or No?")

	    	jay = False

	    	while jay == False :

	    		if j == "Yes" or j == "yes" or j == "YES" :

	    			print("You run for a minute and then you hit a wall.")

	    			print("The fire closes in and you are nothing but roasted meat")

	    			quit()

	    		elif j == "no" or j == "No" or j == "NO" :

	    			print("You somehow manage to get through the fire...")

	    			print("Unfortunately, it's nothing but ashes for miles and so you starve and perish.")

	    			quit()

	    		else :

	    			print("Invalid response.")

	    			print("Try again!")
	    elif year <= 400 and year >=0 :

	    	print("Turns out the contraption's a time machine...")

	    	print("You find yourself in the year " + YEAR + ".")

	    	print("Nothing but a thick forest going on forever")

	    	print("A lion approaches...")

	    	x = input("Fight for your life?\nYes or No?")

	    	jay = False

	    	while jay == False :

	    		if x == "Yes" or x == "yes" or x == "YES" :
	    			jax = rand.random()

	    			if jax >=0.5 :
    			
	    				print("You fight like hell, and manage to break the lion's neck.")

	    				print("But then you look down and your legs have been bitten off.\nWith nowhere to go, you lie there, only for the pests to eat your body")

	    				quit()

	    			else:
	    				print("The lion rips you to shreds and you don't remember anything that happened after that...")

	    				print("You know, because you're dead.")

	    				quit()


	    		elif x == "no" or x == "No" or x == "NO" :

	    			print("The lion rips you to shreds and you don't remember anything that happened after that...")

	    			print("You know, because you're dead.")

	    			quit()

	    		else :

	    			print("Invalid response.")

	    			print("Try again!")

	    elif year >=2070 :

	    	print("Turns out the contraption's a time machine...")

	    	print("You find yourself in the year " + YEAR + ".")

	    	print("The world is overrun by aliens...")

	    	print("As soon as one of them saw you, you were imprisoned for life...in a ZOO")

	    	quit()

	    else : 
			
	    	print("Invalid response.")

	    	print("Try again!")

def mash () :

    print("\n\nCongratulations!\nYou managed to cause a time overlap between the year 1 B.C. and the year 5000 A.D. with you somehow caught in the middle of it.")

    quit()

def explosion () :

	print("Yeah, you're not faster than a nuclear explosion so...\nyou guessed it: KABOOM!")

	quit()

def randoexpo () :

	x = rand.random()

	if x >= 0.5 :

		print("You managed to diffuse the destruction sequence.")

		fiddle()

	else :

		print("Good try but unfortunately it blows up in your face and now you're nothing but vapor.")

		quit()

def beamhand() :

	print("You're sucked into a wormhole and you find yourseld at the other side of the universe with no way back...\nYou notice the contraption floating in the middle of space, with a keypad...\nApparently there's a passcode you can use to reverse what happened.")

	for i in range(2) :

		pcattempt = input("passcode: ")

		if pcattempt == "contraption" :

			print("Well Done!\nYou're right back where you started.")

			global serialf

			serialf = 1

			Intro()

		else :

			print("Attempts left:")

			print (3 - (i + 1))

	print("You remain floating in outer space till the end of time...")

	quit()
		

Intro()