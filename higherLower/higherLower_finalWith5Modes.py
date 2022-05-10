import random
#Higher or Lower basic gambling program
        #CONTENTS PAGE, USE CTRL+F AND SEARCH NUMBER
#000.0              functions defined here
    #000.1          triesPrint
    #000.2          minAmt
    #000.3          gm2Over
        #000.4.1    gm3Turns
        #000.4.2    gm3Win
    #000.5          gm4Lose
        #000.6.1    gm5Bomb
        #000.6.2    gm5 other boxes

#001.0              game setup
    #001.1          name and age entry, check valueerror, system exit if underage
    #001.2          choose gamemode, learn the rules
    #001.3          if gm4, no wallet, if gm5, set wallet, otherwise random wallet with user box choice
    #001.4          determine if gamemode runs within main higherlower loop, 002
    #001.5          various counters, variables defined here, explinations given

#002.0              main higherlower loop begins here
    #002.1          gm1, gm2, gm3 run here while gameplay == true, determined in 001.4
    #002.2          gm1 winning streak check, ask if user would like to get more back
    #002.3          gm2, gm3 tries check + gm3 wallet passed million check here
    #002.4          counter increments and number randomisers
    #002.5          check if doubleorn, if not then place bets manually
    #002.6          enter higher or lower guess main game
        #002.7.1    randnum < nextrand
        #002.7.2    randnum > nextrand
    #002.8          check if passed minimum wallet threshold
    #002.9          mystery box chance time here
        #002.9.1    1/5 chance determined here
        #002.9.2    randomise boxes, check if values are the same, if yes then change until they are different
        #002.9.3    user chooses box here
        #002.9.4    box choice determined here, money added to wallet if won, continue game

#003.0              gamemode 4 starts here
    #003.1          number randomisers here
    #003.2          user higher lower choice
        #003.3.1    randnum < nextrand
        #003.3.2    randnum > nextrand
    #003.4          turn incrementer here

#004.0              determine variables, gamemode 5 starts here
    #004.1          boxes assigned random and different value picked from random.sample array, values from 0 - 4, changed each loop turn
    #004.2          user box choice, str.upper, convert str to int for valueerror checking
        #004.3.1    boxChoice A
        #004.3.2    boxChoice B
        #004.3.3    boxChoice C
        #004.3.4    boxChoice D
        #004.3.5    boxChoice E
    #004.4 check if passed minimum wallet threshold 
    #004.5 turn incrementer here

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#000.0  functions
#000.1  print the number of tries left
def triesPrint(i):
    if i >= 2:
        print(i, 'tries left!!')
    else:
        print('Final chance; Last try!!')

#000.2  quit game when below minimum wallet amount
def minAmt(kx):
    print("You have fallen below the minimum wallet threshold! The game will end here.")
    if kx >= 2:
        print("You got to {} turns!!".format(kx))
    else:
        print("You got to {} turn!!".format(kx))
    raise SystemExit

#000.3  gm2 end of mode system exit
def gamemodeTwoOver(wallet):
    print("\n✨ Congratulations ✨ \nYou made it to the end of the Game Mode!")
    print("You made: £{}!!".format(wallet))
    raise SystemExit

#000.4.1  gm3 run out of turns, system exit
def gamemodeThreeTurns(wallet):
    print("\nYou have run out of turns! The game will end here.")
    print("You made: £{}!!".format(wallet))
    raise SystemExit

#000.4.2  gm3 reach million, system exit
def gamemodeThreeWin(wallet, kx):
    print("\n✨ Congratulations ✨ \nYou are a millionaire!!")
    print("You made £{} in only {} turns!!".format(wallet, kx))
    raise SystemExit

#000.5  gm4 lose streak, system exit  
def gamemodeFourLose(kx):
    print("\nYou have lost your winning streak! The game ends here.")
    print("You got {} guesses in a row!!".format(kx))
    if kx >= 25:
        print("You got more than 25 guesses in a row correct! ✨ Incredible!! ✨")
    elif (kx <= 24) and (kx >= 11):
        print("You got more than 10 guesses in a row correct! Impressive")
    elif (kx < 10) and (kx >= 1):
        print("You got less than 10 guesses! You can do better")
    else:
        print("You didn't get any guesses right?! That's not great, try again!")
    raise SystemExit

#000.6.1  gm5 bomb box, system exit
def gamemodeFiveBomb(wallet, kx):
    print("This box is the...\n[💣-BOMB BOX-💣]")
    print("You lose!")
    print("You made it to {} turns with £{} in your wallet!".format(kx, wallet))
    if kx >= 25:
        print("You made it past 25 turns! ✨ Incredible!! ✨")
    elif (kx <= 24) and (kx >= 11):
        print("You made it past 10 turns! Impressive")
    elif (kx < 10) and (kx >= 1):
        print("You made it past less than 10 turns! You can do better")
    else:
        print("You lost on your first turn?! That's not great, try again!")
    raise SystemExit

#000.6.2  gm5 other boxes, just text
def gamemodeFiveHalf():
    print("This box is the...\n[--HALF BOX--]")
    print("Your wallet amount will be halved!")
def gamemodeFiveFive():
    print("This box is the...\n[--+50% BOX--]")
    print("Your wallet amount will be multiplied by 50%!")
def gamemodeFiveDouble():
    print("This box is the...\n[🎉-DOUBLE BOX-🎉]")
    print("Your wallet amount will be doubled!")
    

#001.1  game setup
#001.1  name and age entry, system exit if underage
print("Welcome to the Program!!\nGame will begin here--")
userName = input("Please enter your name: ")
while True:
    try:   
        userAge = int(input("Please enter your age: "))
        if userAge < 18:
            print("Unable to continue program: User is below the legal age limit.\nProgram will now terminate")
            raise SystemExit(0)
        break
    except ValueError:
        print("Invalid age!! Please enter your age, using only numbers: ")

#001.2  gamemode choice and rules
print("Welcome to the game,", userName)
print("Game Mode 1: Endless Gamble - keep going until you run out of money!")
print("Game Mode 2: 15 Turn Frenzy - get as much money as possible in only 15 turns!")
print("Game Mode 3: Million Moneys - reach £1,000,000 in 25 turns!")
print("Game Mode 4: Winning Streak - keep going until you guess wrong, no money involved!")
print("Game Mode 5: Bomb Defusings - BONUS GAME - there are 10 boxes, some might double your wallet, some might halve it, and one will blow it all up!")

while True:
    try:   
        gameModeInp = int(input("Please enter '1', '2', '3', '4', or '5': "))
        if (gameModeInp < 1) or (gameModeInp > 5):
            raise ValueError
        break
    except ValueError:
        print("Invalid answer!! Please enter '1', '2', '3', '4', or '5': ")
        continue

if gameModeInp == 1:    
    print("\nYou have chosen Game Mode 1: Endless")
    print("How it works:\n✨ Choose a box to determine your starting wallet value.\n✨ Each round, place your bet before you see the randomly selected number [within budget].")
    print("✨ A randomly selected number between 1 and 100 will appear on the screen. Enter [1] for higher or [0] for lower depending on what you believe the answer to be.")
    print("✨ If you are correct, your bet will be doubled and returned to your wallet.\n✨ If you are incorrect, your bet will be taken away and you will lose the money.")
    print("✨ If you have only %10 of your starting wallet left, you will lose the game.\n✨ Keep playing until you have no money left. Get the highest number of turns!!")
    print("Also note:\n✨ If you win the previous round, you will be offered a chance to keep your previous doubled bet in play. If you choose to do so and win again, you will get an extra %25 gain.")
    print("✨ Every round, there is a 1/10 chance of a bonus box appearing. Select the correct box to be awarded bonus money!")
    print("\n")
elif gameModeInp == 2:
    print("\nYou have chosen Game Mode 2: 15 Turn Frenzy")
    print("How it works:\n✨ Choose a box to determine your starting wallet value.\n✨ Each round, place your bet before you see the randomly selected number [within budget].")
    print("✨ A randomly selected number will appear on the screen between 1 and 100. Enter [1] for higher or [0] for lower depending on what you believe the answer to be.")
    print("✨ If you are correct, your bet will be doubled and returned to your wallet.\n✨ If you are incorrect, your bet will be taken away and you will lose the money.")
    print("✨ If you have only %10 of your starting wallet left, you will lose the game.\n✨ You have 15 turns to get the most amount of money!!")
    print("\n")
elif gameModeInp == 3:
    print("\nYou have chosen Game Mode 3: Million Moneys")
    print("How it works:\n✨ Choose a box to determine your starting wallet value.\n✨ Each round, place your bet before you see the randomly selected number [within budget].")
    print("✨ A randomly selected number between 1 and 100 will appear on the screen. Enter [1] for higher or [0] for lower depending on what you believe the answer to be.")
    print("✨ If you are correct, your bet will be doubled and returned to your wallet.\n✨ If you are incorrect, your bet will be taken away and you will lose the money.")
    print("✨ If you have only %10 of your starting wallet left, you will lose the game.\n✨ Reach £1,000,000 before the turns reach 25! If you don't, the game will end.")
elif gameModeInp == 4:
    print("\nYou have chosen Game Mode 4: Winning Streak")
    print("How it works:\n✨ This game mode has no money involved.\n✨ Keep guessing if the number is higher or lower!\n✨ If you lose, the game ends. Your streak will be displayed.")
    print("✨ A randomly selected number between 1 and 100 will appear on the screen. Enter [1] for higher or [0] for lower depending on what you believe the answer to be.")
    print("\n")
elif gameModeInp == 5:
    print("\nYou have chosen the bonus game, Game Mode 5: Bomb Defusings")
    print("How it works:\n✨ Start with £1000.\n✨ You will have 5 boxes appear in front of you.")
    print("✨ One box will double your money.\n✨ One box will multiply your money by 50%.\n✨ One box will do nothing.\n✨ One box will half your money.")
    print("✨ The final box will be the bomb, if you choose this box, the game will end.\n✨ Your money gained and your number of turns will be displayed")
    print("\n")


#001.3  determine if random or set wallet used, if at all
if gameModeInp != 4:
    if gameModeInp == 5:
        wallet = 1000
        busFare = 10
        print("You have £{}! If you fall below £{}, the game will end.".format(wallet, busFare))
    else:
        print("Box [1]          Box [2]         Box [3]")
        wallet = random.randint(1, 1000)
        initialWallet = wallet
        busFare = (initialWallet * 0.1)
        while True:
            try:
                boxInp = int(input("Please select box [1], box [2], or box [3] by entering the number: "))
                if (boxInp < 1) or (boxInp > 3):
                    raise ValueError
                break
            except ValueError:
                print("Invalid answer!! Enter either '1', '2', or '3': ")
                continue
        print("You have chosen Box [{}]!".format(boxInp))
        print("Your starting amount is: £{}".format(initialWallet))
        print("Remember: if you fall below £{}, you lose! Just enough to take the bus home.".format(int(busFare)))

#001.4  determine if gamemode runs within main higherlower loop, 002
if gameModeInp >= 4:
    gameplay = False
else:
    gameplay = True

#001.5  counters for various things used in all gamemode loops
i = 15  #counts down for gm2
ii = 25 #counts down for gm3
jx = 0  #once i, ii matches jx, gamemode is over
kx = 0  #counts up for gm1, gm3, gm4, gm5 when game is over, turn number is displayed
wx = 0  #win streak counter for previousbetdouble

doubleOrN = False

#002.0 main loop begins
#002.1 gm1, gm2, gm3 runs here in gameplay == true while loop
while gameplay == True:

    #002.2  gm1 winning streak check
    while gameModeInp == 1:
        if wx > 2:
            print("You're on a winning streak!")
            while True:
                try:
                    upTheBet = int(input("Do you want to get more back on your previous bet?? Type [1] for Yes, [0] for No: "))
                    if (upTheBet < 0) or (upTheBet > 1):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid answer!! Enter 1 or 0: ")
                    continue
            if upTheBet == 1:
                doubleOrN = True
            else:
                doubleOrN = False
        break

    #002.3  gm2 and gm3 tries check + gm3 wallet million check
    if gameModeInp == 2:
        triesPrint(i)    
        if i == jx:
            gamemodeTwoOver(wallet)
    if gameModeInp == 3:
        triesPrint(ii)
        if ii == jx:
            gamemodeThreeTurns(wallet)
        if wallet >= 1000000:
            gamemodeThreeWin(wallet, kx)

    #002.4  counter increments + number randomiser
    i -= 1
    ii -= 1
    randNum = random.randint(1, 100)
    kx += 1
    nextRand = random.randint(1, 100)

    print("\nYou currently have: £{}".format(wallet))

    #002.5 check if doubleorn, if not then place bets
    if doubleOrN == False:
        while True:
            try:
                userBet = int(input("Place your bets!!: "))
                if userBet > wallet:
                    raise ValueError
                break
            except ValueError:
                print("Invalid answer!! You can't bet more than you have. Try again: ")
                continue

    print("The number is...\n[-----------{}-----------]".format(randNum))

    #002.6  enter higher or lower guess
    while True:
        try:
            highLow = int(input("Will the next number be Higher [1] or Lower [0]???: "))
            if (highLow < 0) or (highLow > 1):
                raise ValueError
            break
        except ValueError:
            print("Invalid answer!! Enter 1 or 0: ")
            continue

    #002.7.1    1st num less than 2nd num
    while randNum < nextRand:
        if highLow == 1:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            wx += 1
            if doubleOrN == True:
                wallet -= userBet
                userBet *= 1.25
                wallet += userBet
            else:
                wallet -= userBet
                userBet *= 2
                wallet += userBet
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            wallet -= userBet
            wx = 0
            doubleOrN = False
            break

    #002.7.2    1st num more than 2nd num
    while randNum > nextRand:
        if highLow == 0:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            wx += 1
            if doubleOrN == True:
                wallet -= userBet
                userBet *= 1.25
                wallet += userBet
            else:
                wallet -= userBet
                userBet *= 2
                wallet += userBet
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            wallet -= userBet
            wx = 0
            doubleOrN = False
            break       
        

    print("You now have £{} in your wallet!".format(wallet))

    #002.8  check if pass min wallet threshold
    if busFare > wallet:
        minAmt(kx)

    #002.9.0    mystery box appear chance
    if (gameModeInp == 1) or (gameModeInp == 3):
        mysteryBox = random.randint(1, 5)
        #002.9.1  mystery box 1/5 chance of appearing
        if mysteryBox == 1:
            print("\n❗ Surprise ❗\nYou have won the chance of winning a prize!!")
            print("One box will give you a lump sum of upto £1500, another will double your wallet, and the rest do nothing!")

            #002.9.2  randomise boxes, make sure they are different
            mysteryChoiceGift = random.randint(1, 5)
            mysteryChoiceDouble = random.randint(1, 5)

            while mysteryChoiceGift == mysteryChoiceDouble:
                mysteryChoiceGift = random.randint(1, 5)
                mysteryChoiceDouble = random.randint(1, 5)

            #002.9.3    user input box choice
            while True:
                try:
                    mysteryChoiceUser = int(input("Choose a number between 1 and 5: "))
                    if (mysteryChoiceUser < 1) or (mysteryChoiceUser > 5):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid answer!! Enter a number between 1 and 5: ")
                    continue 

            #002.9.4    which box chosen, break to main higher lower loop, continue game
            if mysteryChoiceGift == mysteryChoiceUser:
                print("🎉 You chose the LUMP SUM box! 🎉")
                lumpSumBox = random.randint(1, 1500)
                wallet += lumpSumBox
                print("You won £{}! It has been added to your wallet.".format(lumpSumBox))
            elif mysteryChoiceDouble == mysteryChoiceUser:
                print("🎉 You chose the DOUBLE WALLET box! 🎉")
                wallet *= 2
                print("Your wallet has been doubled.")
            else:
                print("Bad luck! You haven't chosen a winning box.")

#003.0  start gm4
while gameModeInp == 4:
    
    #003.1  number randomiser
    randNum = random.randint(1, 100)
    nextRand = random.randint(1, 100)
    print("\nThe number is...\n[-----------{}-----------]".format(randNum))

    #003.2  user choice if higher lower
    while True:
        try:
            highLow = int(input("Will the next number be Higher [1] or Lower [0]???: "))
            if (highLow < 0) or (highLow > 1):
                raise ValueError
            break
        except ValueError:
            print("Invalid answer!! Enter 1 or 0: ")
            continue

    #003.3.1    1st num less than 2nd num, if wrong quit game
    while randNum < nextRand:
        if highLow == 1:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            gamemodeFourLose(kx)

    #003.3.2    1st num more than 2nd num, if wrong quit game
    while randNum > nextRand:
        if highLow == 0:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            gamemodeFourLose(kx)         

    #003.4  turn incrementer
    kx += 1

#004.0  determine variable and gm5 loop commence
boxChoiceInt = 0
wallet = 1000
minLimit = 10

while gameModeInp == 5:
    
    #004.1  boxes assigned random and different value from 0-4
    boxRand = random.sample(range(0, 5), 5)
    boxA = boxRand[0]
    boxB = boxRand[1]
    boxC = boxRand[2]
    boxD = boxRand[3]
    boxE = boxRand[4]

    print("\nYou currently have £{}".format(wallet))

    #004.2  user box choice, str.upper, convert str to int for valueerror check
    while True:
        try:
            boxChoice = input("Which box will you choose?: ").upper()
            if boxChoice.upper() == 'A':
                boxChoiceInt = 0
            elif boxChoice.upper() == 'B':
                boxChoiceInt = 1
            elif boxChoice.upper() == 'C':
                boxChoiceInt = 2
            elif boxChoice.upper() == 'D':
                boxChoiceInt = 3
            elif boxChoice.upper() == 'E':
                boxChoiceInt = 4
            if (int(boxChoiceInt) < 0) or (int(boxChoiceInt) > 4):
                raise ValueError
            elif type(boxChoice) == int:
                raise ValueError
            break
        except ValueError:
            print("Invalid answer!! Enter [A], [B], [C], [D], or [E]: ")
            continue

    print("You have chosen Box [{}]!".format(boxChoice))

    #004.3.1    box choice a
    if boxChoice == 'A':
        if boxA == 0:
            gamemodeFiveBomb(wallet, kx)
        elif boxA == 1:
            gamemodeFiveHalf()
            wallet *= 0.5
        elif boxA == 3:
            gamemodeFiveFive()
            wallet *= 1.5
        elif boxA == 4:
            gamemodeFiveDouble()
            wallet *= 2
        else:
            print("This is an empty box! Keep going!!")

    #004.3.2    box choice b
    if boxChoice == 'B':
        if boxB == 0:
            gamemodeFiveBomb(wallet, kx)
        elif boxB == 1:
            gamemodeFiveHalf()
            wallet *= 0.5
        elif boxB == 3:
            gamemodeFiveFive()
            wallet *= 1.5
        elif boxB == 4:
            gamemodeFiveDouble()
            wallet *= 2
        else:
            print("This is an empty box! Keep going!!")

    #004.3.3    box choice c
    if boxChoice == 'C':
        if boxC == 0:
            gamemodeFiveBomb(wallet, kx)
        elif boxC == 1:
            gamemodeFiveHalf()
            wallet *= 0.5
        elif boxC == 3:
            gamemodeFiveFive()
            wallet *= 1.5
        elif boxC == 4:
            gamemodeFiveDouble()
            wallet *= 2
        else:
            print("This is an empty box! Keep going!!")

    #004.3.4    box choice d
    if boxChoice == 'D':
        if boxD == 0:
            gamemodeFiveBomb(wallet, kx)
        elif boxD == 1:
            gamemodeFiveHalf()
            wallet *= 0.5
        elif boxD == 3:
            gamemodeFiveFive()
            wallet *= 1.5
        elif boxD == 4:
            gamemodeFiveDouble()
            wallet *= 2
        else:
            print("This is an empty box! Keep going!!")

    #004.3.5    box choice e
    if boxChoice == 'E':
        if boxE == 0:
            gamemodeFiveBomb(wallet, kx)
        elif boxE == 1:
            gamemodeFiveHalf()
            wallet *= 0.5
        elif boxE == 3:
            gamemodeFiveFive()
            wallet *= 1.5
        elif boxE == 4:
            gamemodeFiveDouble()
            wallet *= 2
        else:
            print("This is an empty box! Keep going!!")

    #004.4  check for minimum wallet threshold
    if wallet <= minLimit:
        print("You have fallen below £10! The game will end here.")
        minAmt(kx)

    #004.5  turn incrementer
    kx += 1