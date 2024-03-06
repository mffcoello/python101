#TOD0: account for letter repetition (need a for loop)
#TODO account for reptitive tries
#TODO change the print so it looks more like the game


import random
#word guesses/ list of words

word_list = ["mayfness", "apple", "airplane","ashes" ]

#call random word from list of words to check conditions
word = random.choice(word_list)
guess = input("Guess a letter: ")
correct_guess = len(word)
print(word)
user_guess = len(guess)
#check if the guess letter is in word x in wordlist

while correct_guess != 0:
        if guess in word:
            correct_guess -= 1
            print("Correct!")
            print(correct_guess)
            guess = input("Guess a letter: ")
        elif guess not in word:
            correct_guess = correct_guess
            print("Incorrect!")
            print(correct_guess)
            guess = input("Guess a letter: ")
# condition if already tried this letter

 # if guess == guess:
# correct_guess = correct_guess
# print("you already tried that!")

# Exit the game when  guesses <= 1
        if correct_guess == 1:
            print("You won!")
            exit()




