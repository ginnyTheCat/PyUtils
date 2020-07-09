from enum import Enum

import matplotlib.pyplot as plt
from simalia.data import index


class PlotTypes(Enum):
    LINE = 1
    BAR = 2
    PIE = 3
    DONUT = 4


class Plot:

    def __init__(self, title="", legend=False):
        self.title = title
        self.legend = legend
        self.type = None

        self._legend_data = []

        self._keys = []
        self._values = []

    def dict(self, dictionary):
        self._keys = dictionary.keys()
        self._values.append(dictionary.values())
        return self

    def keys(self, keys):
        self._keys = keys
        return self

    def values(self, *values):
        self._values += values
        return self

    def mean(self, val):
        plt.plot(list(self._keys), [val] * len(self._keys), label="mean", linestyle='--')
        return self

    def line(self, markers=True):
        self.type = PlotTypes.LINE

        keys = list(self._keys)
        for val in self._values:
            plt.plot(keys, list(val), marker='o' if markers else None, linestyle='solid')
        return self

    def bar(self, horizontal=False):
        self.type = PlotTypes.BAR

        fig, ax = plt.subplots()

        width = 0.3
        for i, val in enumerate(self._values):
            positions = [x + (float(i) * width) for x in index(val)]
            if horizontal:
                ax.barh(positions, val, height=width)
            else:
                ax.bar(positions, val, width=width)
        label_pos = [x + (len(self._values) - 1) / 2 * width for x in index(self._keys)]
        if horizontal:
            ax.set_yticks(label_pos)
            ax.set_yticklabels(self._keys)
            ax.invert_yaxis()
        else:
            ax.set_xticks(label_pos)
            ax.set_xticklabels(self._keys)
        return self

    def pie(self, highlight_first=True):
        self.type = PlotTypes.PIE
        self._legend_data = self._keys

        explode = None
        if highlight_first:
            explode = [0.] * len(self._keys)
            explode[0] = 0.05
        plt.pie(self._values[0], labels=self._labels(), explode=explode)
        return self

    def donut(self):
        self.type = PlotTypes.DONUT
        self._legend_data = self._keys

        plt.pie(self._values[0], labels=self._labels(), wedgeprops=dict(width=0.4))
        return self

    def _labels(self):
        if self.legend:
            return None
        return self._keys

    def draw(self):
        if self.legend:
            loc = self.legend if self.legend is not True else "best"
            plt.legend(self._legend_data, loc=loc)
        plt.title(self.title)
        plt.draw()


plt.style.use("seaborn")
