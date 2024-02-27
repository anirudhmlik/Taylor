from os import error
import numpy as np
import sympy as sy
from sympy import *
from sympy.core.function import diff
from sympy.core.symbol import Symbol
from sympy.utilities.lambdify import lambdify
from math import factorial as fact, pi
import matplotlib.pyplot as plt



function = input('Enter the function, for e.g. {sin(x),cos(x),exp(x)}: ')
list_for_taylor_functions = []           # to store derivatives (divided by factorials)
list_for_taylor_values = []              # to store the evaluated values of derivatives
number_of_terms = int(input('Enter the number of terms: '))
x_0 = int(input('Enter the value of c in taylor series: '))
for n in range(0, number_of_terms + 1):
    nth_function = diff(function, Symbol('x'), n)/fact(n)              # differentiating with respect to x, n times
    list_for_taylor_functions.append(nth_function)
    list_for_taylor_values.append(lambdify(Symbol('x'), nth_function, 'numpy')(x_0))     # storing the value of nth_function at x = x_0


# constructing taylor polynomial (in string form)

polynomial = ""
for n in range(len(list_for_taylor_values)-1):
    polynomial += str(list_for_taylor_values[n]) + f'*pow(x - {x_0}, {n}) + '

taylor_polynomial = polynomial + str(list_for_taylor_values[-1]) + f'*pow(x - {x_0}, {len(list_for_taylor_values)})'
print(taylor_polynomial)
# taylor function to calculate values of taylor polynomial


def taylor_func(x):
    return eval(taylor_polynomial)


def original_func(a,function):
    res=lambdify(Symbol('x'), sympify(function), 'numpy')(a)
    return res

# plotting
l1=float(input('Enter the start limit of fx: '))
l2=float(input('Enter the end limit of fx: '))
x = np.linspace(l1, l2, 100)
y_taylor=[]
y_original=[]

for i in range(len(x)):
    y_taylor.append(taylor_func(x[i]))
    y_original.append(original_func(x[i],function))

plt.plot(x, y_taylor, 'r', label=f'Approximated by taylor polynomial with {number_of_terms} terms')
plt.plot(x, y_original, 'g--', label='Original function')
plt.xlabel('x')
plt.ylabel(function)
plt.grid()
plt.legend()
plt.show()
