import matplotlib.pyplot as plt


def main(expenses, names, finalNet):
    # all fraction of the pies must be 0
    explode = tuple(0 for _ in range(len(expenses)))
    # Adding the net
    expenses.append(finalNet)
    names.append("Net = " + str(finalNet))
    # The net must explode more than other slices
    explode = explode + (0.1,)
    # final plot
    plt.pie(expenses, explode=explode, labels=names, pctdistance=2, radius=1.3)
    plt.show()
