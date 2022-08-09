# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:32:22 2019

@author: Chenlin
"""

import numpy as np
import matplotlib.pyplot as plt

 # la fonction pivot
def pivot(M,i,j):
     # M est une np.array (2 dimensions)
    # i indice de la ligne
    # indice de la colonne
    N = M.copy ()
    l,c = np.shape(N)
    for k in np.arange(l):
        if k==i : # on est sur la ligne de i
            N[k ,:] = M[k ,:]/M[k,j] # on normalise la ligne pour avoir 1 en (i,j)
        else:
            # on soustrait aux lignes pour annuler au dessus et en dessous du pivot
            N[k ,:]=M[k ,:] - M[k,j]/M[i,j]*M[i ,:]
    return N
    
    
def test_optimalite_sommet(M):
    optimal = 0
    d = M[-1,:-1]
    if (np.sum(d<=0) == len(d)):
        optimal = 1
    return optimal    
    
def critere_naturel(M):
    d = M[-1,:-1]
    j = np.argmax(d)
    A_j = M[:-1,j]
    b = M[:-1,-1]
    div = A_j/b
    i = np.argmax(div)
    if div[i] < 0:
        i = -1
    return i,j
    
def critere_bland(M):
    d = M[-1,:-1]
    j = np.nonzero(d>0)[0][0]
    A_j = M[:-1,j]
    b = M[:-1,-1]
    div = A_j/b
    i = np.argmax(div)
    if div[i] < 0:
        i = -1
    return i,j
    
def methode_simplexe_premiere_espece_naturel(M):
    M_opt = np.copy(M)
    optimal = test_optimalite_sommet(M)
    niter = 0
    while((optimal == 0) & (niter < 10000)):
        i,j = critere_naturel(M_opt)
        M_opt = pivot(M_opt,i,j)
        optimal = test_optimalite_sommet(M_opt)
        niter += 1
    return M_opt, niter
    
def methode_simplexe_premiere_espece_bland(M):
    M_opt = np.copy(M)
    optimal = test_optimalite_sommet(M)
    niter = 0
    while((optimal == 0) & (niter < 10000)):
        i,j = critere_bland(M_opt)
        M_opt = pivot(M_opt,i,j)
        optimal = test_optimalite_sommet(M_opt)
        niter += 1
    return M_opt, niter
    
#EXO 1
'''    
A = np.array([[1,2,1,0,0], [-2,1,0,1,0], [1,2,0,0,1]], dtype = float)
b = np.array([[1],[0],[2]], dtype = float)
C = np.array([[1],[2],[0],[0],[0]], dtype = float)
zero = np.array([[0]], dtype = float)
M = np.vstack((np.hstack((A,b)), np.hstack((C.T, zero))))

M_temp = pivot(pivot(pivot(M, 0, 0), 1, 3), 2,4)

B = np.array([[1,0,0],[-2,1,0],[1,0,1]], dtype = float)
B_inv = np.linalg.inv(B)
B_inv_A = np.dot(B_inv, A)
B_inv_b = np.dot(B_inv, b)

CN = C.T[0,[1,2]] - np.dot(C.T[0,[0,3,4]],B_inv_A[:,[1,2]])
'''




#EXO 2
A = np.array([[-1,2,1,0,-1], [1,2,0,1,-1]], dtype = float)
b = np.array([[-2],[10]], dtype = float)
C = np.array([[0],[0],[0],[0],[-1]], dtype = float)
zero = np.array([[0]], dtype = float)
M = np.vstack((np.hstack((A,b)), np.hstack((C.T, zero))))

M_temp1 = pivot(pivot(M, 0, 2), 1, 4)
M_temp2 = pivot(pivot(M, 1, 3), 0, 4)

M_n, niter_n = methode_simplexe_premiere_espece_naturel(M)
i,j = np.shape(M_n)
M_ini = np.zeros([i,j-1])
M_ini[:-1, :] = M_n[:-1, :-1]
M_ini[:-1,-1] = M_n[:-1,-1]
M_ini[-1,:] = np.array([2,4,0,0,0], dtype = float)
M_ini_n, niter_n = methode_simplexe_premiere_espece_naturel(M_ini)
