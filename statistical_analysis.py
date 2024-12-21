# import statements
from faker import Faker
from datetime import date, datetime, timedelta
import random
import csv

def generate_dummy_data(num_transactions=5000):
    fake = Faker()
    transactions = []
    categories = ["groceries","dining","utilities","transportation","entertainment",
                             "shopping","health_and_fitness","travel","subscriptions","misc",
                             "education","home_improvement","insurance","donations","business"]

    for i in range(num_transactions):

        # Random date of birth and calculate Age
        dob = fake.date_of_birth(minimum_age=18, maximum_age=85)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Transaction Date
        days_ago = random.randint(0, 365)
        var_date = datetime.now() - timedelta(days=days_ago)
        date_str = var_date.strftime("%Y-%m-%d")

        # Bank Account Number
        account_num = fake.bban()

        # Category Type
        description = random.choice(categories)

        # Transaction Amount
        amount = round(random.uniform(0, 2000), 2)

        transactions.append({
            "Date": date_str,
            "Account_Number": account_num,
            "Amount": amount,
            "Description": description
        })

    return transactions


def save_transactions_to_csv(transactions, filename="transactions.csv"):
    # Save to a CSV file
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Account_Number", "Amount", "Description"])
        writer.writeheader()
        writer.writerows(transactions)
    print(f"Transactions saved to {filename}")

    # Generate dummy transactions
transactions = generate_dummy_data(10000)

    # Save to CSV file
save_transactions_to_csv(transactions, "dummy_transactions.csv")