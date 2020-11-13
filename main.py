import csv
from graphic import main as grp

gross_wage = 4000

def main():
    expenses, names = csv_to_array("Expenses.csv")
    final = estimate_final(expenses)
    taxes = gross_wage*13.7/100
    expenses.append(taxes)
    names.append("Taxes")
    grp(expenses, names, final)


def csv_to_array(filename):
    expenses = []
    names = []
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            exp = line['Cost']
            nam = line['Name']
            expenses.append(exp)
            names.append(nam)
    return expenses, names


def estimate_final(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses = total_expenses + int(expense)
    net_wage = (gross_wage - (gross_wage*13.7/100))
    return net_wage - total_expenses


main()
