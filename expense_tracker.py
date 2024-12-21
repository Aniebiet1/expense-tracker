from datetime import datetime
import csv
from collections import defaultdict

# File to store expenses
FILE_NAME = "expenses.csv"


def add_expenses():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the category (e.g., Food Transport, Entertainment): ")
    description = input("Enter a short description: ")
    date = input("Emter the date (YYYY_MM_DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m--%d")

    expense = [date, category, amount, description]
    save_expense(expense)
    print("Expense added successfully!\n")


def save_expense(expenses):
    with open(FILE_NAME, "a") as file:
        writer = csv.writer(file)
        writer.writerow(expenses)

    print("Expense saved successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            expenses = list(reader)

        print(
            f"\n{'Date':<12} | {'Category':<15} | {'Amount':<10} | {'Description':<20}"
        )
        print("-" * 65)
        total = 0
        for expense in expenses:
            if len(expense) < 4:
                continue
            total += float(expense[2])
            print(
                f"{expense[0]:<12} | {expense[1]:<15} | {expense[2]:<10} | {expense[3]:<20}"
            )
        print("-" * 65)
        print(f"Total expenses: {total}\n")

    except FileNotFoundError:
        print("No expenses found!\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
