""""Write a program with total change amount as an integer input,
and output the change using the fewest coins,
one coin type per line. The coin types are
Dollars, Quarters, Dimes, Nickels, and Pennies.
Use singular and plural coin names as appropriate,
like 1 Penny vs. 2 Pennies."""


change = int(input("Enter the amount of Money: "))

change_dollar = change // 100
change_store_dollar = change - (change_dollar * 100)
if change_dollar == 1:
   print("There is ", change_dollar, "dollar")
elif change_dollar >= 2:
   print("There are ",change_dollar, "dollars")

change_quarter = change_store_dollar // 25
change_store = change_store_dollar - (change_quarter * 25)
if change_quarter == 1:
   print("There is ", change_quarter, "quarter")
elif change_quarter >= 2:
   print("There are ", change_quarter, "quarters")

change_dime = change_store // 10
change_store2 = change_store - (change_dime * 10)
if change_dime == 1:
   print("There is ",change_dime, "dime")
elif change_dime >= 2:
   print("There are ", change_dime, "dimes")

change_nickel = change_store2 // 5
change_store3 = change_store2 - (change_nickel * 5)
if change_nickel == 1:
   print("There is ",change_nickel, "nickel")
elif change_nickel >= 2:
   print("There are ", change_nickel, "nickels")

change_penny = change_store3 // 1
if change_penny == 1:
   print("There is ",change_penny, "penny")
elif change_penny >= 2:
   print("There are ", change_penny, "pennies")

if change == 0:
   print("No change")































