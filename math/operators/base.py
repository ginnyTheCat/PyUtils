from simalia.math.numbers.base import Number
from simalia.math.calcable import Calcable


class DualOperator(Calcable):

    def __init__(self, sign, func, a, b):
        super().__init__(True)
        self.__sign = sign
        self.__func = func
        self._a = a
        self._b = b

    def __str__(self):
        return str(self._a) + self.__sign + self._b.str()

    def latex(self):
        return self._a.latex() + self.__sign + self._b.latex()

    def calc(self):
        a = self._a.calc()
        b = self._b.calc()
        if not isinstance(a, Number) or not isinstance(b, Number):
            return self.__class__(a, b)
        res = getattr(a, self.__func)(b, a, b)
        if res != NotImplemented:
            return res
        return getattr(b, self.__func)(a, a, b)
