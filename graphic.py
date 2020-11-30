import matplotlib.pyplot as plt


def main(expenses, names, final_net):
    # all fraction of the pies must be 0
    explode = tuple(0 for _ in range(len(expenses)))
    # Adding the net
    expenses.append(final_net)
    names.append("Net = " + str(final_net))
    # The net must explode more than other slices
    explode = explode + (0.1,)
    # final plot
    plt.pie(expenses, explode=explode, labels=names, pctdistance=2, radius=1.3)
    plt.show()
