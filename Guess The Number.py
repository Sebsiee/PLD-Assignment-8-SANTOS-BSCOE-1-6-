import random

def introduction():
    print("Welcome to my Program 2 - Guess The Number!")

def guesstheNumber():
    generatedNumber = random.randint(0,100)
    count = 0
    while True:
        try:
            userNumber = int(input("Input your number: ")) 
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if int(userNumber) < generatedNumber:
            print("Greater than")
            count+=1 
            continue
        elif int(userNumber) > generatedNumber:
            print("Less than")
            count+=1 
            continue
        else:
            print("You guessed correctly!")
            print(f"You tried {count} times.")
            break

def goodbye():
    print()
    print("Thank you for using my program!")

introduction()
guesstheNumber()
goodbye()

    
    