import random

def introduction():
    print("Welcome to my Program 1 - Lottery!")

def lottery():
    firstLottery = random.randint(0,9)
    secondLottery = random.randint(0,9)
    thirdLottery = random.randint(0,9)
    while True:
            try:
                firstGuess = int(input("Input 1st Number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break
    while True:
            try:
                secondGuess = int(input("Input 2nd Number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break
    while True:
            try:
                thirdGuess = int(input("Input 3rd Number: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            break
    if int(firstGuess) == firstLottery or int(firstGuess) == secondLottery or int(firstGuess) == thirdLottery:
        fg1 = 1
    else:
        fg1 = 0
    if int(secondGuess) == secondLottery or int(secondGuess) == firstLottery or int(secondGuess) == thirdLottery:
        fg2 = 1
    else:
        fg2 = 0
    if int(thirdGuess) == thirdLottery or int(thirdGuess) == firstLottery or int(thirdGuess) == secondLottery:
        fg3 = 1
    else:
        fg3= 0
    points = fg1 + fg2 + fg3
    if points == 3:
        print("You won!")
    elif points == 2:
        print("You guessed 2 numbers correctly. So close!")
        print(f"The winning numbers are: {firstLottery}, {secondLottery} & {thirdLottery}")
    elif points == 1:
        print("You guessed 1 correctly.")
        print(f"The winning numbers are: {firstLottery}, {secondLottery} & {thirdLottery}")
    else:
        print("You lost.")
        print(f"The winning numbers are: {firstLottery}, {secondLottery} & {thirdLottery}")
    while True:
        tryAgain = str(input("Would you like to try again? \nY/N: "))
        if tryAgain == "Y" or tryAgain == "y":
            print("Goodluck!")
            lottery()       
            break   
        elif tryAgain == "N" or tryAgain == "n":
            print("Try again next time!")
            break
        else:
            print("Sorry, I didn't understand that.")
            continue

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
lottery()
goodbye()