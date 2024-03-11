#TODO: 1st input not working/ not going into the list
#TODO: get rid of duplicate on list (for loop)


import random
#word guesses/ list of words

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = [ "apple",
    "river",
    "chair",
    "cloud",
    "music",
    "ocean",
    "tiger",
    "green",
    "heart",
    "smile",
    "pizza",
    "lemon",
    "fairy",
    "house",
    "bread"]

#call random word from list of words to check conditions
MAX_WRONG = len(HANGMANPICS) - 1
word = random.choice(word_list)
correct_guess = 0
print(word)
used = []
guess = input("Guess a letter: ")


#check if the guess letter is in word x in wordlist

while correct_guess < MAX_WRONG:
        if guess in word:

            print("Correct!")
            print("You have used these letters", used)
            print(correct_guess)
            correct_guess = correct_guess
            guess = input("Guess a letter: ")
            used.append(guess)
        elif guess not in word:

            print(HANGMANPICS[correct_guess])
            print("Incorrect!")
            print("You have used these letters", used)
            print(correct_guess)
            correct_guess += 1
            guess = input("Guess a letter: ")
            used.append(guess)

if correct_guess == MAX_WRONG:
    print("You ded!")
# Exit the game when  guesses <= 1
if correct_guess == 1:
    print("You won!")
    exit()





