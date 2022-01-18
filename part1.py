import numpy as np
import sympy as sy
from sympy.core.function import diff
from sympy.core.symbol import Symbol
from sympy.utilities.lambdify import lambdify
from math import factorial as fact, pi, sin
import matplotlib.pyplot as plt
import pandas as pd
function='sin(x)'
calculated_ys = []
required_terms = []
list_for_taylor_values = []
number_of_terms = 0
x=pi/2
x_0=0
s=[]
m=[2,4,6,8,10,12,14,16,18,20]
for k in m:
    sum=0
    for number_of_terms in range (k):
        nth_function = diff(function, Symbol('x'), number_of_terms)/fact(number_of_terms)
        print(nth_function,k)       # differentiating with respect to x, n times
        list_for_taylor_values.append(lambdify(Symbol('x'), nth_function, 'numpy')(x_0))     # storing the value of nth_function at x = x_0
        sum += list_for_taylor_values[-1] * ((x-x_0)**number_of_terms)
        print(sum)
    s.append(sum)
    plt.scatter(number_of_terms,sum)
plt.plot(m,s)
plt.grid()
plt.legend()
plt.show()