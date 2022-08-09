# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:07:21 2019

@author: Chenlin
"""

import numpy as np

'''
Question 1
'''
A = np.array([[4,6,-2,3],[2,-1,0,1],[-7,0,1,12]])
A[0:2, :] = A[0:2, :] * 2
A[:,-1] = A[:,-1] * 3

B = np.ones([3,3])
B[0,:] = np.arange(4,7)
B[1,:] = np.arange(5,20,5)

C = np.copy(A[0:3,0:3])

D = np.dot(B, A)
E = B * C

E_sum = np.sum(E)
Y = np.sum(D, 1)



'''
Question 2
'''
A = np.array([[4,5,6,-1],[5,10,15,2],[6,15,1,4],[-1,2,4,-2]])
W,V = np.linalg.eig(A)
# np.dot(A,V) = W * V
A_inv_1 = np.dot( V*1/W , V.transpose())
# A^-1 = V W^-1 V^T
A_inv_2 = np.linalg.inv(A)

def compa_inverse(A):
    W,V = np.linalg.eig(A)
    A_inv_1 = np.dot( V*1/W , V.transpose())
    A_inv_2 = np.linalg.inv(A)
    return A_inv_1, A_inv_2, W, V
    

n = 5
A = np.eye(n)
B = np.eye(n-1)
A = A * 2
A[0:-1,1:] = A[0:-1,1:]-B
A[1:,0:-1] = A[1:,0:-1]-B

A_inv_1, A_inv_2, W, V = compa_inverse(A)
W = np.sort(W)

eig = 4 * np.sin(np.arange(1,n+1) * np.pi/(2 * (n+1)))**2




'''
Question 3
'''
A = np.array([[1,-1,2,1,2],[-1,2,3,-4,1],[0,-1,1,0,0]])
rank = np.linalg.matrix_rank(A)

A = np.array([[1,-1,2],[-1,2,3],[0,-1,1]])
b = np.array([3,-7,1])
x = np.linalg.solve(A,b)