from simalia.math.calcable import Calcable


class Variable(Calcable):

    def __init__(self, key, val=None, insert=True):
        super().__init__(False)
        self.key = key
        self._val = val
        self.insert = insert

    def __str__(self):
        return self.key

    @property
    def val(self):
        if self.insert:
            return self._val

    @val.setter
    def val(self, value):
        self._val = value

    def calc(self):
        if self.val is None or not self.insert:
            return self
        return self.val.calc()
