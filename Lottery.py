import random

def introduction():
    print("Welcome to my Program 1 - Lottery!")

def lottery():
    firstLottery = random.randint(0,9)
    secondLottery = random.randint(0,9)
    thirdLottery = random.randint(0,9)
    firstGuess = int(input("Input 1st Number: "))
    secondGuess = int(input("Input 2nd Number: "))
    thirdGuess = int(input("Input 3rd Number: "))
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
    else:
        print("You lost.")

introduction()
lottery()