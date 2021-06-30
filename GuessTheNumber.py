# Create a the program that will allow you as many guesses to pick 
# a number between 1 and 1000. 
# Use a while loop to
# allow as many guesses as necessary.
# Lookup "import random" and use that to generate the number.
# http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
# https://docs.python.org/2/library/random.html
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess. 

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
    