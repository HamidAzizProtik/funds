import csv
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.csv")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter a number")

def save(expenses, filename=DATA_FILE):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "amount"])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def load(filename=DATA_FILE):
    expenses = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append({"name": row["name"], "amount": float(row["amount"])})
    except FileNotFoundError:
        pass
    return expenses

print('''
┏┓ ╻ ╻╺┳┓┏━╸┏━╸╺┳╸╻┏┓╻┏━╸   ┏━┓┏━┓┏━┓
┣┻┓┃ ┃ ┃┃┃╺┓┣╸  ┃ ┃┃┗┫┃╺┓   ┣━┫┣━┛┣━┛
┗━┛┗━┛╺┻┛┗━┛┗━╸ ╹ ╹╹ ╹┗━┛   ╹ ╹╹  ╹  
''')

monthly = get_float("enter monthly revenue: ")
expenses = load()
spent = 0
for e in expenses:
    spent += e["amount"]

while True:
    name = input("enter name of the expense (done = stop): ")

    if name == "done":
        print(f"you spent {spent:.2f} and have {monthly - spent:.2f} left behind")
        totals = {}

        for e in expenses:
            option_name = e["name"]
            amount = e["amount"]

            if option_name in totals:
                totals[option_name] += amount
            else:
                totals[option_name] = amount

        for option_name, amount in totals.items():
            print(f"{option_name}: {amount:.2f}")

        if (monthly - spent) >= 0:
            print("you can survive")
        else:
            print("you spent too much")

        save(expenses)
        break

    else:
        cost = get_float("enter cost of expense: ")
        spent = spent + cost
        expenses.append({"name": name, "amount": cost})