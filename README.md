![Header Image](https://github.com/DiogoPoletti/Guess-The-Number/blob/main/Documentation/HeaderImage2.png)

# Guess The Number

## Description
A Python-based program that prompts the user to guess the number randomly generated by the program using the *input* method. The program will then run the user's answer through conditions to compare the answer with the real number. If the number is higher, the program will prompt the user again to display a message asking for a lower number. The opposite will display a message asking for a higher number. If the user wants to exit, typing 0 will trigger another condition where the user will be prompted to enter either *Y* or *N* to exit or not.

## Screenshot
![Game Running](https://github.com/DiogoPoletti/Guess-The-Number/blob/main/Documentation/GessTheNumber.gif)

> The number generated was displayed in the IDLE for demonstration purposes.

## What have I learned
Creating this program enabled me to practice a few aspects:
* Improve with Python syntax and good practices when coding.
* Use *random* library and learn a few functions.

## Code highlight
The following block of code is the entire program where loopings and conditions were triggered.

```
//Checks each input from the user
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
```


> This is a companion project to Python 3.8 Full Stack Masterclass, check out the full course at www.udemy.com


![Footer Image](https://github.com/DiogoPoletti/Guess-The-Number/blob/main/Documentation/FooterImage.png)
