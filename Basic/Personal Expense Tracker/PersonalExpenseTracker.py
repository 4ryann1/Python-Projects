expenses = []


# Add Expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").title()
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


# View Expenses
def view_expenses():

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    print("\n----- All Expenses -----")

    for expense in expenses:
        print("Amount:", expense["amount"])
        print("Category:", expense["category"])
        print("Description:", expense["description"])
        print("------------------------")


# Total Expenses
def total_expenses():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expenses:", total)


# Highest Expense
def highest_expense():

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    highest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n----- Highest Expense -----")
    print("Amount:", highest["amount"])
    print("Category:", highest["category"])
    print("Description:", highest["description"])


# Category-wise Spending
def category_spending():

    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount

        else:
            categories[category] = amount

    print("\n----- Category-wise Spending -----")

    for category, amount in categories.items():
        print(category, ":", amount)


# Main Program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Category-wise Spending")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        category_spending()

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")