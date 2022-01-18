import numpy as np
import matplotlib as plt
from numpy.core.function_base import linspace
import sympy as sp
import math

def taylor(x,fx,X,c,n):
    lim=linspace(x,X,dtype='float')
    fX=[]
    i=j=1
    for i in range(len(x)):
        s=1
        for j in range(n):
            s+=(1/math.factorial(n))*(derivative(fx,n))*((x-c)**n)
        fX.append(s)
    return fX

def derivative(st, n):
    f=sympify(st)
    if n==1:
        return f(x(t))
    else:
        return derivative(f,n-1).diff(t).replace(sp.Derivative,lambda *args: f(x(t)))

def main_function(x):
    y=[]
    for i in range(len(x)):
        ele=np.exp(x[i])
        y.append(ele)
    return y
        

def exp_fn(x,n):
    y=[]
    for i in range(len(x)):
        ele=Exp_single(x[i],n)
        y.append(ele)
    return y

def add_vec(p,q,i):
    p[i,:]=q
    return p

def MyExp(x,n):
    o_m=np.zeros([len(n),len(x)])
    label_list=[]
    for i in range(len(n)):
        y1=exp_fn(x,n[i])
        o_m=add_vec(o_m,y1,i)
        title1=str("N="+str(n[i]))
        label_list.append(title1)
    plot_graph(x,o_m,label_list)


def plot_graph(X,o_m,label_list):
    Y=[]
    fig,ax=plt.subplots()
    for i in range(len(label_list)):
        plt.scatter(X,o_m[i,:],marker=".",label=label_list[i])
        plt.plot(X,o_m[i,:])
    y=main_function(X)
    plt.plot(X,y,label="exp x")
    ax.set_title("EXP FUNCTION")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.grid()
    plt.legend()
    plt.show()    


a=float(input("Enter lower limit: "))
b=float(input("Enter lower limit: "))
x=np.linspace(a,b,10,dtype="float")

fx=input("Enter the f(x): for example: For f(x)=sin x enter sin:- ") 