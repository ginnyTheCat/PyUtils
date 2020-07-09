from simalia.math.numbers.integer import Integer
from simalia.math.operators.factorial import Factorial
from simalia.math.operators.sum import Sum
from simalia.pymath import Variable


class E(Sum):

    def __init__(self, iterations=18):
        self.__k = Variable("k", Integer(0))
        super().__init__(iterations, self.__k, lambda: Integer(1) / Factorial(self.__k.val))
        self.iterations = iterations

    def __str__(self):
        return "e"
