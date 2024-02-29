"""

For this version, you have two players. Player 1 and Player 2.
You will need to create if statements (and probably nesting)
to decide who has won, lost or if the game is a tie.
Make it fun and add emojis or epic comments as your
players battle it out.
Keep it simple for you.
Don't expect the user to type in the words rock, paper, scissors.
Instead, encourage them to use R, P, or S.
(Can you ensure the user can still input an option even if it is typed in wrong?)
"""

print("Welcome to Rock Paper & Scissors!")
player1_name = input("What is your nickname Player 1?")
player2_name = input("What is your nickname Player 2?")
player1_score = 0
player2_score = 0
player1_move = ("")
player2_move = ("")
#this prints the user's option
#just makes it pretty to see what it is




#this is is whatever condition is met (including ties)
while player1_score < 3 and player2_score < 3:
    player1 = input("What would you like to play Player 1?")
    player1_move = player1.capitalize()
    player2 = input("What would you like to play Player 2?")
    player2_move = player2.capitalize()

    if player1_move == "P" and player2_move == "R":
        player1_score += 1
        print("✋vs✊")
        print("You won!",player1_name)
        print("You got!",player1_score,"points")
    elif player1_move == "R" and player2_move == "S":
        player1_score += 1
        print("✊vs️✌️")
        print("You won!",player1_name)
        print("You got!",player1_score,"points")
    elif player1_move == "S" and player1_move == "P":
        player1_score += 1
        print("️✌️vs✋")
        print("You won!",player1_name)
        print("You got!",player1_score,"points")
    elif player2_move == "P" and player1_move == "R":
        player2_score += 1
        print("✋vs✊")
        print("You won!",player2_name)
        print("You got!",player2_score,"points")
    elif player2_move == "R" and player1_move == "S":
        player2_score += 1
        print("✊vs️✌️")
        print("You won!",player2_name)
        print("You got!",player2_score,"points")
    elif player2_move == "S" and player1_move == "P":
        player2_score += 1
        print("️✌️vs✋")
        print("You won!",player2_name)
        print("You got!",player2_score,"points")
    elif player2_move == "P" and player1_move == "P":
        print("✋vs✋")
        print("You tied!",player1_name ,player2_name)
    elif player2_move == "R" and player1_move == "R":
        print("✊vs️✊")
        print("You tied!", player1_name, player2_name)
    elif player2_move == "S" and player1_move == "S":
        print("️✌️vs✌️")
        print("You tied!", player1_name, player2_name)






