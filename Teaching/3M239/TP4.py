# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np

# la fonction pivot
def pivot(M,i,j):
 # M est une np.array (2 dimensions)
 # i indice de la ligne
 # indice de la colonne
    N = M.copy()
    l,c = np.shape(N)
    for k in np.arange(l):
        if k==i : # on est sur la ligne de i
            N[k,:] = M[k,:]/M[k,j] # on normalise la ligne pour avoir 1 en (i,j)
        else:
 # on soustrait aux lignes pour annuler au dessus et en dessous dupivot
            N[k,:]=M[k,:] - M[k,j]/M[i,j]*M[i,:]
    return N



def verify(M):
# La première ligne est le vecteur marginal
# Le dernière colonne est la solution de base
    X_B = M[1:, -1]
    Z = M[0,-1]
    if (np.sum(X_B >= 0) == (len(M)-1)):
        print "admissible "
        print "Z = " + str(-Z)
    return X_B, Z

print M

def Dantzig(M):
    
    return i,j


#EXO 1
'''
A = np.array([[1,2,1,0,0],[1,1,0,1,0],[9,4,0,0,1]], dtype = 'float')    
b = np.array([[8,5,36]], dtype = 'float').T
v = np.array([[2,1,0,0,0]], dtype = 'float')
v2 = np.concatenate((v,[[0]]),1)
M = np.concatenate((v2, np.concatenate((A,b), 1)), 0)


M = pivot(M, 1, 1)
print M
X_B, Z = verify(M)

M = pivot(M, 2,2)
print M
X_B, Z = verify(M)


M = pivot(M, 3,3)
print M
X_B, Z = verify(M)


M = pivot(M, 1,0)
print M
X_B, Z = verify(M)


M = pivot(M, 3,4)
print M
X_B, Z = verify(M)


M = pivot(M, 2,3)
print M
X_B, Z = verify(M)


M = pivot(M, 2,1)
print M
X_B, Z = verify(M)


M = pivot(M, 3,3)
print M
X_B, Z = verify(M)


M = pivot(M, 3,2)
print M
X_B, Z = verify(M)
'''

#EXO 2
A = np.array([[2,2,1,1,0,0],[1,2,2,0,1,0],[1,1,1,0,0,1]], dtype = 'float')    
b = np.array([[6000,7000,4000]], dtype = 'float').T
v = np.array([[20,18, 15, 0,0,0]], dtype = 'float')
v2 = np.concatenate((v,[[0]]),1)
M = np.concatenate((v2, np.concatenate((A,b), 1)), 0)

print M

