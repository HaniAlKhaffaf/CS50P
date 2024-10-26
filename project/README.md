# Personal Finance Tracker
#### Video Demo: https://youtu.be/MUAGQmSPukk 
#### Description:

## Introduction
The **Personal Finance Tracker** is a Python-based command-line application that helps users manage 
their finances, i.e. Income and Expenses. The program allows users to add transactions, categorize 
them based on some certain categories, calculate their total balance, and generate a detailed report 
of their financial activity. With features like date-stamping, category validation, and modular design 
(using the Dispatch Table practice), this application offers a convenient way for users to keep track 
of their finances and make a better budgeting decisions.

This project is developed for the final submission for CS50P, an introduction to Python programming 
course offered by Harvard and Edx. The code will be uploaded on my personal Github account as an open source to help others in any possible way, but this is a reminder that using the code for cheating or with the intent of submitting it will be counted as unethical plagiarism and a misconduct according to harvard's policies, happy coding.

## Project Files
### 1. `project.py`
This is the main file of the application, containing the all of the functions used in the project:
- **`main()`**: Acts as the entry point of the program, handling user input and directing them to various features using a dispatch table.
- **`add_transaction()`**: Allows users to add a new transaction through either an income or an expense. Each transaction is automatically stamped with the current date and time, and users are prompted to categorize their entries, this function is tightly couples with the `get_valid_category()` function.
- **`calculate_balance()`**: Reads the stored transactions in the CSV file and calculates the overall balance by adding all income and subtracting all expenses. It also warns users if their balance is negative.
- **`generate_report()`**: Generates a report that includes all of transactions done by the user, categorized by income and expense types, along with details like description and date. The report helps users visualize their financial behavior over time.
- **`show_balance()`**: A helper function to display the current balance, tightly couples and calling `calculate_balance()` for printing the result, basically for pretty formatting for the user.
- **`exit_program()`**: Terminates the program gracefully when the user selects the option to quit.
- **`get_valid_category()`**: Ensures that the user enters a valid category by checking against a predefined list.

### 2. `transactions.csv`
This file is used to store all the user's transactions using the CSV format, including:
- **Transaction Type** (income or expense)
- **Amount**
- **Category**
- **Description**
- **Date & Time**

Each entry is stored in CSV format, making it easy to read, update, and process. The application automatically creates this file if it doesn't exist.

### 3. `test_project.py`
This file contains unit tests for the application, ensuring that the functions of the applications 
work as expected. The test cases focus on:
- Verifying that transactions are correctly added to the CSV file.
- Confirming that the balance calculation logic handles various combinations of income and expenses 
accurately.
- Checking that the report generation correctly categorizes and displays transaction details, 
including descriptions and dates.
- Testing the `show_balance()` function to ensure that the displayed output matches the calculated 
balance.

The test file uses the `pytest` framework and includes techniques to use temporary files for testing, 
ensuring that the tests do not interfere with the main application data.

### 4. `requirements.txt`
This file lists any external libraries that the project relies on. For this project, only `pytest` is 
included for testing purposes. The `requirements.txt` file allows users to easily install dependencies 
by running:
```bash
pip install -r requirements.txt
```

## Design Choice
Below are some of the design choices that i have implemented

### CSV Storage
Decided to not go for complicated storage systems for the purpose of avoiding third-party technologies
such as Databases, therefore used CSV for the means of basic internal/local storage system, if the project exapnds, might reconsider this approach, so far CSV is serving my project perfectly

### CLI 
opted for the usage of CLI for simplicity of the code logic. I am planning to use this app for my own personal use and i am familiar enough with CLI therefore would not need any interactice or graphical UI to interact with the application. If i had the intentions of publishing this project and expanding the user-base, might consider swtiching to GUI based applications for simpler user-end usability.

### Dispatch Table
Used Dispatch Table design for easy code logic understand as well as for future scalability of the application, with the use of Dispatch Table design you could easy implement new features as a separate modules and functions
