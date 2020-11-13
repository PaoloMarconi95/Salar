import matplotlib.pyplot as plt

def main(expenses, names, final):
    explode = list()
    for i in expenses:
        explode.append(0)
    explode = tuple(explode)
    expenses.append(final)
    names.append("Net")
    explode = explode + (0.05,)
    plt.pie(expenses, explode=explode, labels=names, startangle=0)
    plt.show()

