# TODO: establish range for random number
#TODO: function for random number
#TODO: Set guess boolean to false
#TODO: loop asks input and we determine number
#TODO:conditions + boolean to true so it doesn't loop forever
#TODO: nicetohave numbers you have guessed printed
#TODO: can only have 3 tries
#TODO: Exit at 3 tries

import random

MAX_TRIES = 2
guessNumber = False
number = random.randint(1, 30)
correctguess = 0
used = []
print(number)

print('WELCOME TO GUESS THE NUMBER!')
print('I am thinking of a number between 1 and 30')
guess = int(input('Type your number: '))


while correctguess < MAX_TRIES and guess != number:
    if guess in used:
        correctguess += 1
        print("You already used that number!")
    else:
        used.append(guess)

    if guess > 30:
        correctguess += 1
        print("Not valid!")
        guess = int(input('Try a different number: '))


    if guess > number:
        correctguess += 1
        print("Too high!")
        guess = int(input("Guess a number between 1 and 30: "))

    elif guess < number:
        correctguess += 1
        print("Too low!")
        guess = int(input("Guess a number between 1 and 30: "))

    elif guess == number:
        guessNumber = True
        print("Congratulations!")



if correctguess == MAX_TRIES:
    print("You're out of guesses!")
    exit()
