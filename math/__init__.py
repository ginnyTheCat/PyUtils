from simalia.math.functions.sine import Sine
from simalia.math.numbers import Integer, Fraction
from simalia.math.operators import Add, Sub, Div, Mult, Pow, Neg
from simalia.math.operators.factorial import Factorial
from simalia.math.variables.e import E
from simalia.math.variables.pi import Pi
from simalia.math.variables.variable import Variable


def n(num):
    if type(num) == int:
        return Integer(num)
    elif type(num) == float:
        zeros = 10 ** str(num)[::-1].find('.')
        return Fraction(Integer(int(num * zeros)), Integer(zeros))
    elif type(num) == str:
        return Variable(num)
    return num
