# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y=np.log(x**2+3)
    return y

def fp(x):
    y=(2*x)/(x**2+3)
    return y

def fpp(x):
    y=(-2*x**2+6)/((x**2+3)**2)
    return y

g=np.arange(-10,10,0.01)
plt.figure()
plt.subplot(1,3,1)
plt.plot(g,f(g),'r')
plt.subplot(1,3,2)
plt.plot(g,fp(g),'b')
plt.subplot(1,3,3)
plt.plot(g,fpp(g),'g')
plt.show()


