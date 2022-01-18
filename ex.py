import numpy as np
import math
import matplotlib.pyplot as plt

def pow(x,n):
    s=1
    z=[]
    for j in range(len(x)):
      for i in range(n):
        s+=(x[j]**i)/math.factorial(i)
      z.append(s)
      s=1
    return z

def main(x):
  y=[]
  for i in range(len(x)):
    ele = np.exp(x[i])
    y.append(ele)
  return y

def plot(x,y):
  plt.plot(x,y)
  plt.show()

x1=int(input(("Enter starting limit: ")))
x2=int(input(("Enter ending limit: ")))
n=int(input(("Enter n: ")))
x=np.linspace(x1,x2,n,dtype="float")
y=main(x)
z=pow(x,n)
plot(x,z)
plot(x,y)