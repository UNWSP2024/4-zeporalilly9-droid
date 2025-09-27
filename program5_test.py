# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.
#Author: Zepora
#Date: 9/26/2025
#Title: Monthly Budget Tracker

budget = 0.0
difference = 0.0
spent = 1.0         #initialize for while loop
total = 0.0

# Program #5: Bank Balance

budget = float(input("Enter your budget for the month: "))

total_expenses = 0.0

more_expenses = "yes"
while more_expenses.lower() == "yes":
    expense = float(input("Enter an expense amount: "))
    total_expenses += expense
    more_expenses = input("Do you have another expense? (yes/no): ")

if total_expenses > budget:
    print("You are over budget by", total_expenses - budget)
else:
    print("You are under budget by", budget - total_expenses)