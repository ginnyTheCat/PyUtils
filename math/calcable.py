class Calcable:

    def __init__(self, brackets):
        self.__brackets = brackets

    def calc(self):
        pass

    def latex(self):
        return str(self)

    def _neg(self):
        from simalia.math.operators import Mult
        from simalia.math.numbers import Integer
        return Mult(Integer(-1), self).calc()

    def _cmp(self, other):
        pass

    def cmp(self, other):
        res = self._cmp(other)
        if res != NotImplemented:
            return res
        return other._cmp(self)

    def str(self):
        return "(" + str(self) + ")" if self.__brackets else str(self)

    def __repr__(self):
        return str(self)

    def _repr_latex_(self):
        return "${" + self.latex() + "}$"

    def __add__(self, other):
        from simalia.math.operators import Add
        return Add(self, other)

    def __sub__(self, other):
        from simalia.math.operators import Sub
        return Sub(self, other)

    def __mul__(self, other):
        from simalia.math.operators import Mult
        return Mult(self, other)

    def __truediv__(self, other):
        from simalia.math.operators import Div
        return Div(self, other)

    def __mod__(self, other):
        from simalia.math.operators import Mod
        return Mod(self, other)

    def __pow__(self, other):
        from simalia.math.operators import Pow
        return Pow(self, other)

    def __neg__(self):
        from simalia.math.operators import Neg
        return Neg(self)

    def __eq__(self, other):
        if not isinstance(other, Calcable):
            return super().__eq__(other)
        return self.cmp(other) == 0

    def __lt__(self, other):
        if not isinstance(other, Calcable):
            return super().__lt__(other)
        return self.cmp(other) < 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __ge__(self, other):
        return self.cmp(other) >= 0
