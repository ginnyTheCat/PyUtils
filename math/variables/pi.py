from simalia.math.numbers.integer import Integer
from simalia.math.operators.sum import Sum
from simalia.pymath import Variable


class Pi(Sum, Variable):

    def __init__(self, iterations=11):
        self.__k = Variable("k", Integer(0))
        super().__init__(iterations, self.__k, self.__formular)
        self.iterations = iterations

    def __str__(self):
        return "\u03c0"

    def latex(self):
        return "\\pi"

    def __formular(self):
        k8 = (Integer(8) * self.__k.val).calc()
        return (Integer(1) / Integer(16) ** self.__k.val) * (
                (Integer(4) / (k8 + Integer(1))) -
                (Integer(2) / (k8 + Integer(4))) -
                (Integer(1) / (k8 + Integer(5))) -
                (Integer(1) / (k8 + Integer(6))))
