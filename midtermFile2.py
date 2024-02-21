# 2. Create a program that allows you to add items to a list and recall its contents
# The recall of the list should print the items individually, without any
# additional marks (hint: do not just print the list)
# 15 points
# Enter your code here:

my_list= []

while True:
    choice = input("Enter 'add' to add an item, 'print' to print the list:  ")

    if choice == "add":
        item = input("Enter an item to add to the list: ")
        my_list.append(item)
        print("Item added successfully!")

    elif choice == "print":
        for item in my_list:
            print("Here's your list", item)
    else:
        print("Not a choice! Please try again.")