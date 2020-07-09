from simalia.math.numbers.base import Number


class Integer(Number):

    def __init__(self, num):
        super().__init__(num < 0)
        self.num = num

    def __str__(self):
        return str(self.num)

    def __len__(self):
        length = len(str(self.num))
        return length if self >= Integer(0) else length - 1

    def _cmp(self, other):
        if type(other) == Integer:
            return self.num - other.num
        return NotImplemented

    def _add(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(self.num + other.num)
        return NotImplemented

    def _sub(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(a1.num - a2.num)
        return NotImplemented

    def _mult(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(self.num * other.num)
        return NotImplemented

    def _div(self, other, a1, a2):
        if type(other) == Integer:
            from simalia.math.numbers.fraction import Fraction
            return Fraction(a1, a2)
        return NotImplemented

    def _rdiv(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(a1.num // a2.num)
        return NotImplemented

    def _mod(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(a1.num % a2.num)
        return NotImplemented

    def _pow(self, other, a1, a2):
        if type(other) == Integer:
            return Integer(a1.num ** a2.num)
        return NotImplemented

    def calc(self):
        return Integer(self.num)
