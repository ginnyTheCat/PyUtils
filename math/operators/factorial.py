from simalia.math.calcable import Calcable
from simalia.math.numbers import Integer


class Factorial(Calcable):

    def __init__(self, a):
        super().__init__(False)
        self.__a = a

    def __str__(self):
        return self.__a.str() + "!"

    def __factorial(self, num):
        if num <= Integer(2):
            if num == Integer(0):
                return Integer(1)
            return num
        return num * self.__factorial((num - Integer(1)).calc())

    def calc(self):
        return self.__factorial(self.__a.calc()).calc()
