# Personal Finance Tracker
#### Video Demo: [URL HERE]
#### Description:

## Introduction
The **Personal Finance Tracker** is a Python-based command-line application that helps users manage their income and expenses. The program allows users to add transactions, categorize them, calculate their overall balance, and generate a detailed report of their financial activity. With features like automatic date-stamping and category validation, this tool offers a convenient way for users to keep track of their finances and make informed budgeting decisions.

This project was developed as the final submission for CS50P, an introduction to Python programming. The goal was to apply the skills and concepts learned throughout the course to build a fully functional software application.

## Project Files
### 1. `project.py`
This is the main file of the application, containing the core functions:
- **`main()`**: Acts as the entry point of the program, handling user input and directing them to various features of the tracker.
- **`add_transaction()`**: Allows users to add a new transaction, either as income or an expense. Each transaction is automatically stamped with the current date and time, and users are prompted to categorize their entries.
- **`calculate_balance()`**: Reads the stored transactions and calculates the overall balance by adding all income and subtracting all expenses. It also warns users if their balance is negative, encouraging them to review their spending habits.
- **`generate_report()`**: Generates a report that summarizes all transactions, categorized by income and expense types, along with details like description and date. The report helps users visualize their financial behavior over time.
- **`get_valid_category()`**: Ensures that the user enters a valid category by checking against a predefined list. This prevents errors and keeps data consistent.

### 2. `transactions.csv`
This file is used to store all the user's transactions, including:
- **Transaction Type** (income or expense)
- **Amount**
- **Category**
- **Description**
- **Date & Time**

Each entry is stored in CSV format, making it easy to read, update, and process. The application automatically creates this file if it doesn't exist.

### 3. `test_project.py`
This file contains unit tests for the application, ensuring that the core functions work as expected. The test cases focus on:
- Verifying that transactions are correctly added to the CSV file.
- Confirming that the balance calculation logic handles various combinations of income and expenses accurately.
- Checking that the report generation correctly categorizes and displays transaction details, including descriptions and dates.

The test file makes use of the `pytest` framework and includes techniques to use temporary files for testing, ensuring that the tests do not interfere with the main application data.

### 4. `requirements.txt`
This file lists any external libraries that the project relies on. For this project, only `pytest` is included for testing purposes. The `requirements.txt` file allows users to easily install dependencies by running:
```bash
pip install -r requirements.txt

## Design Choice
