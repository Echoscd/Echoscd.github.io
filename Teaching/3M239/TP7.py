# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:42:03 2019

@author: Chenlin
"""


import numpy as np
import matplotlib.pyplot as plt

# la fonction pivot
def pivot(M,i,j):
# M est une np.array (2 dimensions)
# i indice de la ligne
# j indice de la colonne
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
    

# EXO 2    
def choix_auxilaire(M):
    i = np.argmin(M[:,-1])
    shape = np.shape(M)
    j = shape[1] - shape[0] - 1 + i  
    return i,j



# EXO 3    
def pivot_auxilaire(M):
    i,j = choix_auxilaire(M)
    M3 = np.copy(M)
    M3[i,:] = M3[i,:] * -1
    M3 = pivot(M3,i,-2)
    return M3

# EXO 4    
def resolution_auxilaire(M):
    M_opt, niter = methode_simplexe_premiere_espece_naturel(M)
    real = 1
    if M_opt[-1,-1] != 0:
        real = 0
    if M_opt[-1,-2] == 0:
        real = 0
    return M_opt, real
    
    
# la fonction mystère
def mystere(M):
    L,c = np.shape(M)
    gamma = -np.ones(L-1)
    for j in np.arange(c-1):
        if abs(M[L-1,j]) < 10**(-8):
            test = -1
            for i in np.arange(L-1):
                if abs(M[i,j]) > 10**(-8):
                    if test==-1:
                        test = i
                    else:
                        test = L
            if test!=L and test != -1 and abs(M[test ,j]-1) < 10**(-8):
                gamma[test]=j
    return gamma
    
    

# EXO 7    
def representation_auxilaire(M):
    L,c = np.shape(M)
    M_axl = np.zeros([L,c+1])
    M_axl[:,:-1] = np.copy(M)
    M_axl[-1,:] = 0
    M_axl[:,-1] = M[:,-1]
    M_axl[:,-2] = -1
    return M2
     
     
     
# EXO 8
def initialisation_simplexe(M):
    M_axl = representation_auxilaire(M)
    M_axl_pivot = pivot_auxilaire(M_axl)
    M_axl_opt, real = resolution_auxilaire(M_axl_pivot)
    L,c = np.shape(M_axl_opt)
    M_axl_initial = np.zeros([L,c-1])
    M_initial = np.copy(M)
    if(real == 1):
        M_axl_initial = np.copy(M_axl_opt[:,:-1])
        M_axl_initial[:,-1] = M_axl_opt[:,-1]
        gamma = mystere(M_axl_initial)
        for i in range(len(gamma)):
            M_initial = pivot(M_initial, i, int(gamma[i]))
    else:
        M_initial = np.copy(M_axl_opt)
    return M_initial

# EXO 9    
def methode_simplexe_deuxieme_espece(M):
    M_initial = initialisation_simplexe(M)
    M_opt, niter = methode_simplexe_premiere_espece_bland(M_initial)
    return M_opt



# EXO 10
def test_espece(b):
    if(np.min(b) < 0):
        espece = 2
    else:
        espece = 1
    return espece

# EXO 11
def representation_probleme(a, b, c):
    L,c = np.shape(a)
    M = np.zeros([L+1, L+c+1])
    M[:-1,:c] = np.copy(a)
    M[:-1,c:c+L] = np.eye(L)
    M[:-1,-1] = np.copy(b[:,-1])
    M[-1,:c] = np.copy(c)
    return M

# EXO 12
def methode_simplexe(a, b, c):
    M = representation_probleme(a, b, c)
    espece = test_espece(b)
    if(espece == 1):
        M_opt, niter = methode_simplexe_premiere_espece_bland(M)
    if(espece == 2):
        M_opt = methode_simplexe_deuxieme_espece(M)
    return M_opt

# EXO 6
A = np.array([[1,-1,1,0,0], [-3,1,0,1,0], [1,1,0,0,1]], dtype = float)
b = np.array([[-2],[2],[6]], dtype = float)
C = np.array([[1],[2],[0],[0],[0]], dtype = float)
zero = np.array([[0]], dtype = float)
M = np.vstack((np.hstack((A,b)), np.hstack((C.T, zero))))

A2 = np.array([[1,-1,1,0,0,-1], [-3,1,0,1,0,-1], [1,1,0,0,1,-1]], dtype = float)
C2 = np.array([[0],[0],[0],[0],[0],[-1]], dtype = float)
zero = np.array([[0]], dtype = float)
M2 = np.vstack((np.hstack((A2,b)), np.hstack((C2.T, zero))))


i,j = choix_auxilaire(M2)
M3 = pivot_auxilaire(M2)
M4, real =  resolution_auxilaire(M3)

#EXO 5 Find the base
gamma3 = mystere(M3)
gamma4 = mystere(M4)

M_axl = representation_auxilaire(M)
M_initial = initialisation_simplexe(M)
M_opt = methode_simplexe_deuxieme_espece(M)

a = np.array([[1,-1],[-3,1], [1,1]], dtype = float)
b = np.array([[-2],[2],[6]], dtype = float)
c = np.array([[1],[2]], dtype = float)

espece = test_espece(b)
M_new = representation_probleme(a, b, c)
M_new_opt = methode_simplexe(a, b, c)

