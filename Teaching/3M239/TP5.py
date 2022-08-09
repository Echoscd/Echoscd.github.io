# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:14:56 2019

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

'''    
#EXO 1    
A = np.array([[3,2,1,0,0,0], [5,1,0,1,0,0], [1,2,0,0,1,0], [1,4,0,0,0,1]], dtype = float)
b = np.array([[3],[1],[4],[5]], dtype = float)
C = np.array([[1],[2],[0],[0],[0],[0]], dtype = float)
zero = np.array([[0]], dtype = float)
M = np.vstack((np.hstack((A,b)), np.hstack((C.T, zero))))

#EXO 2
optimal = test_optimalite_sommet(M)

#EXO 3
i_n,j_n = critere_naturel(M)

#EXO 4
i_b, j_b = critere_bland(M)

#EXO 5
M_n, niter_n = methode_simplexe_premiere_espece_naturel(M)

#EXO 6
M_b, niter_b = methode_simplexe_premiere_espece_bland(M)
'''


A2 = np.array([[1.0/2,-11.0/2,-5.0/2,9,1,0,0,], [1.0/2,-3.0/2,-1.0/2,1,0,1,0], [1,0,0,0,0,0,1]], dtype = float)
b2 = np.array([[0],[0],[1]], dtype = float)
C2 = np.array([[10],[-57],[-9],[-24],[0],[0],[0]], dtype = float)
zero = np.array([[0]], dtype = float)
M2 = np.vstack((np.hstack((A2,b2)), np.hstack((C2.T, zero))))

#EXO 8
M2_n, niter2_n = methode_simplexe_premiere_espece_naturel(M2)

#EXO 9
M2_b, niter2_b = methode_simplexe_premiere_espece_bland(M2)