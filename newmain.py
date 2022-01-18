import time
start = time.time()
import numpy as np
import sympy as sy
from sympy.core.function import diff
from sympy.core.symbol import Symbol
from sympy.utilities.lambdify import lambdify
from math import factorial as fact, pi, sin
import matplotlib.pyplot as plt
import pandas as pd

def taylorerror(x_0,no,x,function):
    list_for_taylor_functions = []           
    # to store derivatives (divided by factorials)
    list_for_taylor_values = []              
    # to store the evaluated values of derivatives
    for n in range(0, no + 1):
        nth_function = sy.diff(function, sy.Symbol('x'), n)/fact(n)              
        # differentiating with respect to x, n times
        list_for_taylor_functions.append(nth_function)
        list_for_taylor_values.append(sy.lambdify(sy.Symbol('x'), 
        nth_function, 'numpy')(x_0))     
        # storing the value of nth_function at x = x_0


# constructing taylor polynomial (in string form)

    polynomial = ""
    for n in range(len(list_for_taylor_values)-1):
        polynomial += str(list_for_taylor_values[n]) + f'*pow(x - {x_0}, {n}) + '

    taylor_polynomial = polynomial + str(list_for_taylor_values[-1]) + f'*pow(x - {x_0}, {len(list_for_taylor_values)})'
    print(taylor_polynomial)
# taylor function to calculate values of taylor polynomial


    def taylor_func(x):
        return eval(taylor_polynomial)
    
    y_taylor=[]

    for i in range(len(x)):
        y_taylor.append(taylor_func(x[i]))
    
    plt.plot(x,y_taylor,label = f'"n= {no}"')

function = input('Enter the function, for e.g. {sin(x),cos(x),exp(x)} to be plotted: ')
list_for_taylor_functions = []           # to store derivatives (divided by factorials)
list_for_taylor_values = []              # to store the evaluated values of derivatives
number_of_terms = int(input('Enter the number of terms for only this plot: '))
x_0 = int(input('Enter the value of c in taylor series for only this plot: '))
for n in range(0, number_of_terms + 1):
    nth_function = diff(function, Symbol('x'), n)/fact(n)              
    # differentiating with respect to x, n times
    list_for_taylor_functions.append(nth_function)
    list_for_taylor_values.append(lambdify(Symbol('x'), nth_function, 'numpy')(x_0))     
    # storing the value of nth_function at x = x_0


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
    res=lambdify(Symbol('x'), sy.sympify(function), 'numpy')(a)
    return res
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


error_margin = float(input('Enter the error:'))
xs = np.arange(0, pi+pi/8, pi/8)
calculated_ys = []
required_terms = []

for x in xs:
    list_for_taylor_values = []
    number_of_terms = 0
    sum = 0
    while abs(sum - lambdify(Symbol('x'), function, 'numpy')(x)) >= error_margin:
        nth_function = diff(function, Symbol('x'), number_of_terms)/fact(number_of_terms)              
        # differentiating with respect to x, n times
        list_for_taylor_values.append(lambdify(Symbol('x'), nth_function, 'numpy')(x_0))     
        # storing the value of nth_function at x = x_0
        sum += list_for_taylor_values[-1] * ((x-x_0)**number_of_terms)
        number_of_terms += 1
    taylorerror(x_0,number_of_terms,xs,function)
    required_terms.append(number_of_terms)
    calculated_ys.append(sum)


original_ys = []
for i in xs:
    original_ys.append(lambdify(Symbol('x'), function, 'numpy')(i))


data = {"x":xs,
        function+"_original":original_ys,
        function+"_calculated":calculated_ys,
        "n":required_terms}
df = pd.DataFrame(data)
print(df)

plt.plot(xs,original_ys,marker = ".",label = "original ", color = "blue")
plt.scatter(xs,calculated_ys,marker = "x", color = "black", label = "sin(x) at different values of n")      
plt.grid()
plt.xlabel("x")
plt.ylabel(function)
plt.legend()
plt.show()
def part1bc(function,x,x_0):
    list_for_taylor_values = []
    number_of_terms = 0
    s=[]
    m=[2,4,6,8,10,12,14,16,18,20]
    for k in m:
        sum=0
        for number_of_terms in range (k):
            nth_function = diff(function, Symbol('x'), number_of_terms)/fact(number_of_terms)    
            # differentiating with respect to x, n times
            list_for_taylor_values.append(lambdify(Symbol('x'), nth_function, 'numpy')(x_0))     
            # storing the value of nth_function at x = x_0
            sum += list_for_taylor_values[-1] * ((x-x_0)**number_of_terms)
        s.append(sum)
        plt.scatter(number_of_terms,sum)
    plt.plot(m,s)
    plt.grid()
    plt.legend()
    plt.show()

x=float(input('Enter the value of x: '))
x_0=float(input('Enter the value of x_0: '))

part1bc(function,x,x_0)