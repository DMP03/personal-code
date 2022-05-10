import random
#Higher or Lower basic gambling program
#000.1 game setup, name and age (under 18s are kicked out)
#000.2 game mode, input 1 or 2

#001.1 gamemode chosen rules and information
#001.2 box chosen, wallet initiated
#001.3 define procedure tries counter

#002.1 gameplay true, main loop initialised


#000.1 game setup

def triesPrint(i):
    if i >= 2:
        print(i, 'tries left!!')
    else:
        print('Final chance; Last try!!')

def minAmt(kx):
    print("You have fallen below the minimum wallet threshold! The game will end here.")
    if kx >= 2:
        print("You got to {} turns!!".format(kx))
    else:
        print("You got to {} turn!!".format(kx))
    raise SystemExit

def gamemodeTwoOver(wallet):
    print("\n✨ Congratulations ✨ \nYou made it to the end of the Game Mode!")
    print("You made: £{}!!".format(wallet))
    raise SystemExit

def gamemodeThreeTurns(wallet):
    print("\nYou have run out of turns! The game will end here.")
    print("You made: £{}!!".format(wallet))
    raise SystemExit

def gamemodeThreeWin(wallet, kx):
    print("\n✨ Congratulations ✨ \nYou are a millionaire!!")
    print("You made £{} in only {} turns!!".format(wallet, kx))
    raise SystemExit
        
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

def gamemodeFiveHalf():
    print("This box is the...\n[--HALF BOX--]")
    print("Your wallet amount will be halved!")
    

def gamemodeFiveFive():
    print("This box is the...\n[--+50% BOX--]")
    print("Your wallet amount will be multiplied by 50%!")
    

def gamemodeFiveDouble():
    print("This box is the...\n[🎉-DOUBLE BOX-🎉]")
    print("Your wallet amount will be doubled!")
    


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

#checklist
#gm1 streak bet increase, learn how to do it
#gm3 new game mode, keep going until you lose, no money 


#001.1 gamemode chosen rules and information


#001.2 box chosen, wallet initialised
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



if gameModeInp >= 4:
    gameplay = False
else:
    gameplay = True

i = 15  #counts down for gm2
ii = 25 #counts down for gm3
jx = 0  #once i, ii matches jx, gamemode is over
kx = 0  #counts up for gm1, gm3, gm4, gm5 when game is over, turn number is displayed
wx = 0  #win streak counter for previousbetdouble

doubleOrN = False


while gameplay == True:

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

    i -= 1
    ii -= 1
    randNum = random.randint(1, 100)

    print("\nYou currently have: £{}".format(wallet))
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
    kx += 1

    nextRand = random.randint(1, 100)

    while True:
        try:
            highLow = int(input("Will the next number be Higher [1] or Lower [0]???: "))
            if (highLow < 0) or (highLow > 1):
                raise ValueError
            break
        except ValueError:
            print("Invalid answer!! Enter 1 or 0: ")
            continue

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

    if busFare > wallet:
        minAmt(kx)

    if (gameModeInp == 1) or (gameModeInp == 3):
        mysteryBox = random.randint(1, 5)
        if mysteryBox == 1:
            print("\n❗ Surprise ❗\nYou have won the chance of winning a prize!!")
            print("One box will give you a lump sum of upto £1500, another will double your wallet, and the rest do nothing!")
            mysteryChoiceGift = random.randint(1, 5)
            mysteryChoiceDouble = random.randint(1, 5)

            while mysteryChoiceGift == mysteryChoiceDouble:
                mysteryChoiceGift = random.randint(1, 5)
                mysteryChoiceDouble = random.randint(1, 5)

            while True:
                try:
                    mysteryChoiceUser = int(input("Choose a number between 1 and 5: "))
                    if (mysteryChoiceUser < 1) or (mysteryChoiceUser > 5):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid answer!! Enter a number between 1 and 5: ")
                    continue 

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

while gameModeInp == 4:
    
    randNum = random.randint(1, 100)
    nextRand = random.randint(1, 100)
    print("The number is...\n[-----------{}-----------]".format(randNum))

    while True:
        try:
            highLow = int(input("Will the next number be Higher [1] or Lower [0]???: "))
            if (highLow < 0) or (highLow > 1):
                raise ValueError
            break
        except ValueError:
            print("Invalid answer!! Enter 1 or 0: ")
            continue

    while randNum < nextRand:
        if highLow == 1:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            gamemodeFourLose(kx)

    while randNum > nextRand:
        if highLow == 0:
            print("✨ Congratulations ✨ \nYou guessed correctly! The answer is: [---{}---]".format(nextRand))
            break
        else:
            print("Incorrect!! The answer is: {}".format(nextRand))
            gamemodeFourLose(kx)         

    kx += 1

boxChoiceInt = 0
wallet = 1000
minLimit = 10

while gameModeInp == 5:
    

    boxRand = random.sample(range(0, 5), 5)
    boxA = boxRand[0]
    boxB = boxRand[1]
    boxC = boxRand[2]
    boxD = boxRand[3]
    boxE = boxRand[4]

    print("\nYou currently have £{}".format(wallet))

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

    if wallet <= minLimit:
        print("You have fallen below £10! The game will end here.")
        minAmt(kx)

    kx += 1
