# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:33:58 2024

@author: Jacob White
"""

import csv
from datetime import datetime

# Store expenses/incomes in a list of dictionaries
records = []

# Load records from CSV (if available)
def load_data(file_name="expenses.csv"):
    try:
        with open(file_name, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Amount'] = float(row['Amount'])  # Convert amount to float
                records.append(row)
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")

# Save records to CSV
def save_data(file_name="expenses.csv"):
    with open(file_name, mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Amount", "Type", "Category"])
        writer.writeheader()
        writer.writerows(records)

# Add a new entry (income or expense)
def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")
    amount = float(input("Enter amount: "))
    type_ = input("Enter type (Income/Expense): ").capitalize()
    category = input("Enter category (e.g., Food, Rent, Salary): ").capitalize()

    record = {"Date": date, "Amount": amount, "Type": type_, "Category": category}
    records.append(record)
    print("Entry added successfully!")

# View all records
def view_records():
    if not records:
        print("No records to display.")
        return

    print("\nAll Entries:")
    for record in records:
        print(f"{record['Date']} - {record['Category']} - {record['Type']}: ${record['Amount']:.2f}")
    print()

# Get a summary (total income, expenses, and balance)
def summary():
    total_income = sum(r['Amount'] for r in records if r['Type'] == "Income")
    total_expense = sum(r['Amount'] for r in records if r['Type'] == "Expense")
    balance = total_income - total_expense

    # Print the summary with clear formatting
    print("\n=== Summary ===")
    print(f"Total Income:   ${total_income:,.2f}")
    print(f"Total Expense:  ${total_expense:,.2f}")
    print(f"Balance:        ${balance:,.2f}\n")


# Main menu
def menu():
    load_data()  # Load previous data if available

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Entry")
        print("2. View Records")
        print("3. Summary")
        print("4. Save & Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_records()
        elif choice == "3":
            summary()
        elif choice == "4":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
