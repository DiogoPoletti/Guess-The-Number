
import random

limit = 1000
randomNumber = random.randint(1,1000)

print(randomNumber)

guess = 0

while guess != randomNumber:
    guess = int(input("Guess a number between 1 and 10000: "))
    
    if guess == 0:
        exit = input("Are you sure you want to leave? (Y/N)").upper()
        if exit == 'Y':
            print("Thanks for playing!!")
            break
        else:
             continue
    
    elif guess == randomNumber:
        print("That's the correct number.")

    elif guess > randomNumber:
        print("Wrong number, aim lower.")
        continue

    elif guess < randomNumber:
        print("Wrong number, aim higher.")
        continue

    else:
        print("Enter a number please!")
        continue
    