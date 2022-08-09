# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #y = x**2 - 10
    #y = x**4 - 30*x**2 -1
    y = x**4 - 10 * x **3 - 30*x**2 -1
    return y
    
def df(x, delta):
    df = (f(x+delta) - f(x-delta))/(2 * delta)
    return df
    
def GD(x0, N):
    x = x0
    y = np.zeros(N+1)
    y[0] = x0
    for i in range(N):
        l = 1.0/(i + 1000)
        x = x - l * df(x, l/10)
        y[i+1] = x
    return x, y
    
x_list = np.linspace(-5, 5, 100)
plt.figure()
plt.plot(x_list, f(x_list))    
    
x0 = -2
N = 100
x,y = GD(x0, N)
plt.figure()
plt.plot(range(N+1), y)
    
