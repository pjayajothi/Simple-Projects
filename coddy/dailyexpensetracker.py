# Build a simple program to manage daily expenses.
# The user can add, view, and clear expenses, as well as calculate the total and average.
# This project reinforces basic programming concepts like lists, loops, and functions in a practical, real-life scenario.
print("Welcome to the Daily Expense Tracker!\n")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expenses = []
while True: # Creating an infinite loop
    choice = int(input()) # Getting a choice from the user
    if choice == 1:
        expense = float(input()) # New Expense from user
        expenses.append(expense)
        print("Expense added successfully!")
    elif choice == 2:
        if not expenses:  # Empty List
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for bullet, expense in enumerate(expenses, start=1):
                print(f"{bullet}. {expense}")
    elif choice == 3:
        if not expenses:  # Empty List
            print("No expenses recorded yet.")
        else:
            print("Total expense:", sum(expenses)) # Sum of all expenses in list
            print("Average expense:", sum(expenses)/len(expenses)) # Average of all expenses in list
    elif choice == 4:
        expenses.clear() # CLear all vaues from list
        print("All expenses cleared.")
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.") # In case we get an invalid option from user
