# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 22:50:16 2019

@author: Chenlin
"""

import matplotlib.pyplot as plt
import numpy as np

#EX 1

A = np.array([[4,2,1,4,5,6,7],[1,4,-6,2,2,0,-2],[1,-2,3,3,-5,6,1],[1,-1,1,-1,2,-3,-1],[1,1,1,8,2,3,4]])
b = np.array([[1],[2],[-10],[-2],[3]])
M = np.concatenate((A,b),axis=1)

def solvebypivot(M):
    shape = np.shape(M)
    N = np.array(M,dtype = float)
    for i in range(shape[0]):
        if N[i,i] != 0:
            N[i,:] = N[i,:]/N[i,i]
            for j in range(i+1, shape[0]):
                N[j,:] = N[j,:] - N[j,i]*N[i,:]
    return N
    
N = solvebypivot(M)
Q = np.random.rand(20,30)
d = np.arange(20).reshape(20,1)
M_2 = np.concatenate((Q,d), axis = 1)
N_2 = solvebypivot(M_2)


#EX 2
'''
Vector representation, V_m takes the place of e_j
Attention : keep A[j,m] not changed and float !
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
    
'''
We should have C = PB == A
V_2 and V_4 cannot replace e_3 since they are not pivot.
'''
#EX 3
'''
A = np.array([[3,4,-2,1],[1,-1,0,1],[-2,0,8,0]])
rank = np.linalg.matrix_rank(A)
B = pivot(A, 2, 2)
P = np.eye(3)
P[:,2] = A[:,2]
C = np.dot(P,B)
'''

#EX 4
'''
A = np.array([[1,3,2,5,0],[2,7,0,0,-1],[-2,-4,3,2,-1]], dtype = float)
#D = np.array(A[0:3, 0:3], dtype = float)
D = np.array(A[:,[0,1,3]], dtype = float) 
rank = np.linalg.matrix_rank(D)
D_aug = np.concatenate((D, np.eye(3)), axis = 1)
D_inv_aug = pivot(pivot(pivot(D_aug, 0, 0), 1, 1), 2, 2)
D_inv = D_inv_aug[0:3,3:]
Id_ver = np.dot(D[0:3,0:3], D_inv)
A_b = np.concatenate((A,np.array([[5],[-1],[-2]], dtype = float)), axis = 1)
D_A_b = np.dot(D_inv, A_b)
'''