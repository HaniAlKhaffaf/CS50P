import sys, os, csv
from datetime import datetime


TRANSACTIONS_FILE = "transactions.csv"
VALID_INCOME_CATEGORIES = ["salary", "freelance", "investment", "business"]
VALID_EXPENSE_CATEGORIES = ["food", "rent", "utilities", "entertainment", "transportation", "healthcare", "education", "shopping"]

def main():
    print("Welcome to CS50P Finances Application")
    while True:
        print("\nChoose an option:")
        print("1. Add transactions")
        print("2. View balance")
        print("3. Generate report")
        print("4. Quit")
        option = input("Enter your choice: ")
        
        if option == "1":
            add_transaction()
        elif option == "2":
            print(f"Current balance: {calculate_balance()}")
        elif option == "3":
            generate_report()
            print(f"\nCurrent balance: {calculate_balance()}")
        elif option == "4":
            exit()
            break
        else:
            print("Invalid choice! Try again.")

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
    
    # Automatically capture the current date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write the transaction to CSV file with the date
    with open(TRANSACTIONS_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category, description, date])
    
    print("Transaction added successfully!")


def get_valid_category(valid_categories, category_type):
    """Prompt user for a valid category and validate it against a list of predefined categories."""
    while True:
        category = input(f"Enter {category_type} category (e.g., {', '.join(valid_categories)}): ").strip().lower()
        if category in valid_categories:
            return category
        else:
            print(f"Invalid {category_type} category! Please choose from the valid options.")

def calculate_balance():
    balance = 0.0
    
    if not os.path.exists(TRANSACTIONS_FILE):
        return balance  # No transactions, so balance is zero
    
    with open(TRANSACTIONS_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            transaction_type, amount, _, _, _ = row
            if transaction_type == "income":
                balance += float(amount)
            elif transaction_type == "expense":
                balance -= float(amount)
    
    if balance < 0:
        print(f"\nWarning: Your balance is negative! You have overspent by ${abs(balance):.2f}.")
    
    return balance

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
            
            # Group by categories
            if transaction_type == "income":
                label = f"Income - {category}"
            else:
                label = f"Expense - {category}"
            
            if label in categories:
                categories[label].append((amount, description, date))
            else:
                categories[label] = [(amount, description, date)]
    
    # Print out the report with dates and descriptions
    print("***********************************")
    print("\nTransactions Report by Category:")
    for label, transactions in categories.items():
        print(f"\n{label}:")
        for amount, description, date in transactions:
            print(f"  Amount: ${amount:.2f}, Description: {description}, Date: {date}")
    print("***********************************")
    

def exit():
    sys.exit("Exiting the application")

if __name__ == "__main__":
    main()