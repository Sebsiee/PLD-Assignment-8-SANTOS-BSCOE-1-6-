import random

def introduction():
    print("Welcome to my Program 2 - Guess The Number!")

def lottery():
    generatedNumber = random.randint(0,100)
    print(f"{generatedNumber}")
    count = 0
    while True:
        try:
            userNumber = int(input("Input number: ")) 
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


introduction()
lottery()

    
    