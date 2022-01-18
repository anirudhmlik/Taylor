import sympy as sy
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy.core.function import diff
from sympy.core.symbol import Symbol
from sympy.core.sympify import sympify
from sympy.plotting.textplot import linspace
from sympy.utilities.lambdify import lambdify

def taylor(lim,n,c,fX):
    z=fx=[]
    for j in range(len(lim)):
        x=Symbol('x')
        s=k=0
        f=sy.sympify(fX)
        FX=sy.lambdify(x,f,"numpy")
        print(lim[j])
        l=lim[j]
        print(FX(0),l,FX(l))
        z.append(FX(l))
        print(z)
        for i in range(n):
            m=deri(fX,i,c)
            k=((1/math.factorial(i))*m*((lim[j]-c)**i))
            s=s+k
        fx.append(s)
    print(i,j)
    print(len(z))
    print(len(fx))
    difference = []
    zip_object = zip(z, fx)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i-list2_i)
    print(len(difference))
    plot(lim,z,fx)

def deri(m,i,c):
    x=Symbol('x')
    fm=sy.sympify(m)
    df=sy.diff(fm,x,i)
    v=lambdify(x,df,"numpy")
    m=v(c)
    return(m)

def plot(xlable,y1,y2):
    fig,ax=plt.subplots()
    plt.plot(xlable,y1,label="original")
    plt.plot(xlable,y2,label="taylor")
    ax.set_title("EXP FUNCTION")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.grid()
    plt.legend()
    plt.show() 


x=math.radians(-90) #int(input('Enter the lower limit: '))
y=math.radians(90) #int(input('Enter the upper limit: '))
n=5 #int(input('Enter the number of terms: '))
st='sin(x)' #(input('Enter the function, for e.g. {sin(x)}: '))
c=0 #int(input('Enter the value of c in taylor series: '))
lim=np.linspace(x,y,10,dtype="float")
print(len(lim))
taylor(lim,n,c,st)