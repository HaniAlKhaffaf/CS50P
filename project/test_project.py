import pytest
from project import add_transaction, calculate_balance, generate_report
import csv
import os

@pytest.fixture
def mock_transactions_file(tmpdir):
    temp_file = tmpdir.join("transactions.csv")
    return temp_file

def test_add_transaction(mock_transactions_file):
    
    def mock_add_transaction(transaction_type, amount, category, description):
        date = "2024-10-12 10:00:00"
        with open(mock_transactions_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([transaction_type, amount, category, description, date])

    mock_add_transaction("income", "1000", "salary", "monthly salary")

    with open(mock_transactions_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    assert len(rows) == 1
    assert rows[0][0] == 'income'
    assert rows[0][1] == '1000'
    assert rows[0][2] == 'salary'
    assert rows[0][3] == 'monthly salary'
    assert rows[0][4] == '2024-10-12 10:00:00'

def test_calculate_balance(mock_transactions_file, monkeypatch):
    
    monkeypatch.setattr("project.TRANSACTIONS_FILE", str(mock_transactions_file))
    
    with open(mock_transactions_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['income', '2000', 'salary', 'monthly salary', '2024-10-12 10:00:00'])
        writer.writerow(['expense', '500', 'food', 'grocery shopping', '2024-10-13 12:00:00'])
        writer.writerow(['expense', '300', 'rent', 'monthly rent', '2024-10-14 08:00:00'])
    
    balance = calculate_balance()
    
    assert balance == 1200.0


def test_generate_report(mock_transactions_file):
    
    with open(mock_transactions_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['income', '1000', 'salary', 'monthly salary', '2024-10-12 10:00:00'])
        writer.writerow(['expense', '200', 'food', 'grocery shopping', '2024-10-13 12:00:00'])
        writer.writerow(['expense', '300', 'rent', 'monthly rent', '2024-10-14 08:00:00'])
    
    transactions = []
    with open(mock_transactions_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            transactions.append(row)
    
    assert len(transactions) == 3
    assert transactions[0] == ['income', '1000', 'salary', 'monthly salary', '2024-10-12 10:00:00']
    assert transactions[1] == ['expense', '200', 'food', 'grocery shopping', '2024-10-13 12:00:00']
    assert transactions[2] == ['expense', '300', 'rent', 'monthly rent', '2024-10-14 08:00:00']
