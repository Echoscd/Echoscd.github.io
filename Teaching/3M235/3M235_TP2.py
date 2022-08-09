# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# -*- coding: utf-8 -*-
"""
Ã‰diteur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


texte = open("3M235_TP2_Immunoglobuline.pdb").read()

'''
with open("3M235_TP2_Immunoglobuline.pdb", "r") as f:
    array = []
    for line in f:
        array.append(line)
'''


####Step 1: Read protein list

with open("3M235_TP2_Immunoglobuline.pdb", "r") as f:
    array = []
    for line in f:
        if "ATOM" in line:
            r = line.split()
            array.append([r[6], r[7], r[8]])
f.close()

prt_array = np.array(array, dtype='float').T 
    

####Step 2: Read mysterious protein
mys_array = np.loadtxt("3M235_TP2_Chaine_Mystere.txt").T


###Step 3: Recenter
def recenter(A):
    A_c = np.zeros(np.shape(A))
    center = np.zeros(np.shape(A[:,0]))
    for i in range(len(A)):
        center[i] = np.mean(A[i,:])
        A_c[i,:] = A[i,:] - center[i]
    return A_c
    
mys_array_c = recenter(mys_array)





###Step 4: Calcul of errors
L = len(prt_array[0,:])
erreur = np.zeros(L-11)
for i in range(L-11):
    C = prt_array[:,i:i+12]
    A = recenter(C)
    u,s,vh = np.linalg.svd(np.dot(mys_array_c, A.T))
    R = np.eye(len(u))
    R[-1,-1] = np.linalg.det(np.dot(u,vh))    
    SO = np.dot(u,np.dot(R,vh))
    erreur[i] = np.linalg.norm(np.dot(SO,A)-mys_array_c)
    
    
    
###Step 5: Visualization
plt.figure()
plt.axis([0, len(erreur), 0, 5])
plt.scatter(range(len(erreur)), erreur) 
index = np.nonzero(erreur < 1)

###Step 6: 3D
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(mys_array_c[0,:], mys_array_c[1,:], mys_array_c[2,:])

#i = index[0][0]
i = 100
C = prt_array[:,i:i+12]
A = recenter(C)    
u,s,vh = np.linalg.svd(np.dot(mys_array_c, A.T))
R = np.eye(len(u))
R[-1,-1] = np.linalg.det(np.dot(u,vh))    
SO = np.dot(u,np.dot(R,vh))
ASO = np.dot(SO,A)

fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
#ax2.plot(A[0,:], A[1,:], A[2,:], color = 'r')
ax2.plot(ASO[0,:], ASO[1,:], ASO[2,:], color = 'r')


