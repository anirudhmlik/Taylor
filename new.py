import time
start = time.time()
import numpy as np
import sympy as sy
import math
import matplotlib.pyplot as plt
from math import factorial as fact, pi

def taylor(x_0,no,x,function):
    list_for_taylor_functions = []           # to store derivatives (divided by factorials)
    list_for_taylor_values = []              # to store the evaluated values of derivatives
    for n in range(0, no + 1):
        nth_function = sy.diff(function, sy.Symbol('x'), n)/fact(n)              # differentiating with respect to x, n times
        list_for_taylor_functions.append(nth_function)
        list_for_taylor_values.append(sy.lambdify(sy.Symbol('x'), nth_function, 'numpy')(x_0))     # storing the value of nth_function at x = x_0


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
            res=sy.lambdify(sy.Symbol('x'), sy.sympify(function), 'numpy')(a)
            return res

    
    y_taylor=[]
    y_original=[]

    for i in range(len(x)):
        y_taylor.append(taylor_func(x[i]))
        y_original.append(original_func(x[i],function))
    print(len(y_taylor),len(y_original),len(x))
    plt.plot(x, y_taylor, 'r', label=f'Approximated by taylor polynomial with {no} terms')
    plt.plot(x, y_original, 'g--', label='Original function')
    plt.xlabel('x')
    plt.ylabel(function)
    plt.grid()
    plt.legend()
    plt.show()


#x_0 = int(input('Enter the value of c in taylor series: '))
#m=[1,2,5,10,20]
#x = np.linspace(-2*(math.pi), 2*(math.pi), 100)
#function = input('Enter the function, for e.g. {sin(x),cos(x),exp(x)}: ')
#for i in m:
    #taylor(x_0,i,x,function)

def taylortolerance(x_0,no,x,function,tol):
    list_for_taylor_functions = []           # to store derivatives (divided by factorials)
    list_for_taylor_values = []              # to store the evaluated values of derivatives
    for n in range(0, no + 1):
        nth_function = sy.diff(function, sy.Symbol('x'), n)/fact(n)              # differentiating with respect to x, n times
        list_for_taylor_functions.append(nth_function)
        list_for_taylor_values.append(sy.lambdify(sy.Symbol('x'), nth_function, 'numpy')(x_0))     # storing the value of nth_function at x = x_0


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
            res=sy.lambdify(sy.Symbol('x'), sy.sympify(function), 'numpy')(a)
            return res

    
    y_taylor=[]
    y_original=[]

    for i in range(len(x)):
        y_taylor.append(taylor_func(x[i]))
        y_original.append(original_func(x[i],function))
    t=0
    err=[]
    for i in range(len(x)):
        t=abs((y_taylor[i]-y_taylor[i-1])/y_taylor[i])
        err.append(t)
    #def tolerance(tole,x,y_taylor,y_original):
    if max(err)<tol:
        taylortolerance(x_0,no+2,x,function,tol)
    else:
        return no

tol=0.005 #float(input('Enter the tol: '))
x_0 = int(input('Enter the value of c in taylor series: '))
m=n=0
x = np.linspace(0, (math.pi), 8)
print(x)
function = input('Enter the function, for e.g. {sin(x),cos(x),exp(x)}: ')
for i in range (len(x)):
    n=taylortolerance(x_0,m,x[i],function,tol)
    print(n,x[i])

end = time.time()
print(end-start)