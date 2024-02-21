import math
import random

# 3. Create a menu using if, elif, else statements.
# The menu should have four options:
# Option 1 should add two numbers, inputs from the user
# Option 2 should get the square of one number, user input
# Option 3 should give a famous quote at random (3+ quotes)
# Option 4 should exit the program
# Anything else is up to you.
# 20 points
print(""""  Welcome to Mayfness options!


Here's a list of items you can pick from: 

Option 1. Math Related Operation
Option 2. A Fancier Math Operation
Option 3. Some Words Of Wisdom
Option 4. Try It And See ;)
Option 5. This Is Definitely A Surprise (Even For Me)

""")

option = int(input("Enter your option number: "))

if option == 1:
    option1num = int(input("Enter your first option number: "))
    option1num2 = int(input("Enter your second option: "))
    option1num3 = option1num + option1num2
    print("TA-DA! Here's the sum of your numbers: ", option1num3)


elif option == 2:
    option2num1 = int(input("Enter a number: "))
    option2calc = math.sqrt(option2num1)
    print(f"The square root of ${option2num1} is ${option2calc:.2f}")


elif option == 3:
    quotes = [
        "Life is suffering. It is hard. The world is cursed. But still, you find reasons to keep living.",       "The way to get started is to quit talking and begin doing. - Walt Disney",
        "It does not do to dwell on dreams and forget to live, remember that.",
        "We each need to find our own inspiration. Sometimes it's not easy.",
        "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light."
    ]
    quote = random.choice(quotes)
    print("Here's a famous quote for you: ")
    print(quote)

elif option == 4:
    print("Whoops! You broke me D: ")

elif option == 5:
    words = ["Super", "Mighty", "Incredible", "Fantastic", "Amazing", "Dynamic"]
    nouns = ["Hero", "Avenger", "Champion", "Defender", "Guardian", "Sentinel"]

    superhero_name = random.choice(words) + " " + random.choice(nouns)
    print("Your superhero name is:", superhero_name)

else:
    print("That's not an option! >:(")

# Enter your code here: