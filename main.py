import csv
from graphic import main as grp

gross_wage = 4000


def main():
    expenses, names = csv_to_array("Expenses.csv")
    final_net, taxes = estimate_net(expenses)
    # clean all the values containing "%", referred as taxes
    clean_out(expenses, names)
    # add those values as a single "Taxes" name in the pie chart
    expenses.append(taxes)
    names.append("Taxes")
    # Graphic plot
    grp(expenses, names, final_net)


def csv_to_array(filename):
    # array in which the data will be saved
    expenses = []
    names = []
    # read every single line of the csv and store their values
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for line in reader:
            exp = line['Cost']
            name = line['Name']
            expenses.append(exp)
            names.append(name)
    return expenses, names


def estimate_net(expenses):
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
            tax_to_apply = float(tax.replace("%", ""))
            tax_estimated = gross_wage * tax_to_apply / 100
            total_taxes = total_taxes + tax_estimated
            no_taxes_wage = no_taxes_wage - tax_estimated
    final_net = no_taxes_wage - total_expenses
    return final_net, total_taxes


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def clean_out(expenses, names):
    names_to_remove = []
    expenses_to_remove = []
    for exp in expenses:
        if "%" in exp:
            i = expenses.index(exp)
            names_to_remove.append(names[i])
            expenses_to_remove.append(expenses[i])

    for i in range(len(expenses_to_remove)):
        expenses.remove(expenses_to_remove[i])
        names.remove(names_to_remove[i])


main()
