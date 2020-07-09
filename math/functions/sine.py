from simalia.math.variables import Variable
from simalia.math.numbers import Integer
from simalia.math.operators.factorial import Factorial
from simalia.math.operators.sum import Sum


class Sine(Sum):

    def __init__(self, val, iterations=10):
        self.__k = Variable("k", Integer(0))
        super().__init__(iterations, self.__k, self.__formular)
        self.val = val
        self.__neg = False

    def __str__(self):
        return "sin(" + str(self.val) + ")"

    def __formular(self):
        l = self.var.val * Integer(2) + Integer(1)
        res = (self.val ** l) / Factorial(l)
        self.__neg = not self.__neg
        if self.__neg:
            return res
        return -res
