# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 22:25:14 2019

@author: Chenlin
"""

import numpy as np
import matplotlib.pyplot as plt


#EXO 1
def orthonormalisation(A):
    shape = np.shape(A)
    dim_max = shape[0]
    B = np.matrix(np.zeros(shape))
    A_temp = np.matrix(np.copy(A))
    dim = 0
    for i in range(shape[1]):
        vec = A_temp[:,i]
        norm = np.sqrt(np.dot(vec.T, vec))
        if norm == 0:
            continue
        else:
            dim = dim + 1
            vec = vec/norm
            B[:,i] = vec
            A_temp = A_temp  - np.dot(vec, np.dot(vec.T, A_temp))
        if dim == dim_max:
            break
    return B
    
    
    
A = np.random.rand(7,8)
B = orthonormalisation(A)



#EXO 2, beta[1] = constant at origin, beta[0] = pente
def regression_lineaire(nom_fichier):
    data = []
    with open(nom_fichier) as f:    
        for line in f:
            s = line.split()
            data.append(s)
    f.close()
    
    data = np.array(data, dtype = float)
    X = np.copy(data)
    X[:,1] = 1
    Y = data[:,1]
    beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    
    X_min = np.min(X[:,0])
    X_max = np.max(X[:,0])
    X_list = np.linspace(X_min, X_max, 101)
    plt.figure()
    plt.scatter(X[:,0], Y)
    plt.plot(X_list, beta[0]*X_list + beta[1],'r')
    return beta[1], beta[0]
    
c, k = regression_lineaire('3M235_TP_note.txt')