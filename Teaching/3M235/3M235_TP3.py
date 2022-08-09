# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

###ETAPE 1
def image_read(name):
    img = mpimg.imread(name)
    img = np.array(img * 256, dtype = 'int')
    return img
    
'''    
img = image_read('./faces/images/person09_04.png')
plt.imshow(img, cmap='gray')


Dic = {}
Dic['Apple'] = 'red'
Dic['Orange'] = 'orange'

vec = np.reshape(img, 2500)
'''

'''
### STEP 2 
Train = {}
Train_matrix = np.zeros([11, 54, 2500])
Train_index = np.zeros(11)
with open("./faces/train.txt", "r") as f:
    for line in f:
        r = line.split()
        index = int(r[1])
        img = image_read(r[0])
        vec = np.reshape(img, 2500)
        Train_matrix[index, Train_index[index], :] = vec
        Train_index[index] += 1
f.close()
for i in range(1,11):
    Train[i] = Train_matrix[i]




### STEP 3
SVD = {}
for i in range(1,11):
    u,s,vh = np.linalg.svd(Train[i])
    SVD[i] = u,s,vh
'''


'''    
### STEP 4
vec = SVD[1][2][40]
img = np.reshape(vec, [50,50])
plt.imshow(img, cmap='gray')
'''

'''
### STEP 5
Test_matrix = np.zeros([100, 2500])
Test_index = np.zeros(100)
num = 0
with open("./faces/test.txt", "r") as f:
    for line in f:
        r = line.split()
        index = int(r[1])
        img = image_read(r[0])
        vec = np.reshape(img, 2500)
        Test_matrix[num, :] = vec
        Test_index[num] = index
        num += 1
f.close()
'''

def comparaison(vec, SVD, N):
    projection = np.zeros([11, 2500])
    erreur = np.zeros(11)
    for i in range(1,11):
        for j in range(N):
            vec_sin = SVD[i][2][j]
            projection[i] += vec_sin * np.dot(vec_sin, vec)
        erreur[i] = np.linalg.norm(projection[i] - vec)
    return projection, erreur

N = 10
vec = Test_matrix[86]
projection, erreur = comparaison(vec, SVD, N)
img = np.reshape(vec, [50,50])
plt.figure()
plt.imshow(img, cmap='gray')


img = np.reshape(projection[9], [50,50])
plt.figure()
plt.imshow(img, cmap='gray')


#STEP 6 AUTOMATISER
Prediction_index = np.zeros(100)
for i in range(100):
    vec = Test_matrix[i]
    projection, erreur = comparaison(vec, SVD, N)
    erreur[0] = np.Infinity
    Prediction_index[i] = np.argmin(erreur)
precision = np.average(Prediction_index == Test_index)

