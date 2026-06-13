def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter a number")

print(r'''
┏┓ ╻ ╻╺┳┓┏━╸┏━╸╺┳╸╻┏┓╻┏━╸   ┏━┓┏━┓┏━┓
┣┻┓┃ ┃ ┃┃┃╺┓┣╸  ┃ ┃┃┗┫┃╺┓   ┣━┫┣━┛┣━┛
┗━┛┗━┛╺┻┛┗━┛┗━╸ ╹ ╹╹ ╹┗━┛   ╹ ╹╹  ╹  
''')

monthly = get_float("enter monthly revenue: ")
spent = 0
expenses = []

while True:
    name = input("enter name of the expense (done = stop): ")

    if name == "done":
        print(f"you spent {spent:.2f} and have {monthly - spent:.2f} left behind")
        print(expenses)
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
        break

    else:
        cost = get_float("enter cost of expense: ")
        spent = spent + cost
        expenses.append({"name": name, "amount": cost})