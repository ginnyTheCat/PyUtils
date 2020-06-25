import matplotlib.pyplot as plt
from Utils.data import index

LOCATION = "best"


def bar(names, values, *more_vals):
    names = _get_names(values, names)
    more_vals = list(more_vals)
    more_vals.insert(0, values)

    width = 0.3

    for i, val in enumerate(more_vals):
        plt.bar([x + (float(i) * width) for x in index(val)], val, width=width)
    plt.xticks([x + (len(more_vals) - 1.5) * width for x in index(values)], names)


def line(names, values, markers=True):
    names = _get_names(values, names)
    plt.plot(list(names), list(values), marker='o' if markers else None, linestyle='solid')


def pie(names, values, highlight_first=True, legend=False):
    names = _get_names(values, names)
    explode = None
    if highlight_first:
        explode = [0.] * len(values)
        explode[0] = 0.05
    patches, _ = plt.pie(values, labels=None if legend else names, explode=explode)
    if legend:
        plt.legend(patches, names, loc=LOCATION, facecolor='white', framealpha=1)


def donut(names, values):
    names = _get_names(values, names)
    plt.pie(values, labels=names, wedgeprops=dict(width=0.4))


def _get_names(values, names):
    if names is None:
        return index(values)
    return names


plt.style.use("seaborn")
