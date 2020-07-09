from simalia.math.calcable import Calcable
from simalia.math.operators.base import DualOperator


class Add(DualOperator):

    def __init__(self, a, b):
        super().__init__("+", "_add", a, b)


class Sub(DualOperator):

    def __init__(self, a, b):
        super().__init__("-", "_sub", a, b)


class Mult(DualOperator):

    def __init__(self, a, b):
        super().__init__("*", "_mult", a, b)


class Div(DualOperator):

    def __init__(self, a, b):
        super().__init__("/", "_div", a, b)

    def latex(self):
        return "\\frac{" + self._a.latex() + "}{" + self._b.latex() + "}"


class RDiv(DualOperator):

    def __init__(self, a, b):
        super().__init__("//", "_rdiv", a, b)


class Mod(DualOperator):

    def __init__(self, a, b):
        super().__init__(" mod ", "_mod", a, b)


class Pow(DualOperator):

    def __init__(self, a, b):
        super().__init__("^", "_pow", a, b)


class Neg(Calcable):

    def __init__(self, a):
        super().__init__(True)
        self.__a = a

    def __str__(self):
        return "-" + self.__a.str()

    def calc(self):
        return self.__a.calc()._neg()
