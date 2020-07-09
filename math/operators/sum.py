from simalia.math.calcable import Calcable
from simalia.math.numbers.integer import Integer


class Sum(Calcable):

    def __init__(self, iterations, var, func):
        super().__init__(False)
        self.iterations = iterations
        self.var = var
        self.func = func
        self.__res = Integer(0)

    def __iter__(self):
        for i in range(self.iterations):
            self.iterations -= 1
            self.__res += self.func().calc()
            yield self.__res
            self.var.val += Integer(1)

    def calc(self):
        for _ in self:
            pass
        return self.__res.calc()
