import random

def introduction():
    print("Welcome to my Program 2 - Guess The Number!")

def lottery():
    generatedNumber = random.randint(0,100)
    while True:
        try:
            userNumber = int(input("Input number: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if int(userNumber) < generatedNumber:
            print("Greater than")
            continue
        elif int(userNumber) > generatedNumber:
            print("Less than")
            continue
        else:
            print("You guessed correctly!")
            break

introduction()
lottery()

    
    