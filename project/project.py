import sys, os, csv
from datetime import datetime

TRANSACTIONS_FILE = "transactions.csv"
VALID_INCOME_CATEGORIES = ["salary", "freelance", "investment", "business"]
VALID_EXPENSE_CATEGORIES = ["food", "rent", "utilities", "entertainment", "transportation", "healthcare", "education", "shopping"]

# main entry for the application
def main():
    print("Welcome to CS50P Finances Application")
    # Dispatch table mapping options to functions
    options = {
        "1": add_transaction,
        "2": show_balance,
        "3": generate_report,
        "4": exit_program
    }

    while True:
        print("\nChoose an option:")
        print("1. Add transactions")
        print("2. View balance")
        print("3. Generate report")
        print("4. Quit")
        option = input("Enter your choice: ").strip()

        action = options.get(option)
        if action:
            action()
        else:
            print("Invalid choice! Try again.")

# adding any either an income or expense type of transaction to the system
def add_transaction():
    transaction_type = input("Enter transaction type (income/expense): ").strip().lower()
    
    if transaction_type not in ['income', 'expense']:
        print("Invalid transaction type! Must be 'income' or 'expense'.")
        return
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    if transaction_type == "income":
        category = get_valid_category(VALID_INCOME_CATEGORIES, "income")
    else:
        category = get_valid_category(VALID_EXPENSE_CATEGORIES, "expense")
    description = input("Enter description: ").strip()
    
    # for capturing the date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Writeing the transaction to CSV file with the date that we made
    with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category, description, date])
    
    print("Transaction added successfully!")

# Asking user for valid category
def get_valid_category(valid_categories, category_type):
    while True:
        category = input(f"Enter {category_type} category (e.g., {', '.join(valid_categories)}): ").strip().lower()
        if category in valid_categories:
            return category
        else:
            print(f"Invalid {category_type} category! Please choose from the valid options.")

# calculating the user current balance
def calculate_balance():
    balance = 0.0
    
    if not os.path.exists(TRANSACTIONS_FILE):
        # No transactions, so balance is going to become zero
        return balance  
    
    with open(TRANSACTIONS_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            transaction_type, amount, _, _, _ = row
            if transaction_type == "income":
                balance += float(amount)
            elif transaction_type == "expense":
                balance -= float(amount)
    
    if balance < 0:
        print(f"\nWarning: your balance is negative. You overspent by ${abs(balance):.2f}.")
    return balance

# just for filtering the print to the user
def show_balance():
    print(f"Current balance: ${calculate_balance():.2f}")

# generating the history of transactions
def generate_report():
    if not os.path.exists(TRANSACTIONS_FILE):
        print("No transactions available to generate a report.")
        return
    categories = {}
    
    with open(TRANSACTIONS_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            transaction_type, amount, category, description, date = row
            amount = float(amount)
            
            # grouping by categories
            if transaction_type == "income":
                label = f"Income - {category}"
            else:
                label = f"Expense - {category}"
            
            if label in categories:
                categories[label].append((amount, description, date))
            else:
                categories[label] = [(amount, description, date)]
    
    # Print out the report with dates and descriptions, stars for clear formatting
    print("***********************************")
    print("\nTransactions Report by Category:")
    for label, transactions in categories.items():
        print(f"\n{label}:")
        for amount, description, date in transactions:
            print(f"  Amount: ${amount:.2f}, Description: {description}, Date: {date}")
    print("***********************************")

def exit_program():
    sys.exit("Exiting the application")

if __name__ == "__main__":
    main()
