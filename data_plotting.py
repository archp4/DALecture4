import matplotlib.pyplot as plt


def plot_hist(data, column, xLabel, yLabel, title):
    plt.hist(data[column])
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.savefig(f"{title}.png")
