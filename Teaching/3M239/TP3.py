# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:16:24 2019

@author: Chenlin
"""

import matplotlib.pyplot as plt
import numpy as np

#EX 1

b = np.array([[8],[5],[36]],dtype = float)
A = np.array([[1,2,0],[1,1,0],[9,4,0]], dtype = float)
A1 = np.copy(A)
A1[0,2]=1
x_base = np.linalg.solve(A1,b)

N = 11
'''
y1 = np.linspace(0,4,N)
x1 = 8 - 2*y1
y2 = np.linspace(0,5,N)
x2 = 5 - y2
y3 = np.linspace(0,9,N)
x3 = 9 - 4.0/9 * y3
'''
x = np.linspace(0,10,100)
y1 = 4 - 0.5 * x
y2 = 5 - x
y3 = 9 - 9 * x / 4
ax = plt.figure()
plt.plot(x,y1, color = 'r')
plt.plot(x,y2, color = 'g')
plt.plot(x,y3, color = 'b')
y = np.min(np.array([y1,y2,y3]), 0)
plt.fill_between(x, y, y2=0,  color = 'g')

xy_sommet1 = np.linalg.solve(A[:2,:2],b[:2])
xy_sommet2 = np.linalg.solve(A[1:,:2],b[1:])

'''
C_max = 20
C = np.linspace(0, C_max, C_max+1)
a = 1.0
for i in range(C_max+1):
    x4 = np.linspace(0,C[i]/a,11)
    y4 = C[i] - a * x4
    plt.plot(x4,y4, linestyle = '--', color = 'm')
'''    
    

#EX 3
'''
def pivot(A, j, m):
    shape = np.shape(A)
    N = np.array(A, dtype = float)
    pivot = A[j,m]+0.0
    if A[j,m] != 0:
        for i in range(shape[0]):
            if i == j:
                N[i,:] = N[i,:]/pivot
            else:
                N[i,:] = N[i,:] - A[i,m]/pivot * A[j,:]
            
    return N
    
A = np.array([[1,2,1,0,0],[1,1,0,1,0],[9,4,0,0,1]], dtype = float)
b = np.array([[8],[5],[36]],dtype = float)
M = np.concatenate([A,b],1)
N = pivot(pivot(pivot(M,0,1),1,3),2,4)
test = np.dot(A[:,[1,3,-1]], N[:,-1]) - np.array(b[:,0])

#Three test
N = pivot(pivot(pivot(M,0,0),1,1),2,4)
test = np.dot(A[:,[0,1,-1]], N[:,-1]) - np.array(b[:,0])
'''
