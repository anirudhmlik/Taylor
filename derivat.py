# import everything from sympy module
from sympy import *
import sympy as sy
import numpy 
a = numpy.arange(10)
x = Symbol('x')
fx="sin(x)"
expr = sympify(fx)
f = lambdify(x, expr, "numpy") 
print(f(a))
# make a symbol

n=int(input('Enter the n-th derivative!'))
# ake the derivative of sin(x)*e ^ x
ans1 = diff(expr, x,n)
fx = lambdify(x, ans1, "numpy") 
print("derivative of sin(x): ", fx(0))


def deri(m,i,c):
    print(type(m))
    fm=sy.sympify(m)
    print(type(fm))
    x=Symbol('x')
    FM=sy.lambdify(x,fm,"numpy")
    print(FM)
    df=sy.diff(fm,x,5)
    print(df)

deri('sin(x)',5,0)