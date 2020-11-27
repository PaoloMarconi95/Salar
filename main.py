import csv
from graphic import main as grp

gross_wage = 4000


def main():
    expenses, names = csv_to_array("Expenses.csv")
    finalNet, taxes = estimate_final(expenses)
    clean_out(expenses, names)
    expenses.append(taxes)
    names.append("Taxes")
    grp(expenses, names, finalNet)


def csv_to_array(filename):
    expenses = []
    names = []
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            exp = line['Cost']
            name = line['Name']
            expenses.append(exp)
            names.append(name)
    return expenses, names


def estimate_final(expenses):
    taxes = []
    total_expenses = 0
    for expense in expenses:
        if is_int(expense):
            total_expenses = total_expenses + int(expense)
        else:
            taxes.append(expense)
    no_taxes_wage = gross_wage
    total_taxes = 0
    if len(taxes) > 0:
        for tax in taxes:
            tax_to_apply = tax.replace("%", "")
            tax_to_apply = float(tax_to_apply)
            tax_estimated = gross_wage * tax_to_apply / 100
            total_taxes = total_taxes + tax_estimated
            no_taxes_wage = no_taxes_wage - tax_estimated
    finalNet = no_taxes_wage - total_expenses
    return finalNet, total_taxes


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def clean_out(expenses, names):
    for exp in expenses:
        if "%" in exp:
            i = expenses.index(exp)
            names.remove(names[i])
            expenses.remove(expenses[i])


main()
