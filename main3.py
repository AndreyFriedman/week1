
# https://predictivehacks.com/newton-raphson-method-in-python/

import numpy as np
from sympy import *


def find_root(func, x1, x2):

    x = symbols('x') # define what is the variable
    f = func
    fderivative = f(x).diff(x) # find the derivative
    xn = x1
    for i in range(10):
        fx = np.float(f(x).evalf(subs={x: xn}))
        ftagx = np.float(fderivative.evalf(subs={x: xn}))
        xn = xn - fx / ftagx # make the step
        if fx < 0.005 and xn < x2:
            return int(xn)

# Tests and examples:

q11 = find_root(lambda x: x**2-4, 1, 3)
q12 = find_root(lambda x: x**2-4, -3, 1)
q21 = find_root(lambda x: x**2-4*x-5, -3, 1)
q22 = find_root(lambda x: x**2-4*x-5, 4, 10)
print(q11)
print(q12)
print(q21)
print(q22)
