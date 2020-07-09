from simalia.math.numbers.base import Number
from simalia.math.operators import RDiv


class Fraction(Number):

    def __init__(self, num, div):
        super().__init__(True)
        self.num = num
        self.div = div

    def __str__(self):
        return self.num.str() + "/" + self.div.str()

    def latex(self):
        return "\\frac{" + str(self.num) + "}{" + str(self.div) + "}"

    def _cmp(self, other):
        if type(other) == Fraction:
            return (self.num * other.div).calc().cmp((other.num * self.div).calc())
        return self.num.calc().cmp((other * self.div).calc())

    def _add(self, other, a1, a2):
        if type(other) == Fraction:
            return Fraction(self.num * other.div + other.num * self.div, self.div * other.div).calc()
        return Fraction(self.num + other * self.div, self.div).calc()

    def _sub(self, other, a1, a2):
        if type(other) == Fraction:
            return Fraction(a1.num * a2.div - a2.num * a1.div, a1.div * a2.div).calc()
        if self == a1:
            return Fraction(self.num - other * self.div, self.div).calc()
        return Fraction(other * self.div - self.num, self.div).calc()

    def _mult(self, other, a1, a2):
        if type(other) == Fraction:
            return Fraction(a1.num * a2.num, a1.div * a2.div).calc()
        return Fraction(self.num * other, self.div).calc()

    def _div(self, other, a1, a2):
        if type(other) == Fraction:
            return Fraction(a1.num * a2.div, a1.div * a2.num).calc()
        return Fraction(self.num, self.div * other).calc()

    #def _mod(self, other, a1, a2):
    #    from simalia.math.numbers.integer import Integer
    #    if type(a2) == Integer:
    #        return ((a1 - a2) * RDiv(a1, a2)).calc()

    def _pow(self, other, a1, a2):
        if self == a1:
            return Fraction(a1.num ** a2, a1.div ** a2).calc()
        return NotImplemented

    @staticmethod
    def gcd(a, b):
        from simalia.math.numbers.integer import Integer
        while b != Integer(0):
            a, b = b, (a % b).calc()
        return a

    def calc(self):
        num = self.num.calc()
        div = self.div.calc()
        if not isinstance(num, Number) or not isinstance(div, Number):
            return Fraction(num, div)
        g = Fraction.gcd(num, div)
        return Fraction(RDiv(num, g).calc(), RDiv(div, g).calc())
