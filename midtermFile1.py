# Midterm Exam - Answer the following three questions within 40 minutes
# 1. Create a loop to ask the user for input. The input should be an integer.
# Take the number from the input and add any integers that came before it, all the way to 0
# Ex. If you choose 5 as input, the loop should add 5, 4, 3, 2, 1, and 0 together.
# 5 points
# Enter your code here:
user_input = int(input("Enter a number here: "))
total = 0
while user_input != 0:
    total += user_input
    user_input = user_input - 1
print(total)